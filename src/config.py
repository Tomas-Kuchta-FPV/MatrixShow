MQTT_Enabled = True
MQTT_BROKER = "192.168.200.100"
MQTT_PORT = 1883
MQTT_USER = "mqtt"
MQTT_PASS = "ChytreMQTT"

SONOFF_Enabled = False

TESTING = False  # If True, do not actually send MQTT messages

MQTT_PYTHON_ZIGBEE2MQTT_TOPIC = "zigbee2mqtt/{DeviceName}/set"

MQTT_PYTHON_INFO_TOPIC = "python/info"

## LED Configuration

matrix = [
    ["HONZA","FERDA","bulb-r0c2","ONDREJ","bulb-r0c4","ANNA","bulb-r0c6","MILAN","TRANZISTOR","bulb-r0c9","bulb-r0c10","bulb-r0c11","bulb-r0c12","bulb-r0c13","bulb-r0c14","bulb-r0c15","bulb-r0c16"],
    ["bulb-r1c0","bulb-r1c1","bulb-r1c2","bulb-r1c3","bulb-r1c4","bulb-r1c5","bulb-r1c6","bulb-r1c7","bulb-r1c8","bulb-r1c9","bulb-r1c10","bulb-r1c11","bulb-r1c12","bulb-r1c13","bulb-r1c14","bulb-r1c15","bulb-r1c16"],
    ["bulb-r2c0","bulb-r2c1","bulb-r2c2","bulb-r2c3","bulb-r2c4","bulb-r2c5","bulb-r2c6","bulb-r2c7","bulb-r2c8","bulb-r2c9","bulb-r2c10","bulb-r2c11","bulb-r2c12","bulb-r2c13","bulb-r2c14","bulb-r2c15","bulb-r2c16"],
]