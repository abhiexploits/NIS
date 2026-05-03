#!/bin/bash

echo "[*] Setting up Network Intelligence Suite"

# Update packages
pkg update -y 2>/dev/null || sudo apt update -y

# Install Python and pip
pkg install python -y 2>/dev/null || sudo apt install python3 python3-pip -y

# Install required packages
pip install scapy requests whois dnspython

# Install system tools
pkg install nmap arp-scan tcpdump -y 2>/dev/null || sudo apt install nmap arp-scan tcpdump -y

# Create directories
mkdir -p output wordlists

# Create wordlists
echo "21,22,23,25,53,80,110,111,135,139,143,443,445,993,995,1723,3306,3389,5432,5900,6379,8080,27017" > wordlists/common_ports.txt

echo "admin,root,password,123456,toor,abc123" > wordlists/weak_passwords.txt

# Make main script executable
chmod +x nis.py

echo "[+] Setup complete!"
echo "[*] Run: python nis.py"
