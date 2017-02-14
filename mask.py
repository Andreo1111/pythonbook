from os.path import isfile
from os.path import isdir
import os
import glob
import tarfile

question1 = raw_input('\033[1;36mYou want to create  backup file(B)  or extract backup file(E)?:\033[0;m'"\033[1;31m(B/E)\033[0;m"'\033[1;36m:\033[0;m')

sources_mask = glob.glob("/etc/rc*.d/*ohasd*")
sources_mask1 = glob.glob("/etc/rc*.d/*gcstartup*")
sources_mask2 = [
          # "/u01",
          #"/u01/app/oracle/",
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
          # "/etc/rc*.d/*gcstartup*",
           "/etc/init.d/init.ohasd",
           "/etc/init.d/ohasd",
          # "/etc/rc*.d/*ohasd*",
           "/etc/init/oracle-ohasd.conf",
           "/etc/systemd/system/oracle-ohasd.service",
           "/home/oracle/.ssh/",
           "/home/oracle/.bashrc",
           "/home/oracle/.bash_profile"]

def check_df(sources):
    if isdir(sources):
        return 1
        print()
    elif  isfile(sources):
        return 1
        print()
    else:
        print(" Error! Object not exist!", sources)


if question1 == "B":
    path = raw_input('\033[1;36mWhere store backup files ?\033[0;m' "\033[1;31m(for example: /tmp/backup.tar )\033[0;m" '\033[1;36m :\033[0;m').strip()
    tar = tarfile.open(path,"w")
    for i in (sources_mask2):
        if check_df(i):
            tar.add(i)
    for i in (sources_mask):
        if check_df(i):
            tar.add(i)
    for i in (sources_mask1):
        if check_df(i):
            tar.add(i) 
    tar.close()
    print'\033[1;36mBackup is success!!! in:\033[0;m',path
elif question1 == "E":
    obj = raw_input('\033[1;36mPlease input name of backup file:\033[0;m').strip()
    file_list = tarfile.open(obj)
    file_list.extractall(path="/")
    file_list.close() 
    oracle_ohasd_service = open("/etc/systemd/system/oracle-ohasd.service","w")
    oracle_ohasd_service.write(
'''
[Unit]
Description=ohasd daemon

[Service]
ExecStart=/etc/init.d/init.ohasd run > /dev/null 2>&;1

[Install]
WantedBy=multi-user.targe
'''
)
    oracle_ohasd_service.close()
    print("OK")
else:
    print("Good bye!!!")

