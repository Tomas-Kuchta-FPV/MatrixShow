#You can Choose from various configuration options below.

DEBUG_PRINTS = False  # Set to True to enable debug prints

# Sonoff DIY mode configuration
SONOFF_ENABLED = True
SONOFF_MS = 100 # transition time in ms for Sonoff DIY mode


# Scheduling options
# Set to True to enable automatic on/off by time (local system time)
SCHEDULE_ENABLED = True
# Times are in 24h "HH:MM" format. Examples: "08:00" or "22:30"
ON_TIME = "17:00"   # time to turn on effects
OFF_TIME = "23:00"  # time to turn off effects

## LED Matrix Configuration

# GYMPL
matrix = [
    ["10.12.1.13","10.12.1.14","10.12.1.15","10.12.1.16","10.12.1.31","10.12.1.17","10.12.1.18","10.12.1.32","10.12.1.20","10.12.1.21","10.12.1.26","10.12.1.22","10.12.1.28","10.12.1.24","10.12.1.25","10.12.1.64","10.12.1.27"],
    ["10.12.1.29","10.12.1.30","10.12.1.40","10.12.1.41","10.12.1.42","10.12.1.33","10.12.1.34","10.12.1.44","10.12.1.35","10.12.1.43","10.12.1.45","10.12.1.63","10.12.1.36","10.12.1.46","10.12.1.37","10.12.1.47","10.12.1.48"],
    ["10.12.1.38","10.12.1.49","10.12.1.50","10.12.1.51","10.12.1.52","10.12.1.53","10.12.1.54","10.12.1.55","10.12.1.57","10.12.1.56","10.12.1.59","10.12.1.58","10.12.1.62","10.12.1.60","10.12.1.61","10.12.1.39","10.12.1.19"],
]