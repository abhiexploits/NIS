import subprocess
import re
import threading
from concurrent.futures import ThreadPoolExecutor

class NetworkScanner:
    def __init__(self):
        self.devices = []
    
    def scan(self, network):
        print(f"[*] Scanning network: {network}")
        
        # Use arp-scan if available, else fallback to ping
        try:
            result = subprocess.run(['arp-scan', '--localnet'], 
                                  capture_output=True, text=True, timeout=30)
            lines = result.stdout.split('\n')
            
            for line in lines:
                match = re.search(r'(\d+\.\d+\.\d+\.\d+)\s+([0-9a-f:]{17})\s+(.+)', line)
                if match:
                    self.devices.append({
                        'ip': match.group(1),
                        'mac': match.group(2),
                        'hostname': match.group(3)
                    })
        except:
            self.ping_scan(network)
        
        return self.devices
    
    def ping_scan(self, network):
        base_ip = network.rsplit('.', 1)[0]
        
        def ping_ip(ip):
            result = subprocess.run(['ping', '-c', '1', '-W', '1', ip], 
                                  capture_output=True)
            if result.returncode == 0:
                hostname = self.get_hostname(ip)
                mac = self.get_mac(ip)
                self.devices.append({
                    'ip': ip,
                    'mac': mac,
                    'hostname': hostname
                })
                print(f"[+] Found: {ip}")
        
        with ThreadPoolExecutor(max_workers=50) as executor:
            for i in range(1, 255):
                ip = f"{base_ip}.{i}"
                executor.submit(ping_ip, ip)
    
    def get_hostname(self, ip):
        try:
            result = subprocess.run(['nslookup', ip], capture_output=True, text=True)
            lines = result.stdout.split('\n')
            for line in lines:
                if 'name = ' in line:
                    return line.split('name = ')[1].strip()
        except:
            pass
        return "Unknown"
    
    def get_mac(self, ip):
        try:
            result = subprocess.run(['arp', '-n', ip], capture_output=True, text=True)
            lines = result.stdout.split('\n')
            for line in lines:
                if ip in line:
                    parts = line.split()
                    if len(parts) >= 3:
                        return parts[2]
        except:
            pass
        return "Unknown"
