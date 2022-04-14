# RPI Led Matrix Album Cover Display
##### Credits:
- Idea: [gonnabuysomewindows](https://www.reddit.com/r/raspberry_pi/comments/ombwwg/my_64x64_rgb_led_matrix_album_art_display_pi_3b/)
- Matrix driver: [hzeller/rpi-rgb-led-matrix](https://github.com/hzeller/rpi-rgb-led-matrix)
- Hardware: [adafruit](https://learn.adafruit.com/adafruit-rgb-matrix-bonnet-for-raspberry-pi/driving-matrices)
### HowTo
```sh
git clone https://github.com/hzeller/rpi-rgb-led-matrix.git
cd rpi-rgb-led-matrix/utils && make led-image-viewer
cd .. && git clone https://github.com/maxfer1221/python-rgb-matrix
cd python-rgb-matrix && pip3 install -r requirements.txt
```
I've included an `init.sh` script which sets up environment variabels and executes the python script to display the album covers. To use it, simply change the `{keys}` inside `init.sh`.
Alternatively, `export KEY_NAME=KEY_VAL` each key inside of `init.sh` and `sudo -E python3 ./test.py`.
Other LED matrix parameters can be changed from within the python script.
###### Optional:
Create a systemd (or equivalent) service that executes the script on startup/some event.

ex:
```
[Unit]
Description=Script service to run on wifi connection
Wants=network-online.target
After=network-online.target

[Service]
Type=simple
User=pi
WorkingDirectory=/home/pi
ExecStart=/home/pi/.onWiFi.sh
# onWiFi.sh:
# #!/bin/bash
# cd /path/to/init.sh 
# sudo sh init.sh

[Install]
WantedBy=multi-user.target
```

###### Old method
Add the lines inside `.bashrc` into your `~/.bashrc` to automatically start the led display on startup.
