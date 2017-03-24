#!/usr/bin/env python
# -*- coding: utf-8 -*-

#only  python-2.7

import os
import subprocess
    

print '=' * 40
print '=' * 10 + '     STATUS NIC     ' + '=' * 10
print '=' * 40


num = 'n/n'
ifname = 'interface name'
ifspeed = 'speed'
ifstatus = 'status'

n = 0



tab_len1 ='{:^8s}{:^14s}{:^10s}{:^8s}'.format(num,ifname,ifspeed,ifstatus)                     # create table header
row = '-' *len(tab_len1)
print
print(tab_len1)
print(row)


proc = subprocess.check_output('ls  /sys/class/net/', shell=True)        # interface name

    
a = proc.splitlines()

for i in a:
    if i != 'lo' and len(i) < 10:
        
        proc1 = (subprocess.check_output('cat  /sys/class/net/'+i+'/speed', shell=True)).splitlines()    # s
        proc2 = (subprocess.check_output('cat  /sys/class/net/'+i+'/operstate', shell=True)).splitlines()
        
        n +=1
        tab_len ='{:^8d}{:^14s}{:^10s}{:^8s}'.format(n,i,proc1[0],proc2[0])
        print tab_len        
        
         
        


 








      
