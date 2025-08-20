## Networking Automation
Manually populate configs of networking devices are repetitive jobs that can be carried out by running automation scripts. Network engineers can moderate configs from a YAML file and push them automatically to a huge amount of devices in no time.

## Download GNS3 VM Simulator
Register an GNS3 account to download from
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
## Setup GNS3 VM
![automation setup](automation-gns3sim-setups.png)

## Configure topology and run simulation
![automation topology](automation-gns3sim-topology.png)

## Run automation codes
