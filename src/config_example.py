#You can Choose from various configuration options below.

DEBUG_PRINTS = True  # Set to True to enable debug prints, good for testing

# MQTT Configuration
ZIGBEE2MQTT_ENABLED = False
MQTT_BROKER = "192.168.1.50"
MQTT_PORT = 1883
MQTT_USER = "mqtt"
MQTT_PASS = "mqttpassword"

MQTT_PYTHON_ZIGBEE2MQTT_TOPIC = "zigbee2mqtt/{DeviceName}/set"

MQTT_PYTHON_INFO_TOPIC = "python/info"

# Sonoff DIY mode configuration
SONOFF_ENABLED = False
SONOFF_MS = 100 # transition time in ms for Sonoff DIY mode

# Homeassistant Configuration on websocket
HOMEASSISTANT_ENABLED = True
HOMEASSISTANT_URL = "ws://localhost:8123"
# A long-lived access token from your Home Assistant user
HOMEASSISTANT_TOKEN = ""


# Scheduling options
# Set to True to enable automatic on/off by time (local system time)
SCHEDULE_ENABLED = True
# Times are in 24h "HH:MM" format. Examples: "08:00" or "22:30"
ON_TIME = "17:00"   # time to turn on effects
OFF_TIME = "23:00"  # time to turn off effects

# If you prefer a different timezone handling, implement it in main.py

## LED Configuration
### for Zigbee2MQTT friendly names
'''
matrix = [
    ["bulb-r0c0","bulb-r0c1","bulb-r0c2","bulb-r0c3","bulb-r0c4","bulb-r0c5","bulb-r0c6","bulb-r0c7","bulb-r0c8","bulb-r0c9","bulb-r0c10","bulb-r0c11","bulb-r0c12","bulb-r0c13","bulb-r0c14","bulb-r0c15","bulb-r0c16"],
    ["bulb-r1c0","bulb-r1c1","bulb-r1c2","bulb-r1c3","bulb-r1c4","bulb-r1c5","bulb-r1c6","bulb-r1c7","bulb-r1c8","bulb-r1c9","bulb-r1c10","bulb-r1c11","bulb-r1c12","bulb-r1c13","bulb-r1c14","bulb-r1c15","bulb-r1c16"],
    ["bulb-r2c0","bulb-r2c1","bulb-r2c2","bulb-r2c3","bulb-r2c4","bulb-r2c5","bulb-r2c6","bulb-r2c7","bulb-r2c8","bulb-r2c9","bulb-r2c10","bulb-r2c11","bulb-r2c12","bulb-r2c13","bulb-r2c14","bulb-r2c15","bulb-r2c16"],
]
'''
### For Sonoff DIY mode IPs
'''
matrix = [
        ["192.168.1.100", "192.168.1.101", "192.168.1.102"],
        ["192.168.1.110", "192.168.1.111", "192.168.1.112"],
    ]
'''