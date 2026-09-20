from scapy.all import rdpcap, IP
import pandas as pd

packets = rdpcap('/tmp/capture.pcap')

rows = []
for pkt in packets:
    if IP in pkt:
        rows.append({
            'src_ip': pkt[IP].src,
            'dst_ip': pkt[IP].dst,
            'protocol': pkt[IP].proto,
            'length': len(pkt)
        })

df = pd.DataFrame(rows)
print(df)
print()
print(f"Total IP packets: {len(df)}")
