# Network Security AI

AI-driven network attack detection system for SDN networks.

## What it does
This project detects network attacks like port scans and SYN floods on SDN networks using machine learning.

## Tech Stack
- Python
- Mininet
- Open vSwitch
- Scapy
- tcpdump
- scikit-learn (Random Forest)

## How it works
I built a virtual SDN network using Mininet with Open vSwitch on Linux. I captured three types of traffic — normal pings, port scans using nmap, and SYN floods using hping3 — with tcpdump. I extracted features from the pcap files using Scapy and trained a Random Forest model with scikit-learn to classify the traffic.

## Results
- Normal traffic: 100% detection
- Flood attacks: 87% F1-score
- Port scans: 64% F1-score
- Overall accuracy: 82%

## Status
In progress - improving portscan detection
