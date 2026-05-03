import socket
import threading
from concurrent.futures import ThreadPoolExecutor

class PortScanner:
    def __init__(self):
        self.open_ports = []
        self.common_ports = {
            21: 'FTP', 22: 'SSH', 23: 'Telnet', 25: 'SMTP', 53: 'DNS',
            80: 'HTTP', 110: 'POP3', 111: 'RPC', 135: 'RPC', 139: 'NetBIOS',
            143: 'IMAP', 443: 'HTTPS', 445: 'SMB', 993: 'IMAPS', 995: 'POP3S',
            1723: 'PPTP', 3306: 'MySQL', 3389: 'RDP', 5432: 'PostgreSQL',
            5900: 'VNC', 6379: 'Redis', 8080: 'HTTP-Alt', 27017: 'MongoDB'
        }
    
    def scan_port(self, ip, port, timeout=0.5):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(timeout)
            result = sock.connect_ex((ip, port))
            if result == 0:
                service = self.common_ports.get(port, 'Unknown')
                self.open_ports.append({'port': port, 'service': service})
                print(f"    Port {port} - OPEN ({service})")
            sock.close()
        except:
            pass
    
    def scan(self, target, port_range):
        self.open_ports = []
        
        if '-' in port_range:
            start, end = map(int, port_range.split('-'))
            ports = range(start, end + 1)
        else:
            ports = [int(port_range)]
        
        print(f"[*] Scanning {target} on ports {min(ports)}-{max(ports)}")
        
        with ThreadPoolExecutor(max_workers=100) as executor:
            for port in ports:
                executor.submit(self.scan_port, target, port)
        
        return [p['port'] for p in self.open_ports]
