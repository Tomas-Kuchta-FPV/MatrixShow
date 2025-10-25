#You can Choose from various configuration options below.

DEBUG_PRINTS = True  # Set to True to enable debug prints

# MQTT Configuration
MQTT_ENABLED = False
MQTT_BROKER = "192.168.200.100"
MQTT_PORT = 1883
MQTT_USER = "mqtt"
MQTT_PASS = "ChytreMQTT"

MQTT_PYTHON_ZIGBEE2MQTT_TOPIC = "zigbee2mqtt/{DeviceName}/set"

MQTT_PYTHON_INFO_TOPIC = "python/info"

# Sonoff DIY mode configuration
SONOFF_ENABLED = False
SONOFF_MS = 100 # transition time in ms for Sonoff DIY mode


# Scheduling options
# Set to True to enable automatic on/off by time (local system time)
SCHEDULE_ENABLED = False
# Times are in 24h "HH:MM" format. Examples: "08:00" or "22:30"
ON_TIME = "14:52"   # time to turn on effects
OFF_TIME = "14:55"  # time to turn off effects

# If you prefer a different timezone handling, implement it in main.py

## LED Configuration
### for MQTT friendly names
'''
matrix = [
    ["HONZA","FERDA","bulb-r0c2","ONDREJ","bulb-r0c4","ANNA","bulb-r0c6","MILAN","TRANZISTOR","bulb-r0c9","bulb-r0c10","bulb-r0c11","bulb-r0c12","bulb-r0c13","bulb-r0c14","bulb-r0c15","bulb-r0c16"],
    ["bulb-r1c0","bulb-r1c1","bulb-r1c2","bulb-r1c3","bulb-r1c4","bulb-r1c5","bulb-r1c6","bulb-r1c7","bulb-r1c8","bulb-r1c9","bulb-r1c10","bulb-r1c11","bulb-r1c12","bulb-r1c13","bulb-r1c14","bulb-r1c15","bulb-r1c16"],
    ["bulb-r2c0","bulb-r2c1","bulb-r2c2","bulb-r2c3","bulb-r2c4","bulb-r2c5","bulb-r2c6","bulb-r2c7","bulb-r2c8","bulb-r2c9","bulb-r2c10","bulb-r2c11","bulb-r2c12","bulb-r2c13","bulb-r2c14","bulb-r2c15","bulb-r2c16"],
]
'''
### For Sonoff DIY mode IPs
'''
matrix = [
    ["192.168.22.221","FERDA","192.168.1.100","ONDREJ","192.168.1.101","ANNA","192.168.1.102","MILAN","TRANZISTOR","192.168.1.103","192.168.1.104","192.168.1.105","192.168.1.106","192.168.1.107","192.168.1.108","192.168.1.109","192.168.1.110"],
    ["192.168.1.111","192.168.1.112","192.168.1.113","192.168.1.114","192.168.1.115","192.168.1.116","192.168.1.117","192.168.1.118","192.168.1.119","192.168.1.120","192.168.1.121","192.168.1.122","192.168.1.123","192.168.1.124","192.168.1.125","192.168.1.126","192.168.1.127"],
    ["192.168.1.128","192.168.1.129","192.168.1.130","192.168.1.131","192.168.1.132","192.168.1.133","192.168.1.134","192.168.1.135","192.168.1.136","192.168.1.137","192.168.1.138","192.168.1.139","192.168.1.140","192.168.1.141","192.168.1.142","192.168.1.143","192.168.1.144"],
]
'''

# GYMPL
matrix = [
    ["10.12.1.13","10.12.1.14","10.12.1.15","10.12.1.16","10.12.1.31","10.12.1.17","10.12.1.18","10.12.1.32","10.12.1.20","10.12.1.21","10.12.1.26","10.12.1.22","10.12.1.28","10.12.1.24","10.12.1.25","10.12.1.64","10.12.1.27"],
    ["10.12.1.29","10.12.1.30","10.12.1.40","10.12.1.41","10.12.1.42","10.12.1.33","10.12.1.34","10.12.1.44","10.12.1.35","10.12.1.43","10.12.1.45","10.12.1.63","10.12.1.36","10.12.1.46","10.12.1.37","10.12.1.47","10.12.1.48"],
    ["10.12.1.38","10.12.1.49","10.12.1.50","10.12.1.51","10.12.1.52","10.12.1.53","10.12.1.54","10.12.1.55","10.12.1.57","10.12.1.56","10.12.1.59","10.12.1.58","10.12.1.62","10.12.1.60","10.12.1.61","10.12.1.39","10.12.1.19"],
]