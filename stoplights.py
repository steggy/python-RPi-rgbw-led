#! /usr/bin/python3

import sys
import time

CHECKVERSION = "0.1.0"


def off():
    with open('/dev/pi-blaster', 'w') as out_file:
        out_file.write('22=0\n')
        out_file.write('23=0\n')
        out_file.write('24=0\n')


if __name__ == '__main__':
        off()
        sys.exit()




#EOF
