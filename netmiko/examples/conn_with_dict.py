#!/usr/bin/env python
from netmiko import ConnectHandler
from getpass import getpass

cisco1 = {
    "host": "10.50.50.1",
    "username": "admin",
    "password": getpass(),
    "device_type": "fortinet",
}

net_connect = ConnectHandler(**cisco1)
output = net_connect.send_command('get sys arp')
print(output)
print(net_connect.find_prompt())
net_connect.disconnect()
