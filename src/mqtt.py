from .config import MQTT_BROKER, MQTT_PORT, MQTT_USER, MQTT_PASS, MQTT_PYTHON_INFO_TOPIC
import paho.mqtt.client as mqtt
import json


def mqtt_init(keepalive: int = 60) -> mqtt.Client:
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

def mqtt_send(topic: str, payload: dict) -> mqtt.MQTTMessageInfo:
    """Send a message to the MQTT broker."""
    client.publish(topic, json.dumps(payload)) # Implement resending when fails
    print(f"Published to {topic}: {payload}")


def mqtt_stop():
    """Stop and disconnect the MQTT client."""
    client.loop_stop()
    client.disconnect()
    print("MQTT disconnected")