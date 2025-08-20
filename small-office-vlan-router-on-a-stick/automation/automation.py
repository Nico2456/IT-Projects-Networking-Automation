"""
Router (R1) Automation Demo with Netmiko
Purpose: Demonstration of automated configuration and verification on a Cisco router (R1).
"""

import yaml
from netmiko import ConnectHandler

# Load inventory
with open("inventory.yaml") as f:
    inventory = yaml.safe_load(f)

# Get R1 device info
r1 = inventory["devices"]["R1"]

# Connect to R1
print(f"Connecting to {r1['host']}:{r1['port']} ...")
connection = ConnectHandler(**r1)

# Commands for R1 basic IP setup
commands = [
    "interface FastEthernet0/0",       # adjust to your actual R1 interface in GNS3
    "ip address 192.168.10.1 255.255.255.0",
    "no shutdown",
]

print("Sending configuration...")
output = connection.send_config_set(commands)
print(output)

connection.save_config()
connection.disconnect()
print("R1 setup complete ✅")
