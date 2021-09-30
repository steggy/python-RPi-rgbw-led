#! /usr/bin/python3

import subprocess, time, sys, os, signal

def bashit(command):
    """ Shell out and run the bash cli command """
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=None, shell=True)
    output = process.communicate()[0]
    return output

def main():    
    if len(sys.argv) < 2:
        exit("need an argument")
    
    holdlines = []
    # look in the pid track file for the proccess
    
    run_file = os.path.dirname(__file__) + "/runfile.txt"
    
    to_run = sys.argv[1]
    sys.argv.pop(0)
    print(sys.argv[0])
    proc = sys.argv[0]

    # Read file to list
    with open(run_file) as f:
        lines = f.read().splitlines()
    for i in lines:
        if proc in i:
            #print("Found proc " + str(proc) + " " + str(i.split(',')[0]))
            try:
                os.kill(int(i.split(',')[0]), signal.SIGTERM)
            except:
                pass
        else:
            holdlines.append(i)     
    #print("new file")
    #print(holdlines)
    # write list to file
    textfile = open(run_file, "w")
    for element in holdlines:
        textfile.write(element + "\n")
    textfile.close()
    bashit(os.path.dirname(__file__) + '/stoplights.py')

    


if __name__ == "__main__":
    main()

#EOF
