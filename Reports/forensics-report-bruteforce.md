# Network Forensics Report - Simulated SSH Brute Force Attack

Date: 2026-03-13  
MITRE ATT&CK: T1110.001 - Password Guessing  
Source IP: 192.168.56.101  
Target: 192.168.56.102:22 (SSH)

## Timeline
09:12:34 - First SSH connection attempt  
09:12:35 to 09:13:28 - 47 failed login attempts (Hydra pattern)  
09:13:29 - Zeek notice: high auth failure rate

## Detections
- Suricata alert sid:1000007 (Hydra brute force threshold)  
- Zeek auth.log: multiple SSH failure events

## IOCs
- Source IP: 192.168.56.101  
- User agents / patterns: Hydra-generated SSH banners

## Recommendations
- Block source IP at firewall  
- Enable fail2ban or similar on SSH  
- Escalate to Tier 2 for full compromise check

Analyst: Kimberley (lab simulation)
