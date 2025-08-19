from netmiko import ConnectHandler

devices = [
    {
        "device_type":"cisco_ios",
        "host":"10.0.0.101",
        "username":"admin",
        "password":"cisco",
        "secret":"cisco"
    },
    {
        "device_type":"cisco_ios",
        "host":"10.0.0.102",
        "username":"admin",
        "password":"cisco",
        "secret":"cisco"
    },
    {
        "device_type":"cisco_ios",
        "host":"10.0.0.103",
        "username":"admin",
        "password":"cisco",
        "secret":"cisco"
    }
]

configs = {
    "r1": [
        "hostname R1",
        "interface GigabitEthernet0/0.10",
        " encapsulation dot1Q 10",
        " ip address 192.168.10.1 255.255.255.0",
        # ... add rest
    ],
    "sw1": [
        "hostname SW1",
        "vlan 10",
        " name HR",
        # ...
    ],
    "sw2":[
        "hostname SW2",
        # ...
    ]
}

for device, cfg in zip(devices, configs.values()):
    net_connect = ConnectHandler(**device)
    net_connect.enable()
    output = net_connect.send_config_set(cfg)
    print(f"== {device['host']} config applied ==\n", output)
    net_connect.disconnect()
