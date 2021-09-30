#!/usr/bin/env python3

import paho.mqtt.client as mqtt
#import RPi.GPIO as GPIO
import math, time, sys, os, logging, datetime, subprocess, socket
from decimal import Decimal
#import ConfigParser
from datetime import timedelta



#LOGFILE="/home/pi/bin/log_filename.txt"
LOGFILE = os.path.dirname(__file__) + "/log_filename.txt"

logging.basicConfig(filename=LOGFILE, level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')



cwd = os.getcwd()
#TOPIC = "smartthings/Livingroom RGBPI"
#TOPIC = "smartthings"
TOPIC = "livingroompi"
BROKER="192.168.33.88"

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

#config = ConfigParser.ConfigParser()
#config.read(cwd+'/mqtt.ini')


def publish_message(Topic, Msg):
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    
    client.connect(BROKER, 1883, 60)
    time.sleep(1)
    client.publish(Topic , Msg)
    time.sleep(1)
    client.publish(Topic , Msg)




def uptime():
    with open('/proc/uptime', 'r') as f:
        uptime_seconds = float(f.readline().split()[0])
        uptime_string = str(timedelta(seconds = uptime_seconds)).replace(',','')
        if 'day' in uptime_string:
            raw = uptime_string.split(' ')
            minn = raw[2].split(':')[1]
            hourr = raw[2].split(':')[0]
            if int(hourr) > 0:
                minn = '59'
        else:
            raw = uptime_string.split(':')
            hourr = raw[0]
            minn = raw[1]
            if int(hourr) > 0:
                minn = '59'

    #print(uptime_string)
    #print("Uptime String " + str(minn))
    return minn

def on_connect(self, client, userdata, rc):
    #print ("Connected with rc: " + str(rc))
    #client.subscribe('%s%s' % (TOPIC,"/#"))
    self.subscribe('%s%s' % (TOPIC,"/#"))


def sendsocket(msg):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(msg.encode())
        data = s.recv(1024)
    print('Received', repr(data.decode('UTF-8')))


def on_message(client, userdata, msg):
    print ("Topic: "+ msg.topic+"   Message: "+str(msg.payload.decode('utf-8')))
    message = msg.payload.decode('utf-8')
    
    if "livingroompi" in msg.topic:
            logging.debug("Topic: "+ msg.topic+" Message: "+str(message))
            try:
                sendsocket(msg.topic + '*' + message)
            except:
                pass
    
    
    

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(BROKER, 1883, 60)


try:
    client.loop_forever()
except KeyboardInterrupt:
    sys.exit(0)

#try:
#    user_input = input()
#except KeyboardInterrupt:
#    sys.exit(0)







# EOF
