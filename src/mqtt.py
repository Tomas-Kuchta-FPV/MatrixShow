from .config import TESTING
from .config import MQTT_BROKER, MQTT_PORT, MQTT_USER, MQTT_PASS, MQTT_PYTHON_INFO_TOPIC
import json
from typing import Optional, TYPE_CHECKING

# Import paho only when actually using MQTT to avoid import errors during testing
if not TESTING:
    import paho.mqtt.client as mqtt
elif TYPE_CHECKING:
    # Allow static type checkers to see mqtt types without importing at runtime
    import paho.mqtt.client as mqtt

client: Optional["mqtt.Client"] = None

if TESTING:
    print("TESTING mode: MQTT messages will not be sent.")
    def mqtt_init(keepalive: int = 60) -> None:
        """Mock MQTT init function for testing mode."""
        print("Mock MQTT initialized")
        return None
    def mqtt_send(topic: str, payload: dict) -> None:
        """Mock MQTT send function for testing mode."""
        print(f"Mock publish to {topic}: {payload}")
        return None
    def mqtt_stop() -> None:
        """Mock MQTT stop function for testing mode."""
        print("Mock MQTT disconnected")
        return None

if not TESTING:
    def mqtt_init(keepalive: int = 60) -> "mqtt.Client":
        """Create and start an MQTT client.

        Returns the connected, loop-started `paho.mqtt.client.Client` instance.
        Note: this will attempt to connect to the broker defined in `src.config`.
        """
        global client
        client = mqtt.Client()

        # Set credentials if provided
        if MQTT_USER or MQTT_PASS:
            client.username_pw_set(MQTT_USER, MQTT_PASS)

        client.connect(MQTT_BROKER, MQTT_PORT, keepalive)
        client.loop_start()
        mqtt_send(MQTT_PYTHON_INFO_TOPIC, {"status": "MQTT Initialized"})
        print("MQTT initialized")
        return client

    def mqtt_send(topic: str, payload: dict) -> "mqtt.MQTTMessageInfo":
        """Send a message to the MQTT broker."""
        if client is None:
            raise RuntimeError("MQTT client is not initialized")
        info = client.publish(topic, json.dumps(payload))  # Implement resending when fails
        print(f"Published to {topic}: {payload}")
        return info


    def mqtt_stop() -> None:
        """Stop and disconnect the MQTT client."""
        global client
        if client is None:
            print("MQTT client not initialized; nothing to stop")
            return
        client.loop_stop()
        client.disconnect()
        client = None
        print("MQTT disconnected")