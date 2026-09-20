from scapy.all import rdpcap, IP
import pandas as pd

def load_pcap(filepath, label):
    packets = rdpcap(filepath)
    rows = []
    for pkt in packets:
        if IP in pkt:
            rows.append({
                'src_ip': pkt[IP].src,
                'dst_ip': pkt[IP].dst,
                'protocol': pkt[IP].proto,
                'length': len(pkt),
                'label': label
            })
    return rows

normal_rows = load_pcap('data/capture.pcap', 'normal')
portscan_rows = load_pcap('data/portscan.pcap', 'portscan')
flood_rows = load_pcap('data/flood.pcap', 'flood')

all_rows = normal_rows + portscan_rows + flood_rows
df = pd.DataFrame(all_rows)

df.to_csv('data/dataset.csv', index=False)

print(df['label'].value_counts())
print()
print(f"Total rows saved to data/dataset.csv: {len(df)}")
