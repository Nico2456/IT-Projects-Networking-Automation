# Office VLAN Topology with Router-on-a-Stick + DHCP

This project demonstrates **enterprise-style VLAN segmentation with inter-VLAN routing** and centralized DHCP, simulated using **Cisco Packet Tracer**.

---

## 🖼️ Network Topology
```
|Internet | R1 --- Gig0/1 | SW1 --- Fa0/1 | HR-PC1
|         |               |         Fa0/2 | HR-PC2
|         |               |         Fa0/3 | IT-PC1
|         |               |         Fa0/4 | IT-PC2
|         |               |         Fa0/24| SW2    --- Fa0/1 | Finance-PC1
|         |               |               |        --- Fa0/2 | Finance-PC2
```
- **R1** – Router-on-a-stick (handles inter-VLAN routing + DHCP)
- **SW1** – Core switch for HR + IT VLANs
- **SW2** – Access switch for Finance VLAN

| Device       | Interface         | Connected To       | Port (DHCP)  | VLAN       |
|--------------|-------------------|--------------------|--------------|------------|
| Internet     | -                 | R1                 | -            | -          |
| R1           | Gig0/1| SW1                | -            | -          |
| R1           | Gig0/1| SW2                | -            | -          |
| SW1          | Fa0/1   | HR-PC1             | -            | VLAN 10 (HR) |
| SW1          | Fa0/2   | HR-PC2             | -            | VLAN 10 (HR) |
| SW1          | Fa0/3   | IT-PC1             | -            | VLAN 20 (IT) |
| SW1          | Fa0/4   | IT-PC2             | -            | VLAN 20 (IT) |
| SW2          | Fa0/1   | Finance-PC1        | -            | VLAN 30 (Finance) |
| SW2          | Fas0/2   | Finance-PC2        | -            | VLAN 30 (Finance) |
---

## ⚙️ VLANs
| VLAN ID | Department | Subnet            | Default GW    |
|---------|------------|------------------|---------------|
| 10      | HR         | 192.168.10.0/24  | 192.168.10.1  |
| 20      | IT         | 192.168.20.0/24  | 192.168.20.1  |
| 30      | Finance    | 192.168.30.0/24  | 192.168.30.1  |

---

## 🚀 Features
- **Router-on-a-Stick** for inter-VLAN routing
- **DHCP** for each VLAN
- **Trunk Links** between router & switches
- **Access Ports** per VLAN
- Portfolio-ready configs and verification steps

---

## 📝 How to Run
1. Open `office_vlan_topology.pkt` in Cisco Packet Tracer
2. Apply configs from `configs/` folder
3. Run verification commands and paste outputs into `verification/`
4. Test connectivity with `ping` from PCs

---

## ✅ Verification Checklist
- Router sub-interfaces UP: `show ip interface brief`
- VLANs configured: `show vlan brief`
- Trunks UP: `show interfaces trunk`
- PCs received IPs via DHCP
- Successful ping tests across VLANs

---

## 🔮 Notes
This topology mimics **real-world enterprise networks** where VLAN segmentation is used for security and performance, with centralized DHCP for management efficiency.

---

👨‍💻 Author: *Your Name Here*  
📌 Repository: [GitHub link once uploaded]
