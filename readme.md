# MatrixShow

MatrixShow powers the LED matrix effects used in Světlo v Ulicích.  
It’s a lightweight framework for orchestrating light animations with a hardware abstraction layer, built for flexibility and experimentation.  


## Instalation
```shell
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
python -m pip install -r requirements.txt
cp src/config_example.py src/config.py
```

## Run it!
```shell
source .venv/bin/activate
python -m src.main
```
Use ``python -m Tools.GUI`` to draw and view the display.  

## Exhibitions
### Light in the streets or "Světlo v Ulicích"
Goal of this installation was to interestingly light up the streets.  
We thought of *smart home!*, and we found adressable LED bulb plopped them into laps, ~~wrote~~ vibecoded a code to control then in sequences So that's how this codebase was born.  
![Thomas](/Images/SvU26/Thomas.jpg)
![Side view](/Images/SvU26/Side%20view.jpg)

### Instalation at our school
This was made with zigbee bulbs and home assistant for the christmass hilidays.  
![testing](/Images/School/all%20on.jpg)
![Control interface](/Images/School/hass.jpg)

## And this year we are comming to Open Sauce!
My idea is to make a giant LED matrix on site at the [outpost hackathon](https://outpost.hackclub.com/).
The repo is here for it: https://github.com/Tomas-Kuchta-FPV/The_Hack-Club_cloud

## External Docs

### Zigbee

https://www.zigbee2mqtt.io/devices/TZ3210_iw0zkcu8.html  

### Sonoff

https://help.sonoff.tech/docs/DIY-MODE-API-PROTOCOL  
**https://help.sonoff.tech/docs/B02BL-B05BL-API**  