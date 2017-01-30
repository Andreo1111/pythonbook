from os.path import isfile
from os.path import isdir
import sys
import tarfile
import os

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

def check_df(sources):
    if isdir(sources):
        return 1         
    elif  isfile(sources):
        return 1         
    else:
         print("Object NOT exist !!! ",sources) 

def glob_quest():
    global path 
    path = input('Where store backup files ? (for example: /tmp/backup ):')
    log = open('/var/log/backup','w')
    log.write(path)

question1 = input("Backup or extract files ?(B/E) :")


#question2 = input("Where store backup files ? :")
#question3 = input("Recovery oracle files?(Y/N) :")


if  question1 == "B":
    glob_quest()
    tar = tarfile.open(path,"w")
    for i in (sources):
        if check_df(i):        
           tar.add(i)
    tar.close()
    print(" Backup is success!!! ")  
    
elif  question1 == "E":
     
    file_list = tarfile.open(/var/log/backup)
    file_list.extractall(path="/")
    file_list.close()
 
#a = glob_quest()
print(path)          
