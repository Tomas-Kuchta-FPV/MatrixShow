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

## External Docs

### Zigbee

https://www.zigbee2mqtt.io/devices/TZ3210_iw0zkcu8.html  

### Sonoff

https://help.sonoff.tech/docs/DIY-MODE-API-PROTOCOL  
**https://help.sonoff.tech/docs/B02BL-B05BL-API**  