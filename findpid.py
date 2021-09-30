#! /usr/bin/python3

from subprocess import check_output
import sys, re, os, signal
import subprocess


def bashit(command):
    """ Shell out and run the bash cli command """
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=None, shell=True)
    output = process.communicate()[0]
    return output

def get_pid(name):
    cmd = 'ps' #-ef | grep ' + name + ' | grep -v grep'
    mypid = subprocess.Popen([cmd,'-ef','| grep ' + name + ' | grep -v grep'])
    #return check_output(["pidof",name])
    return mypid


if len(sys.argv) < 2:
    exit("Need an ARG")
PS = '/usr/bin/ps'
cmd = PS + ' -ef | grep ' + str(sys.argv[1]) + ' | grep -v grep | grep -v findpid.py' 
result = bashit(cmd).decode('UTF-8')
if len(result) > 2:
    print(result)
    pidlines = result.splitlines()
    print('First line:\n' + str(pidlines[0]))
    csv = re.sub("\s+", ",", pidlines[0].strip())
    print(csv)
    for i in range(0, len(pidlines)):
        thepid = re.sub("\s+", ",", pidlines[i].strip()).split(',')[1]
        print("The PID " + str(thepid))
        #if i == 0:
        os.kill(int(thepid), signal.SIGTERM) #or signal.SIGKILL 
        bashit(os.path.dirname(__file__) + '/stoplights.py')





#EOF
