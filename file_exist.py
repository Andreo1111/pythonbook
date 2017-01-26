from os.path import isfile
from os.path import isdir
import subprocess
import sys
from filecmp import cmpfiles
import tarfile


sources = ["/u01/app/oracle/",
           "/home/oracle/",
           "/etc/oracle/",
           "/etc/oratab",
           "/etc/oraInst.loc",
           "/usr/local/bin/dbhome",
           "/usr/local/bin/coraenv",
           "/usr/local/bin/oraenv",
           "/etc/init.d/gcstartup",
           "/etc/init.d/lockgcstartup",
           "/etc/init.d/unlockgcstartup",
           "/etc/rc*.d/*gcstartup*",
           "/etc/init.d/init.ohasd",
           "/etc/init.d/ohasd",
           "/etc/rc*.d/*ohasd*",
           "/etc/init/oracle-ohasd.conf",
           "/etc/systemd/system/oracle-ohasd.service"]
destination = "/tmp/COPY/"
rsync = "rsync"
arguments = "-avz"

def check_dirs(sources):
    if isdir(sources):
        print("Ok :",sources )
    else:
        print("Directory  NOT exist :-(: ",sources)

def check_files(sources):
    if isfile(sources):
        print("Ok :",sources )
    else:
        print("File NOT exist :-(: ",sources)

def bak_files(sources):
    if isfile(sources):
       subprocess.call(("%s %s %s %s " % (rsync, arguments, sources, destination)),shell=True)    
for x in (sources):
    check_dirs(x) and  check_files(x)

question = input("Get are you backup oracle files?(Y/N) :")
if  question == "Y" or "y" :
    tar = tarfile.open("reinstall.tar","w")
    for i in (sources):
        print(i)
        tar.add(i)
    tar.close()
elif question == "N" or "n":
    print("See you later my friend") 

   
          
