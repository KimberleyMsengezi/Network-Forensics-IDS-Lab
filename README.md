# 01 - Network Forensics & IDS Lab | Security Onion + Wireshark

![Security Onion](https://img.shields.io/badge/Security%20Onion-2.4-00A651?style=for-the-badge&logo=linux&logoColor=white)
![Suricata](https://img.shields.io/badge/Suricata-IDS-orange?style=for-the-badge)
![Zeek](https://img.shields.io/badge/Zeek-Network%20Analysis-blue?style=for-the-badge)
![Wireshark](https://img.shields.io/badge/Wireshark-Packet%20Analysis-1679A7?style=for-the-badge&logo=wireshark&logoColor=white)
![MITRE ATT&CK](https://img.shields.io/badge/MITRE%20ATT%26CK-v15-red?style=for-the-badge)

## Overview
Deployed a full **Network Security Monitoring (NSM)** and **Intrusion Detection System (IDS)** lab using **Security Onion** (Suricata + Zeek) integrated with **Wireshark** for deep packet inspection. Generated realistic attack traffic (Nmap scans, Hydra brute-force, simulated C2/beaconing), captured/analyzed PCAPs, tuned rules, extracted IOCs with Python, and mapped detections to **MITRE ATT&CK**. Demonstrates core network forensics, alert triage, and IOC handling skills.

**Repository Structure**  
- `/Suricata-Rules` → Custom & tuned signatures  
- `/Zeek-Logs` → Sample extracted logs  
- `/Wireshark-Filters` → Display & analysis filters  
- `/Python-Scripts` → IOC extraction & VirusTotal enrichment  
- `/PCAPs` → Sample capture placeholders  
- `/Diagrams` → Lab topology & data flow  
- `/Reports` → Forensics reports with timelines & IOCs

## Lab Architecture Diagram
```mermaid
graph LR
    A[Kali Attacker VM<br/>• Nmap scans<br/>• Hydra brute-force<br/>• Simulated C2 (e.g. Cobalt Strike beacon)] 
    --> B[Internal Network<br/>(Bridged/Mirrored Traffic)]
    B --> C[Victim VMs<br/>• Ubuntu/Windows targets<br/>• Vulnerable services]
    B --> D[Security Onion Sensor VM<br/>• Suricata IDS/IPS<br/>• Zeek protocol analysis<br/>• Full packet capture]
    D --> E[Wireshark Analysis<br/>• Deep packet inspection<br/>• Protocol dissection<br/>• IOC extraction]
    D --> F[Dashboards<br/>• Kibana/Elastic<br/>• SOC console alerts]
