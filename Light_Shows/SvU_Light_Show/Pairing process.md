## I'll describe the pairing process that we used for SvU in here

1. Use a smart outlet tou turn the light 5x ON/OFF in 1.1s increments.
2. Pair it using it's own WiFi AP. Write downd its ID. Last 4 digits should work.
3. Find it using mDNS with `./find_ip_sonoff.sh xxxx` - we didn't do this at first which came to bite us by pairing only 15 bulbs out of 51.
4. Write down it's ID, IP, Position into a LibreOffice calc sheet.
5. Repeat a lot of times