import socket
import subprocess

class VulnChecker:
    def __init__(self):
        self.weak_services = {
            21: 'FTP - Anonymous login possible?',
            23: 'Telnet - Unencrypted traffic',
            80: 'HTTP - Check for default pages',
            443: 'HTTPS - Check SSL/TLS version',
            3306: 'MySQL - Default root password?',
            3389: 'RDP - Weak encryption possible',
            5900: 'VNC - Default/no authentication?',
            6379: 'Redis - No auth by default',
            27017: 'MongoDB - No auth by default'
        }
    
    def check(self, target):
        vulnerabilities = []
        
        # Check common weak ports
        for port, description in self.weak_services.items():
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(1)
                result = sock.connect_ex((target, port))
                if result == 0:
                    vulnerabilities.append({
                        'type': 'Open Weak Service',
                        'port': port,
                        'description': description,
                        'severity': 'MEDIUM'
                    })
                sock.close()
            except:
                pass
        
        # Check for default credentials (simulated)
        try:
            default_checks = [
                ('SSH', ['root:root', 'admin:admin']),
                ('FTP', ['anonymous:anonymous', 'ftp:ftp']),
                ('HTTP', ['admin:admin', 'root:toor'])
            ]
        except:
            pass
        
        return vulnerabilities
