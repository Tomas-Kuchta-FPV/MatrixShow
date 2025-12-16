"""
Home Assistant WebSocket protocol helper.

This module provides a minimal WebSocket client for Home Assistant's
`/api/websocket` API. It supports authenticating with a long-lived access
token and sending `call_service` messages. Incoming messages can be handled
by registering an event callback via `set_event_handler()`.

Configuration (see `src/config.py`):
- `HOMEASSISTANT_ENABLED` (bool)
- `HOMEASSISTANT_URL` (ws:// or wss:// URL, e.g. "ws://homeassistant.local:8123")
- `HOMEASSISTANT_TOKEN` (long-lived access token)

Sample `matrix` / usage notes:
- Home Assistant typically uses entity IDs rather than raw IPs. Example
    per-device matrix entry: ["homeassistant", "light.living_room", "Living Room"]

Example usage:
    ha_init()
    call_service('light', 'turn_on', {'entity_id': 'light.living_room'})
"""

from ..config import DEBUG_PRINTS, HOMEASSISTANT_URL, HOMEASSISTANT_TOKEN
import json
import threading
import time
import websocket

ws_app = None
ws_thread = None
_id_counter = 1
_event_handler = None
_connected = False

def _next_id():
    global _id_counter
    _id_counter += 1
    return _id_counter

def _on_message(ws, message):
    global _event_handler
    try:
        data = json.loads(message)
    except Exception:
        if DEBUG_PRINTS: print("HA WS: received non-json message", message)
        return
    if DEBUG_PRINTS: print("HA WS RX:", data)
    # pass the parsed message to the user handler if set
    if _event_handler:
        try:
            _event_handler(data)
        except Exception as e:
            if DEBUG_PRINTS: print("HA WS: event handler error", e)

def _on_open(ws):
    global _connected
    if DEBUG_PRINTS: print("HA WS: connection opened, sending auth")
    # send auth message
    if not HOMEASSISTANT_TOKEN:
        if DEBUG_PRINTS: print("HA WS: no HOMEASSISTANT_TOKEN configured")
        return
    auth_msg = {"type": "auth", "access_token": HOMEASSISTANT_TOKEN}
    ws.send(json.dumps(auth_msg))

def _on_error(ws, err):
    if DEBUG_PRINTS: print("HA WS error:", err)

def _on_close(ws, code, reason):
    global _connected
    _connected = False
    if DEBUG_PRINTS: print(f"HA WS closed: code={code} reason={reason}")

def _run_forever(url):
    global ws_app, _connected
    ws_app = websocket.WebSocketApp(url,
                                    on_message=_on_message,
                                    on_open=_on_open,
                                    on_error=_on_error,
                                    on_close=_on_close)
    _connected = True
    # run_forever is blocking; run in this thread
    try:
        ws_app.run_forever()
    finally:
        _connected = False

def ha_init():
    """Start the Home Assistant websocket client in a background thread."""
    global ws_thread, ws_app
    url = HOMEASSISTANT_URL.rstrip('/') + '/api/websocket'
    if DEBUG_PRINTS: print("HA WS: connecting to", url)
    ws_thread = threading.Thread(target=_run_forever, args=(url,), daemon=True)
    ws_thread.start()
    # wait a short moment for connection/auth sequence
    time.sleep(0.2)
    return ws_app

def set_event_handler(callback):
    """Set a callable to receive incoming websocket messages (dict)."""
    global _event_handler
    _event_handler = callback

def call_service(domain: str, service: str, service_data: dict) -> int:
    """Call a Home Assistant service. Returns the message id used.

    Example: call_service('light','turn_on', {'entity_id':'light.foo'})
    """
    global ws_app
    if ws_app is None:
        raise RuntimeError("HA WS client not initialized")
    mid = _next_id()
    msg = {"id": mid, "type": "call_service", "domain": domain, "service": service, "service_data": service_data}
    try:
        ws_app.send(json.dumps(msg))
        if DEBUG_PRINTS: print("HA WS TX:", msg)
    except Exception as e:
        if DEBUG_PRINTS: print("HA WS: send failed", e)
        raise
    return mid

def ha_stop():
    """Stop the websocket client and background thread."""
    global ws_app
    if ws_app:
        try:
            ws_app.close()
        except Exception:
            pass
    if DEBUG_PRINTS: print("HA WS: stopped")
