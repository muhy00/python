#!/usr/bin/env python
from netmiko import Netmiko
from getpass import getpass

net_connect = Netmiko(
    "10.50.50.1",
    username="admin",
    password=getpass(),
    device_type="fortinet",
)

print(net_connect.find_prompt())
net_connect.disconnect()
