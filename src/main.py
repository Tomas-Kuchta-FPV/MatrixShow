from time import sleep
from .init import init

from .LightEffects.blink_all import blink_all

def main():
    init() # Initialize the application
    sleep(0.5)
    while True:
     blink_all(500, 3, 1, 10)



# Call main function
if __name__ == "__main__":
    main()