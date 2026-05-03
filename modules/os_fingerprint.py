import subprocess
import re

class OSFingerprint:
    def detect(self, target):
        try:
            # Use ping to get TTL
            result = subprocess.run(['ping', '-c', '1', '-W', '2', target], 
                                  capture_output=True, text=True)
            
            ttl_match = re.search(r'ttl=(\d+)', result.stdout.lower())
            
            if ttl_match:
                ttl = int(ttl_match.group(1))
                
                if ttl <= 64:
                    os_name = "Linux / Unix"
                    accuracy = 85
                elif ttl <= 128:
                    os_name = "Windows"
                    accuracy = 80
                elif ttl <= 255:
                    os_name = "Cisco / Solaris"
                    accuracy = 75
                else:
                    os_name = "Unknown"
                    accuracy = 50
                
                # Try nmap if available
                try:
                    nmap_result = subprocess.run(['nmap', '-O', target], 
                                               capture_output=True, text=True, timeout=30)
                    if 'Windows' in nmap_result.stdout:
                        os_name = "Windows"
                        accuracy = 90
                    elif 'Linux' in nmap_result.stdout:
                        os_name = "Linux"
                        accuracy = 90
                except:
                    pass
                
                confidence = "High" if accuracy > 80 else "Medium" if accuracy > 60 else "Low"
                
                return {
                    'os': os_name,
                    'accuracy': accuracy,
                    'confidence': confidence,
                    'ttl': ttl
                }
            
            return {'os': 'Unknown', 'accuracy': 0, 'confidence': 'Low', 'ttl': None}
            
        except:
            return {'os': 'Unknown', 'accuracy': 0, 'confidence': 'Low', 'ttl': None}
