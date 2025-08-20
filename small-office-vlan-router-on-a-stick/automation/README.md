## Download GNS3 VM Simulator
Register an GNS3 account to download
```python
https://www.gns3.com/
```
This automation sim is a data pipeline of:
```python
 automation.py <-> netmiko library <-> Telnet/SSH connection <-> Router R1
```
```mermaid
graph TD
    A[**automation.py**:<br>Device info, host port, username pwd, command list] -->|Uses| B[**Netmiko Library**:<br>SSH/Telnet handler, send_config_set, Receive output]
    B -->|Establishes| C[**Telnet/SSH Connection**:<br>127.0.0.1:5000 GNS3]
    C -->|Sends commands to| D[**Router R1**:<br>Executes commands, <br>Configures interfaces,<br> Returns output]
    D -->|Returns output| C
    C -->|Relays output| B
    B -->|Processes output| A
```

