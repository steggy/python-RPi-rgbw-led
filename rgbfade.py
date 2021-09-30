#!/usr/bin/env python3

import RPi.GPIO as GPIO
import sys, time, random
from threading import Thread

CHECKVERSION = "0.1.0"

PWMLedRed = 22
PWMLedGreen = 23
PWMLedBlue = 24
PWMLedWhite = 25
ledcolor = {'red':PWMLedRed,'green':PWMLedGreen, 'blue' : PWMLedBlue,'white':PWMLedWhite}
newledvalue = [0,0,0]
currentledvalue = [0,0,0]
counter = [0,0]
BLAST = "/dev/pi-blaster"
dled = [0,0,0]

def random_color():
    global counter
    global newledvalue

    if counter[1] == 0:
        newledvalue[0] = random.randrange(0, 10,2)
        newledvalue[1] = 0
        newledvalue[2] = random.randrange(0, 10,2)
    elif counter[1] == 1:
        newledvalue[0] = random.randrange(0, 10,2)
        newledvalue[1] = random.randrange(0, 10,2)
        newledvalue[2] = 0
    elif counter[1] == 2:
        newledvalue[0] = 0
        newledvalue[1] = random.randrange(0, 10,2)
        newledvalue[2] = random.randrange(0, 10,2)
    counter[1] += 1
    #print('%s = %s, %s = %s, %s = %s' % ('RED', str(newledvalue[0]), 'GREEN', str(newledvalue[1]), 'BLUE', str(newledvalue[2])))

def rgbfade():
    global currentledvalue
    global newledvalue
    global dled
    pins=[22,23,24]
    for i in range(3):
        if currentledvalue[i] < newledvalue[i]:
            dled[i] = 1
        else:
            dled[i] = 0
        #print('DLED ' + str(dled[i]))
    while currentledvalue[0] != newledvalue[0] or currentledvalue[1] != newledvalue[1] or currentledvalue[2] != newledvalue[2]:
        for i in range(3):
            if currentledvalue[i] != newledvalue[i]:
                if dled[i] == 1:
                    currentledvalue[i] += 1
                    #print('change pin (' + str(pins[i]) + ') value to ' + str(currentledvalue[i]))
                    with open('/dev/pi-blaster', 'w') as out_file:
                        place = str(pins[i]) + '=' + str("{:0.2f}".format(currentledvalue[i] / 10 )) + '\n'
                        out_file.write(place) 
                else:
                    currentledvalue[i] -= 1
                    #print('change pin (' + str(pins[i]) + ') value to ' + str(currentledvalue[i]))
                    with open('/dev/pi-blaster', 'w') as out_file:
                        place = str(pins[i]) + '=' + str("{:0.2f}".format(currentledvalue[i] / 10 )) + '\n'
                        out_file.write(place) 
            else:
                #print('PIN ' + str(pins[i]) + ' is Equal c=' + str(currentledvalue[i]) + ' n=' + str(newledvalue[i]))
                pass
        time.sleep(0.23)
                
def off():
    with open('/dev/pi-blaster', 'w') as out_file:
        out_file.write('22=0\n')
        out_file.write('23=0\n')
        out_file.write('24=0\n')
        
    
def main():
    # put the counter loop here to hold the color for 10 count cnt or counter[0]
    # while true:
    cnt = 0
    rgb = 0
    random_color()
    #print("Led red color value " + str(currentledvalue[0]))
    #print("Led red NEW color value " + str(newledvalue[0] / 100 ))
    try:
        while True:
            random_color()
            if counter[1] > 2:
                counter[1] = 0
            
            cnt += 1
            if cnt == 5:
                #print('SOLID')
                if rgb == 0:
                    newledvalue[0] = 10
                    newledvalue[1] = 0
                    newledvalue[2] = 0
                    rgb += 1
                elif rgb == 1:
                    newledvalue[0] = 0
                    newledvalue[1] = 10
                    newledvalue[2] = 0
                    rgb += 1 
                else:
                    newledvalue[0] = 0
                    newledvalue[1] = 0
                    newledvalue[2] = 10
                    rgb = 0
                cnt = 0    
            rgbfade()
            #print('In Main current red value ' + str(currentledvalue[0]))
            #print('%s = %s, %s = %s, %s = %s' % ('RED', str(newledvalue[0]), 'GREEN', str(newledvalue[1]), 'BLUE', str(newledvalue[2])))
            time.sleep(5)
    except Exception as e:
        print(e)
    except:
        print('Thanks for playing')
        off()





if __name__ == "__main__":
    main()


