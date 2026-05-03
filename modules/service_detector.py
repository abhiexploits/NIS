import socket
import re

class ServiceDetector:
    def __init__(self):
        self.service_patterns = {
            'SSH': r'SSH-\d+\.\d+',
            'HTTP': r'HTTP/\d+\.\d+',
            'FTP': r'220.*FTP',
            'SMTP': r'220.*ESMTP',
            'MySQL': r'mysql',
            'PostgreSQL': r'PostgreSQL',
            'MongoDB': r'MongoDB',
            'Redis': r'redis',
            'VNC': r'RFB',
            'RDP': r'RDP'
        }
    
    def detect(self, ip, port, timeout=3):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(timeout)
            sock.connect((ip, port))
            
            # Send generic probe
            sock.send(b'HEAD / HTTP/1.0\r\n\r\n')
            banner = sock.recv(1024).decode('utf-8', errors='ignore')
            sock.close()
            
            for service, pattern in self.service_patterns.items():
                if re.search(pattern, banner, re.IGNORECASE):
                    return service
            
            if '220' in banner:
                return 'FTP'
            elif 'SSH' in banner:
                return 'SSH'
            elif 'HTTP' in banner:
                return 'HTTP'
            elif '220' in banner and 'ESMTP' in banner:
                return 'SMTP'
            else:
                return 'Unknown'
                
        except:
            return 'Unknown or filtered'
