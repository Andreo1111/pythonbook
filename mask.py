from os.path import isfile
from os.path import isdir
import glob
import tarfile

question1 = raw_input("You want to create  backup ?(Y/N) :")

sources_mask = glob.glob("/etc/rc*.d/*net*")
print(sources_mask) 
sources = ["/u01",
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
          # "/etc/rc*.d/*ohasd*",
           "/etc/init/oracle-ohasd.conf",
           "/etc/systemd/system/oracle-ohasd.service",
           "/home/oracle/.ssh/",
           "/home/oracle/.bashrc",
           "/home/oracle/.bash_profile"]
print(sources)
def check_df(sources):
    if isdir(sources):
        return 1
        print()
    elif  isfile(sources):
        return 1
        print()
    else:
        print("Object not exist!", sources)


if question1 == "Y":
    path = raw_input('Where store backup files ? (for example: /tmp/backup ):')
    tar = tarfile.open(path,"w")
    for i in (sources):
        if check_df(i):
            tar.add(i)
    for i in (sources_mask):
        tar.add(i)
    tar.close()
    print("Backup is success!!! in: ",path)
else:
    print("Good bye!!!")

