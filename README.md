# Python-RPi-rgbw-led

(In Process)


Using a mqtt listener to pass messages to a socket server that uses a pid launcher to 
run rutines

Sys_Startup is a PHP script used for Raspberry PI startup.
Instead of filling the CRON with @reboot I use this script to run all the gadgets I want at startup

I have also included logs and log rotate using logrotate.

There is a config file sys_startup.ini
If the PI is using temp probes or relays, you can set configuration in the .ini file

Dillinger is a cloud-enabled, mobile-ready, offline-storage, AngularJS powered HTML5 Markdown editor.

  - Type some Markdown on the left
  - See HTML in the right
  - Magic
### Version
0.0.1

### Tech


### Installation

You'll need:
    Hardware:
        Raspberry pi
        Mosfets or Mosfet board
        Power supply for RGBW leds 
    Software:
        - Python3
        - paho-mqtt
        - A running Mosquito broker
        - pi-blaster     
        - If using relays -[WiringPi] by Gorden

```sh
$ npm i -g gulp
```


```sh
$ git clone [git-repo-url] pi-sys-start
$ cd dillinger
$ npm i -d
$ mkdir -p downloads/files/{md,html,pdf}
$ gulp build --prod
$ NODE_ENV=production node app
```

[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)

[Steggy]: <https://github.com/steggy>
[git-repo-url]: <https://github.com/steggy/python-RPi-rgbw-led.git>
[WiringPi]: <http://wiringpi.com>
