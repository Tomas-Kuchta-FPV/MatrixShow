#You can Choose from various configuration options below.

DEBUG_PRINTS = True


MQTT_ENABLED = False
MQTT_BROKER = "192.168.200.100"
MQTT_PORT = 1883
MQTT_USER = "mqtt"
MQTT_PASS = "ChytreMQTT"

SONOFF_ENABLED = False
SONOFF_MS = 100 # transition time in ms for Sonoff DIY mode

MQTT_PYTHON_ZIGBEE2MQTT_TOPIC = "zigbee2mqtt/{DeviceName}/set"

MQTT_PYTHON_INFO_TOPIC = "python/info"

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

matrix = [
    ["192.168.22.221","FERDA","192.168.1.100","ONDREJ","192.168.1.101","ANNA","192.168.1.102","MILAN","TRANZISTOR","192.168.1.103","192.168.1.104","192.168.1.105","192.168.1.106","192.168.1.107","192.168.1.108","192.168.1.109","192.168.1.110"],
    ["192.168.1.111","192.168.1.112","192.168.1.113","192.168.1.114","192.168.1.115","192.168.1.116","192.168.1.117","192.168.1.118","192.168.1.119","192.168.1.120","192.168.1.121","192.168.1.122","192.168.1.123","192.168.1.124","192.168.1.125","192.168.1.126","192.168.1.127"],
    ["192.168.1.128","192.168.1.129","192.168.1.130","192.168.1.131","192.168.1.132","192.168.1.133","192.168.1.134","192.168.1.135","192.168.1.136","192.168.1.137","192.168.1.138","192.168.1.139","192.168.1.140","192.168.1.141","192.168.1.142","192.168.1.143","192.168.1.144"],
]


#matrix = [["192.168.22.221", "192.168.22.199", "192.168.22.116"]]