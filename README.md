# 01 - Network Forensics & IDS Lab | Security Onion + Wireshark

![Security Onion](https://img.shields.io/badge/Security%20Onion-2.4-00A651?style=for-the-badge&logo=linux&logoColor=white)
![Suricata](https://img.shields.io/badge/Suricata-7.0.7-orange?style=for-the-badge)
![Zeek](https://img.shields.io/badge/Zeek-6.0.8-blue?style=for-the-badge)
![Wireshark](https://img.shields.io/badge/Wireshark-4.4.1-1679A7?style=for-the-badge&logo=wireshark&logoColor=white)
![MITRE ATT&CK](https://img.shields.io/badge/MITRE%20ATT%26CK-v15-red?style=for-the-badge)

## Overview
Built a production-grade **Network Security Monitoring (NSM)** and **Intrusion Detection System (IDS)** laboratory environment using **Security Onion 2.4** (Suricata 7.0.7 + Zeek 6.0.8) combined with **Wireshark 4.4.1** for advanced packet-level forensics.  

The lab simulates enterprise network traffic patterns and realistic adversary behaviors using a Kali Linux attacker VM targeting vulnerable Ubuntu/Windows victims. Generated malicious traffic across multiple attack phases (reconnaissance, initial access, execution, persistence, lateral movement, C2, exfiltration), captured full packet data, tuned detection rules, performed deep packet inspection, extracted and enriched IOCs via scripting, and documented forensic findings with MITRE ATT&CK mappings.

## Lab Architecture Diagram
```mermaid
graph LR
    A["Kali Attacker VM (Nmap, Hydra, Metasploit, custom C2)"] 
    --> B["Internal Network (bridged + mirrored SPAN port)"]
    B --> C["Victim VMs (Ubuntu 22.04 + Windows 10/11)"]
    B --> D["Security Onion Sensor VM (Suricata IPS + Zeek + Stenographer full PCAP)"]
    D --> E["Wireshark Workstation (deep inspection + Lua dissectors)"]
    D --> F["Kibana / Security Onion Console (alerts + dashboards)"]
