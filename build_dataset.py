from scapy.all import rdpcap, IP, TCP, UDP
import pandas as pd

def load_pcap(filepath, label):
    packets = rdpcap(filepath)
    rows = []
    for pkt in packets:
        if IP in pkt:
            row = {
                'src_ip': pkt[IP].src,
                'dst_ip': pkt[IP].dst,
                'protocol': pkt[IP].proto,
                'length': len(pkt),
                'ttl': pkt[IP].ttl,
                'label': label
            }

            if TCP in pkt:
                row['src_port'] = pkt[TCP].sport
                row['dst_port'] = pkt[TCP].dport
                row['tcp_flags'] = int(pkt[TCP].flags)
            elif UDP in pkt:
                row['src_port'] = pkt[UDP].sport
                row['dst_port'] = pkt[UDP].dport
                row['tcp_flags'] = 0
            else:
                row['src_port'] = 0
                row['dst_port'] = 0
                row['tcp_flags'] = 0

            rows.append(row)
    return rows

normal_rows = load_pcap('data/capture.pcap', 'normal')
portscan_rows = load_pcap('data/portscan.pcap', 'portscan')
flood_rows = load_pcap('data/flood.pcap', 'flood')

all_rows = normal_rows + portscan_rows + flood_rows
df = pd.DataFrame(all_rows)

df.to_csv('data/dataset.csv', index=False)

print(df['label'].value_counts())
print(f"\nColumns: {df.columns.tolist()}")
print(f"Total rows saved: {len(df)}")
