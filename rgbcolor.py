#!/usr/bin/env python3

import sys, os

PINFILE = os.path.dirname(__file__) + "/pin.txt"
pins = {}

def setpins():
    # Instead of using ConfigParse
    global pins
    with open(PINFILE, 'r') as f:
        parray = [line.rstrip('\n') for line in f]
        #parray = f.readlines().rstrip('\n')
    for i, key in enumerate(parray):
        if '[rpipin]' in key:
            for p in range(i+1):
                parray.pop(0)
            
            for i in range(4):
                color,pin = parray[i].split('=')
                pins[color.strip()] = int(pin)

def rgb_to_hex(rgb):
    return '%02x%02x%02x' % rgb
    #rgb_to_hex((255, 255, 195))

def main(color):
    if '#' in color:
        #we have hex
        # we have a hex color
        color = color.lstrip('#')
        print('RGB =', tuple(int(color[i:i+2], 16) for i in (0, 2, 4)))
        RGB = tuple(int(color[i:i+2], 16) for i in (0, 2, 4))
        r,g,b = RGB
        # mapping 0-255 to 0.0 to 1
        
        print(string)
        f = open('/dev/pi-blaster', 'w')
        f.write(string)
    if 'rgb' in color:
        #we have 3 values
        rgb = color[color.find("(")+1:color.find(")")]
        RGB = (int(rgb.split(',')[0]),int(rgb.split(',')[1]),int(rgb.split(',')[2]))
        print('HEX ' + str(rgb_to_hex(RGB)))

    pin = list(pins.values())
    rgbvar = [x / 255.0 for x in RGB]
    print(rgbvar)
    string = "%s=%s\n%s=%s\n%s=%s\n" % (str(pin[0]),str(rgbvar[0]),str(pin[1]),str(rgbvar[1]),str(pin[2]),str(rgbvar[2]))
    f = open('/dev/pi-blaster', 'w')
    f.write(string)







if __name__ == "__main__":
    if len(sys.argv) < 2:
        exit("need an argument")
    setpins()
    main(sys.argv[1])






#EOF
