#! /usr/bin/python3

import subprocess, time, sys, os



if __name__ == "__main__":
    run_file = os.path.dirname(__file__) + "/runfile.txt"
    if len(sys.argv) < 2:
        exit("need an argument")
    to_run = sys.argv[1]
    sys.argv.pop(0)
    print(sys.argv[0])
    #sys.exit()
    #proc = subprocess.Popen([to_run,sys.argv[2],sys.argv[3]])
    with open(run_file) as f:
        lines = f.read().splitlines()
    for i in lines:
        if str(sys.argv[0]) in i:
            sys.exit()    
    proc = subprocess.Popen(sys.argv, start_new_session=True)
    print ("start process with pid %s" % proc.pid)
    file1 = open(run_file,"a")
    file1.write(str(proc.pid) + ',' + to_run + '\n')
    #file1.writelines(L)
    file1.close() #to change file access modes
    #print(proc.pid)
    # Removed sleep to see process
    #time.sleep(50)
    ## kill after 50 seconds if process didn't finish
    #if proc.poll() is None:
    #    print ("Killing process %s with pid %s " % (to_run,proc.pid))
    #    proc.kill()




#EOF
