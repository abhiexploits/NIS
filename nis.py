#!/usr/bin/env python3
import os
import sys
import json
import time
from datetime import datetime
from modules.network_scanner import NetworkScanner
from modules.port_scanner import PortScanner
from modules.service_detector import ServiceDetector
from modules.os_fingerprint import OSFingerprint
from modules.vuln_checker import VulnChecker
from modules.packet_monitor import PacketMonitor
from modules.report_gen import ReportGen
from utils.colors import Colors
from utils.helpers import validate_ip, validate_network

class NIS:
    def __init__(self):
        self.colors = Colors()
        self.results = {}
        self.start_time = None
        
    def show_banner(self):
        os.system('clear')
        banner = f"""
{self.colors.RED}
╔═══════════════════════════════════════════════════════════════════╗
║                                                                   ║
║     NETWORK INTELLIGENCE SUITE (NIS) v1.0                         ║
║     Professional Network Security Toolkit                         ║
║                                                                   ║
║     For Authorized Testing Only                                   ║
║                                                                   ║
║                    Developed by Abhishek                          ║
║                                                                   ║
╚═══════════════════════════════════════════════════════════════════╝
{self.colors.RESET}
        """
        print(banner)
    
    def show_menu(self):
        menu = f"""
{self.colors.CYAN}┌─────────────────────────────────────────────────────────────┐
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
{self.colors.RESET}
        """
        print(menu)
    
    def network_scan(self):
        print(f"\n{self.colors.YELLOW}[*] Network Scanner{self.colors.RESET}")
        network = input("Enter network (e.g., 192.168.1.0/24): ")
        
        if not validate_network(network):
            print(f"{self.colors.RED}[-] Invalid network format{self.colors.RESET}")
            return
        
        scanner = NetworkScanner()
        devices = scanner.scan(network)
        
        self.results['network_scan'] = devices
        print(f"\n{self.colors.GREEN}[+] Found {len(devices)} active devices{self.colors.RESET}")
        
        for device in devices:
            print(f"    {device['ip']} - {device['mac']} - {device['hostname']}")
        
        return devices
    
    def port_scan(self):
        print(f"\n{self.colors.YELLOW}[*] Port Scanner{self.colors.RESET}")
        target = input("Enter target IP: ")
        
        if not validate_ip(target):
            print(f"{self.colors.RED}[-] Invalid IP address{self.colors.RESET}")
            return
        
        port_range = input("Enter port range (default 1-1000): ") or "1-1000"
        
        scanner = PortScanner()
        open_ports = scanner.scan(target, port_range)
        
        self.results['port_scan'] = {target: open_ports}
        print(f"\n{self.colors.GREEN}[+] Found {len(open_ports)} open ports{self.colors.RESET}")
        
        for port in open_ports:
            print(f"    Port {port} - OPEN")
        
        return open_ports
    
    def service_detection(self):
        print(f"\n{self.colors.YELLOW}[*] Service Detector{self.colors.RESET}")
        target = input("Enter target IP: ")
        port = int(input("Enter port number: "))
        
        detector = ServiceDetector()
        service = detector.detect(target, port)
        
        self.results.setdefault('services', {})[f"{target}:{port}"] = service
        print(f"\n{self.colors.GREEN}[+] Service: {service}{self.colors.RESET}")
        
        return service
    
    def os_fingerprint(self):
        print(f"\n{self.colors.YELLOW}[*] OS Fingerprinting{self.colors.RESET}")
        target = input("Enter target IP: ")
        
        fingerprint = OSFingerprint()
        os_info = fingerprint.detect(target)
        
        self.results['os_fingerprint'] = {target: os_info}
        print(f"\n{self.colors.GREEN}[+] OS: {os_info['os']}{self.colors.RESET}")
        print(f"    Accuracy: {os_info['accuracy']}%")
        print(f"    Confidence: {os_info['confidence']}")
        
        return os_info
    
    def vuln_check(self):
        print(f"\n{self.colors.YELLOW}[*] Vulnerability Checker{self.colors.RESET}")
        target = input("Enter target IP: ")
        
        checker = VulnChecker()
        vulnerabilities = checker.check(target)
        
        self.results['vulnerabilities'] = vulnerabilities
        
        if vulnerabilities:
            print(f"\n{self.colors.RED}[!] Found {len(vulnerabilities)} potential issues{self.colors.RESET}")
            for vuln in vulnerabilities:
                print(f"    {vuln['type']} - {vuln['description']}")
        else:
            print(f"\n{self.colors.GREEN}[+] No obvious vulnerabilities found{self.colors.RESET}")
        
        return vulnerabilities
    
    def packet_monitor(self):
        print(f"\n{self.colors.YELLOW}[*] Packet Monitor{self.colors.RESET}")
        interface = input("Enter network interface (default eth0): ") or "eth0"
        count = int(input("Number of packets to capture (default 50): ") or 50)
        
        monitor = PacketMonitor()
        packets = monitor.capture(interface, count)
        
        self.results['packets'] = packets
        print(f"\n{self.colors.GREEN}[+] Captured {len(packets)} packets{self.colors.RESET}")
        
        for pkt in packets[:10]:
            print(f"    {pkt['src']} -> {pkt['dst']} | {pkt['protocol']} | {pkt['size']} bytes")
        
        return packets
    
    def full_scan(self):
        print(f"\n{self.colors.YELLOW}[*] Running Full Intelligence Scan{self.colors.RESET}")
        target = input("Enter target IP: ")
        
        if not validate_ip(target):
            print(f"{self.colors.RED}[-] Invalid IP address{self.colors.RESET}")
            return
        
        results = {}
        
        # Network scan first to find target
        network = input("Enter your network (e.g., 192.168.1.0/24): ")
        if validate_network(network):
            scanner = NetworkScanner()
            devices = scanner.scan(network)
            results['network'] = devices
        
        # Port scan
        print(f"\n{self.colors.CYAN}[*] Scanning ports...{self.colors.RESET}")
        port_scanner = PortScanner()
        open_ports = port_scanner.scan(target, "1-1000")
        results['open_ports'] = open_ports
        
        # Service detection on open ports
        results['services'] = {}
        service_detector = ServiceDetector()
        for port in open_ports[:10]:
            service = service_detector.detect(target, port)
            results['services'][port] = service
            print(f"    Port {port}: {service}")
        
        # OS fingerprint
        print(f"\n{self.colors.CYAN}[*] Identifying OS...{self.colors.RESET}")
        os_fp = OSFingerprint()
        results['os'] = os_fp.detect(target)
        print(f"    OS: {results['os']['os']}")
        
        # Vulnerability check
        print(f"\n{self.colors.CYAN}[*] Checking vulnerabilities...{self.colors.RESET}")
        vuln_checker = VulnChecker()
        results['vulnerabilities'] = vuln_checker.check(target)
        
        self.results['full_scan'] = results
        
        print(f"\n{self.colors.GREEN}[+] Full scan completed{self.colors.RESET}")
        print(f"    Open ports: {len(open_ports)}")
        print(f"    Services identified: {len(results['services'])}")
        print(f"    Vulnerabilities: {len(results['vulnerabilities'])}")
        
        return results
    
    def generate_report(self):
        if not self.results:
            print(f"{self.colors.RED}[-] No data to report. Run a scan first.{self.colors.RESET}")
            return
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"output/nis_report_{timestamp}"
        
        report_gen = ReportGen()
        report_gen.generate(self.results, filename)
        
        print(f"\n{self.colors.GREEN}[+] Report saved to {filename}.json and {filename}.html{self.colors.RESET}")
    
    def view_last_report(self):
        reports_dir = "output"
        if not os.path.exists(reports_dir):
            print(f"{self.colors.RED}[-] No reports found{self.colors.RESET}")
            return
        
        reports = [f for f in os.listdir(reports_dir) if f.endswith('.json')]
        if not reports:
            print(f"{self.colors.RED}[-] No reports found{self.colors.RESET}")
            return
        
        latest = sorted(reports)[-1]
        with open(f"{reports_dir}/{latest}", 'r') as f:
            data = json.load(f)
        
        print(f"\n{self.colors.CYAN}Last Report: {latest}{self.colors.RESET}")
        print(json.dumps(data, indent=2))
    
    def run(self):
        self.show_banner()
        
        while True:
            self.show_menu()
            choice = input(f"\n{self.colors.RED}nis@tool:~${self.colors.RESET} ")
            
            if choice == '1':
                self.network_scan()
            elif choice == '2':
                self.port_scan()
            elif choice == '3':
                self.service_detection()
            elif choice == '4':
                self.os_fingerprint()
            elif choice == '5':
                self.vuln_check()
            elif choice == '6':
                self.packet_monitor()
            elif choice == '7':
                self.full_scan()
            elif choice == '8':
                self.generate_report()
            elif choice == '9':
                self.view_last_report()
            elif choice == '0':
                print(f"\n{self.colors.YELLOW}[*] Exiting...{self.colors.RESET}")
                sys.exit()
            else:
                print(f"{self.colors.RED}[-] Invalid choice{self.colors.RESET}")
            
            input(f"\n{self.colors.CYAN}Press Enter to continue...{self.colors.RESET}")
            self.show_banner()

if __name__ == "__main__":
    nis = NIS()
    nis.run()
