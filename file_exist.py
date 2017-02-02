from os.path import isfile
from os.path import isdir
#from subprocess import PIPE,Popen,STDOUT
import sys
import tarfile
import os
import subprocess
import re 


sources = [#"/u01",
#/u01/app/oracle/",#
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
           "/etc/systemd/system/oracle-ohasd.service",
           "/home/oracle/.ssh/",
           "/home/oracle/.bashrc",
           "/home/oracle/.bash_profile"]



list_files = open('/tmp/test_sp','r')
for i in (list_files):
      global symlink
      symlink =re.split(' ',i)
      print(symlink)

'''
def check_df(sources):
    if isdir(sources):
        return 1
        print()          
    elif  isfile(sources):
        return 1
        print()         
    else:
        print("Object not exist!", sources)
'''
def glob_quest():
    global path 
    path = raw_input('Where store backup files ? (for example: /tmp/backup ):')
   
question1 = raw_input("You want to create  backup ?(Y/N) :")
print(question1)

if question1 == "Y":
    
   glob_quest()
   tar = tarfile.open(path,"w")
   #for i in (sources):
   #   if check_df(i):
   #      print(i)         
   #      tar.add(i)
   for x in (symlink):
      # if check_df(x):
          tar.add(x) 
   tar.close()
#   print(" Backup is success in :", path )  

  
else:
    print("Good bye !!!")  
     
   # file_list = tarfile.open(/var/log/backup)
 #   file_list.extractall(path="/")
 #   file_list.close()
 
