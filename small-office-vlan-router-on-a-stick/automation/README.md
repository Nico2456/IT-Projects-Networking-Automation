# Networking Automation
Outside of Cisco Packet Tracer, manually populating configs of networking devices are repetitive chores that can be carried out by running automation scripts. Network engineers can moderate configs from a YAML file and push them automatically to a huge amount of devices in no time.

## Download GNS3 VM Simulator
Register an GNS3 account to download from
```python
https://www.gns3.com/
```
This automation sim is a data pipeline of:
```python
 automation.py <-> Netmiko Library <-> Telnet/SSH connection <-> Router R1
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
When prompted to download a virtual machine (VM) in GNS3, follow insturctions to run the GNS3 in a Virtual Environment. Then setup the ports and bind the hosts to a localhost IP like 127.0.0.1, which will become the telnet (IP) address of SSH-enabled network devices in the simulation
![automation setup](automation-gns3sim-setups.png)

## Configure topology and run simulation
The switches used are not SSH-enabled, hence only routers can interact with the automation data pipeline. Router image used is Cisco 3725, which is imported from online sources.
![automation topology](automation-gns3sim-topology.png)

## Run automation codes
Map the telnet address of router R1 in `inventory.yaml`. Via a terminal, run the automation.py script
```python
python3 automation.py
```
