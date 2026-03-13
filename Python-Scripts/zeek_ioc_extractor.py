# zeek_ioc_extractor.py - Basic IOC extraction from Zeek conn.log & http.log
# Usage: python zeek_ioc_extractor.py conn.log http.log

import sys
import pandas as pd

if len(sys.argv) < 2:
    print("Usage: python script.py <conn.log> [http.log]")
    sys.exit(1)

# Read Zeek conn.log (tab-separated, skip comments)
try:
    df_conn = pd.read_csv(sys.argv[1], sep='\t', comment='#', low_memory=False)
    high_traffic_ips = df_conn[df_conn['orig_bytes'] > 5000000]['id.orig_h'].unique()
    print("\nSuspicious high outbound traffic IPs (possible exfil):")
    for ip in high_traffic_ips:
        print(f" - {ip}")
except Exception as e:
    print(f"Error reading conn.log: {e}")

# Optional: VirusTotal placeholder (add your API key in production)
# import requests
# for ip in high_traffic_ips:
#     vt_url = f"https://www.virustotal.com/api/v3/ip_addresses/{ip}"
#     headers = {"x-apikey": "YOUR_VT_API_KEY_HERE"}
#     response = requests.get(vt_url, headers=headers)
#     if response.status_code == 200:
#         print(f"{ip} VT result: {response.json()}")
