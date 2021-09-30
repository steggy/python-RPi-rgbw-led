#! /usr/bin/python3

import socket, sys, subprocess, os

#socket.setdefaulttimeout(150)
host = ''               
port = 65432
socksize = 2048

PINFILE = os.path.dirname(__file__) + "/pin.txt"
run_file = os.path.dirname(__file__) + "/runfile.txt"

#pins = []
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


def bashit(command):
    """ Shell out and run the bash cli command """
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=None, shell=True)
    output = process.communicate()[0]
    #return output


def startpid(mess):
    global pins
    #If request is on off or level - 
    #   There is no need to start a routine
    #Else for things like fade, strobe or Christmas - we need a routine
    print(mess)
    if '*' in mess:
        item = mess.split('*')
    
    if 'fade' in item[0]:
        if item[1] == 'on':
            cmd = os.path.dirname(__file__) + "/startpid.py" 
            carg = os.path.dirname(__file__) + "/rgbfade.py" 
            subprocess.Popen([cmd,carg], start_new_session=True)
        if item[1] == 'off':
            cmd = os.path.dirname(__file__) + "/stoppid.py" 
            carg = os.path.dirname(__file__) + "/rgbfade.py" 
            subprocess.Popen([cmd,carg], start_new_session=True)
    if item[1] == 'reset':
            file1 = open(run_file,"w")
            file1.write("")
            file1.close()
            bashit(os.path.dirname(__file__) + '/stoplights.py')
    if 'switch' in item[0]:
            pin = list(pins.values())
            if 'on' in item[1]:
                f = open('/dev/pi-blaster', 'w')
                f.write('%d=%s\n'%(pin[3], '1'))
            else:
                f = open('/dev/pi-blaster', 'w')
                f.write('%d=%s\n'%(pin[3], '0'))
    if 'level' in item[0]:
            pin = list(pins.values())
            if 'color' in item[0]:
                pass
            else:
                val = float(item[1])
                if val > 10 : val = 10
                val = val / 10
                f = open('/dev/pi-blaster', 'w')
                f.write('%d=%s\n'%(pin[3], val)) 
    if 'color' in item[0]:
            cmd = os.path.dirname(__file__) + "/rgbcolor.py"
            subprocess.Popen([cmd,item[1]], start_new_session=True)
            
            # convert dict list:
            # get keys keys = list(d1.keys())
            # get values values = list(d.values())
            # get pairs values = list(d.items())
            
def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    print("Server started on port: %s" % port)
    s.listen(1)


    while True:
        print("Now listening...\n")
        conn, addr = s.accept()
        print ('New connection from %s:%d' % (addr[0], addr[1]))
        data = conn.recv(socksize)
        if not data:
            break
        elif data == 'killsrv':
            conn.close()
            sys.exit()
        else:
            print(data.decode('UTF-8'))
            startpid(data.decode('UTF-8'))
            conn.sendall(data)


if __name__ == "__main__":
    setpins()
    main()

#EOF



