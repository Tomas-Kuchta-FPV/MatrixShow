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

### Game plan
- [ ] build out and test the code at home
- [ ] get CADing and CAD out the matrix

- [ ] Get all the needed parts to the hackathon venue
- [ ] Build the electrical work there
  - [ ] Maybe try to import the bulbs I own. But I worry that TSA won't like that idea

### BOM
| Item                             | Qty    | Price ($) | Link/Source                                                                                                                                                        | Note                                                                                                                                    |
| -------------------------------- | ------ | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------- |
| WiFi LED bulbs                   | n      | 15 per pc | [Amazon](https://www.amazon.com/SONOFF-B05-BL-A19-Wi-Fi-Smart-Variable/dp/B09TB91WTF)                                                                              | Maybe these can be used as an alternative. [Amazon](https://www.amazon.com/Tapo-Equivalent-Matter-Certified-L535E-2-Pack/dp/B0DSJCN9RZ) |
| WiFi router (Proferably OpenWRT) | 1      | 40        | [Amazon](https://www.amazon.com/Dual-band-Gigabit-WiFi-Internet-Router/dp/B08KJF5BS7)                                                                                        | https://openwrt.org/toh/tp-link/archer-c5-c7-wdr7500                                                                                    |
| Wall light bulb holder           | n + 1  |           | [Home Depot](https://www.homedepot.com/p/Leviton-600-Watt-250-Volt-White-Outlet-Box-Lampholder-49875-R50-49875-000/207106566)                                      |
| WAGOS!                           | 10     | 9         | [Home Depot](https://www.homedepot.com/p/WAGO-221-413K006-000-3-Wire-Lever-Nuts-Conductor-Compact-Splicing-Connectors-12-24-AWG-10-Pack-221-413K006-000/334555570) |
| Lamp cable                       | 100ft  | 23        | [Home Depot](https://www.homedepot.com/p/Southwire-100-ft-18-2-Black-Stranded-CU-SPT-1-Lamp-Wire-49910303/304781536)                                               |
| Electrical tape                  | 6 pack | 10        | [Home Depot](https://www.homedepot.com/p/Commercial-Electric-1-2-in-x-20-ft-Electric-Tape-Multi-Color-6-Pack-30005336/206874157)                                   |
| Spade conenctors                 | 1 kit  | 19        | [Amazon](https://www.amazon.com/smseace-Connectors-Cnnectors-Stripping-Multifunction/dp/B0CSXV82C4)                                                                |



**Stand**
| Item                                  | Qty   | Price ($) | Link/Source                                                                                                                                       | Note                                    |
| ------------------------------------- | ----- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------- |
| OBS Board                             | 2     | 11        | [Home Depot](https://www.homedepot.com/p/OSB-7-16-Application-as-4ft-X-8-ft-Sheathing-Panel-386081/202106230)                                     |                                         |
| 2x4 lumber                            | 5     | 17,4      | [Home Depot](https://www.homedepot.com/p/2-in-x-4-in-x-8-ft-2-Premium-Grade-Dimensional-Lumber-441317/202094172)                                  |
| Screws                                | 1 box | 12        | [Home Depot](https://www.homedepot.com/p/Grip-Rite-9-x-3-in-Star-Drive-Dual-Flat-Head-Coarse-Thread-Construction-Screws-1-lb-Box-3GCS1/204959258) |
| Tools: Impact driver, Drill bits, Saw | -     | -         | Can be borrowed                                                                                                                                   |
| Home depod delivery                   | -     | 79        |                                                                                                                                                   | We cand disscuss logistics with alexren |



## External Docs

### Zigbee

https://www.zigbee2mqtt.io/devices/TZ3210_iw0zkcu8.html  

### Sonoff

https://help.sonoff.tech/docs/DIY-MODE-API-PROTOCOL  
**https://help.sonoff.tech/docs/B02BL-B05BL-API**  