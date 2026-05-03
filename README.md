
# 🔍 Network Intelligence Suite (NIS) v1.0

## Developed by Abhishek

```

╔═══════════════════════════════════════════════════════════════════╗
║                                                                   ║
║     NETWORK INTELLIGENCE SUITE - Professional Security Toolkit    ║
║                                                                   ║
║     For Authorized Security Testing & Educational Purposes Only   ║
║                                                                   ║
╚═══════════════════════════════════════════════════════════════════╝

```

---

## 📌 What is NIS?

Network Intelligence Suite (NIS) is a comprehensive network security toolkit that helps security professionals and ethical hackers perform network reconnaissance, vulnerability assessment, and traffic analysis.

**Use cases:**
- Internal network audits
- Penetration testing
- Security assessments
- Educational learning
- CTF competitions

---

## ✨ Features

| Module | Function | Status |
|--------|----------|--------|
| Network Scanner | Discover all active devices on network | ✅ |
| Port Scanner | Identify open ports on target | ✅ |
| Service Detector | Fingerprint running services | ✅ |
| OS Fingerprinting | Detect operating system | ✅ |
| Vulnerability Checker | Find security weaknesses | ✅ |
| Packet Monitor | Capture and analyze network traffic | ✅ |
| Report Generation | Export results to JSON/HTML | ✅ |

---

## 🚀 Installation

### Termux (Android)

```bash
pkg update && pkg upgrade -y
pkg install python git -y
git clone https://github.com/abhiexploits/NIS.git
cd NIS
chmod +x setup.sh
./setup.sh
python nis.py
```

### Linux (Ubuntu/Debian/Kali)

```bash
sudo apt update
sudo apt install python3 python3-pip git -y
git clone https://github.com/abhiexploits/NIS.git
cd NIS
chmod +x setup.sh
./setup.sh
python3 nis.py
```

#### Manual Installation

```bash
pip install scapy requests whois dnspython
apt install nmap arp-scan tcpdump
mkdir -p output wordlists
```

---

#### 📖 Usage Guide

Start the Tool

```bash
python nis.py
```

## Main Menu

```
┌─────────────────────────────────────────────────────────────┐
│                        MAIN MENU                            │
├─────────────────────────────────────────────────────────────┤
│  [1] Network Scanner - Find all devices                     │
│  [2] Port Scanner - Scan specific target                    │
│  [3] Service Detector - Identify services                   │
│  [4] OS Fingerprinting - Detect operating system            │
│  [5] Vulnerability Check - Find weak spots                  │
│  [6] Packet Monitor - Capture network traffic               │
│  [7] Full Scan - Run all modules on target                  │
│  [8] Generate Report - Save results to file                 │
│  [9] View Last Report                                       │
│  [0] Exit                                                   │
└─────────────────────────────────────────────────────────────┘
```

###### Quick Examples

1. Network Scan

```bash
nis@tool:~$ 1
Enter network (e.g., 192.168.1.0/24): 192.168.1.0/24
[+] Found 12 active devices
    192.168.1.1 - aa:bb:cc:dd:ee:ff - Router
    192.168.1.100 - 11:22:33:44:55:66 - Laptop
    192.168.1.101 - 77:88:99:aa:bb:cc - Phone
```

2. Port Scan

```bash
nis@tool:~$ 2
Enter target IP: 192.168.1.100
Enter port range (default 1-1000): 1-1000
[+] Found 5 open ports
    Port 22 - OPEN (SSH)
    Port 80 - OPEN (HTTP)
    Port 443 - OPEN (HTTPS)
    Port 3306 - OPEN (MySQL)
    Port 8080 - OPEN (HTTP-Alt)
```

3. Full Scan

```bash
nis@tool:~$ 7
Enter target IP: 192.168.1.100
Enter your network: 192.168.1.0/24

[*] Running Full Intelligence Scan
[*] Scanning ports...
[*] Identifying OS...
[*] Checking vulnerabilities...

[+] Full scan completed
    Open ports: 5
    Services identified: 5
    Vulnerabilities: 2
```

---

###### 📊 Output Format

JSON Report

```json
{
  "timestamp": "2026-05-03T10:30:00",
  "tool": "Network Intelligence Suite (NIS)",
  "author": "Abhishek",
  "results": {
    "open_ports": [22, 80, 443, 3306],
    "services": {
      "22": "SSH",
      "80": "HTTP",
      "443": "HTTPS",
      "3306": "MySQL"
    },
    "os": "Linux",
    "vulnerabilities": [...]
  }
}
```



##### 📁 Project Structure

```
NIS/
├── nis.py                 # Main controller
├── setup.sh               # Installation script
├── requirements.txt       # Python dependencies
├── README.md              # Documentation
├── modules/
│   ├── __init__.py
│   ├── network_scanner.py
│   ├── port_scanner.py
│   ├── service_detector.py
│   ├── os_fingerprint.py
│   ├── vuln_checker.py
│   ├── packet_monitor.py
│   └── report_gen.py
├── utils/
│   ├── __init__.py
│   ├── colors.py
│   └── helpers.py
├── wordlists/
│   ├── common_ports.txt
│   └── weak_passwords.txt
└── output/                # Generated reports
```

