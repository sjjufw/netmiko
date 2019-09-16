#!C:\Ling\Software\Python_Script\netmiko\Scripts python
from __future__ import print_function, unicode_literals

# Netmiko is the same as ConnectHandler
from netmiko import Netmiko
from getpass import getpass
import re

with open('ip_list.txt') as f:
    devices_list = f.read().splitlines()
print (devices_list)

for device in devices_list:
   my_device = {
       "host": device,
       "username": "admin",
       #"password": getpass(),
       "password": 'cisco123',
       "device_type": "cisco_ios",
       'session_log': '%s.txt' % device,
       "secret" : "cisco123",
   }
   net_connect = Netmiko(**my_device)
   # Ensure in enable mode
   net_connect.enable()
   output = net_connect.send_command ('do show port-sec')
   print (output)
   str = output.split('\n')
   for x in str:
       a = x.split()
       if a[2] == "0":
           print (a)
   # Close session
   net_connect.disconnect()

## Output

##net_connect.send_config_from_file("config.txt")
#sn = net_connect.send_command ('show ip int brie').split('\n')
#for x in sn:
#	a = x.split()
#	print ('%-11s: %s' % ('interface',a[0]))
#	print ('%-11s: %s' % ('ip-address',a[1]))
#	print ('%-11s: %s' % ('status',a[4]))
#	print ('%-11s: %s' % ('protocol',a[5]))
#	print ('_'*30)
#ntp = net_connect.send_command ('sh run | sec ntp')



re.match ('\s+(\w.*\d)\s+(\d)\s+(\d)\s+(\d)\s+Restrict',output)
