Example 4.1. Example ifcfg-bond0 Interface Configuration File
An example of a channel bonding interface. 

DEVICE=bond0
NAME=bond0
TYPE=Bond
BONDING_MASTER=yes
IPADDR=192.168.1.1
PREFIX=24
ONBOOT=yes
BOOTPROTO=none
BONDING_OPTS="bonding parameters separated by spaces"







Example 4.2. Example Slave Interface Configuration File
For example, if two Ethernet interfaces are being channel bonded, eth0 and eth1, they can both look like the following example:

DEVICE=ethN
NAME=bond0-slave
TYPE=Ethernet
BOOTPROTO=none
ONBOOT=yes
MASTER=bond0
SLAVE=yes
