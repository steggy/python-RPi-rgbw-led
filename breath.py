#! /usr/bin/python3

import RPi.GPIO as GPIO
import sys
import time
import optparse

CHECKVERSION = "0.1.0"

PWMLedRed = 22
PWMLedGreen = 23
PWMLedBlue = 24
PWMLedWhite = 25
ledcolor = {'red':PWMLedRed,'green':PWMLedGreen, 'blue' : PWMLedBlue,'white':PWMLedWhite}



def setgpiomode():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(PWMLedRed,GPIO.OUT)
    GPIO.setup(PWMLedGreen,GPIO.OUT)
    GPIO.setup(PWMLedBlue,GPIO.OUT)
    GPIO.setup(PWMLedWhite,GPIO.OUT)
    #GPIO.cleanup()





def pwm(color):
    global breath
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(color,GPIO.OUT)
    #setgpiomode()
    breath = GPIO.PWM(color, 1000)
    breath.start(0)
    while True:
        for dc in range(1, 101, 1):
            breath.ChangeDutyCycle(dc)
            time.sleep(0.02)
        for dc in range(100, 0, -1):
            breath.ChangeDutyCycle(dc)
            time.sleep(0.02)

def ledbreath(color):
    global breath
    while True:
        try:
            pwm(color)
        except KeyboardInterrupt:
            breath.stop()
            GPIO.cleanup()
            sys.exit()

def get_args():
    global parser
    usage = '%prog [-h] [--doc Detailed help ] [-f FILE] '
    parser = optparse.OptionParser(usage)
    parser.add_option('-t', '--topic', dest='topic')
    parser.add_option('-c', '--color', dest='color')
    parser.add_option('-v', action='store_true', dest='vers')
    parser.add_option('-s', action='store_true', dest='stop')

    return parser.parse_args()



def parseArgs():
    if options.stop:
        breath.stop()
        GPIO.cleanup()
        sys.exit()
    if options.color:
        if options.color in ledcolor:
            print("Color " + options.color) 
            print(str(ledcolor[options.color]))
            ledbreath(ledcolor[options.color])
        else:
            print(str(options.color) + " Not found")
    
    #if not options.topic or not options.sub:
    #    print("You need a -t Topic and -s Message")
    #    sys.exit()




def main():
    global options

    (options, args) = get_args()

    #if not checkconnect():
    #    sys.exit()

    if len(sys.argv) == 1:
        #print(str(parser.usage()))
        parser.print_help()
        sys.exit()

    try:
        parseArgs()
    except KeyboardInterrupt:
        print( " \n Thanks for playing\n")
        breath.stop()
        GPIO.cleanup()
        sys.exit()


if __name__ == '__main__':
        main()
        print( "\n\n")





#EOF
