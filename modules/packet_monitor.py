import socket
import struct
import time

class PacketMonitor:
    def __init__(self):
        self.packets = []
    
    def capture(self, interface, count=50):
        self.packets = []
        
        try:
            # Create raw socket
            sock = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))
            sock.settimeout(5)
            
            for _ in range(count):
                try:
                    packet, addr = sock.recvfrom(65535)
                    self.parse_packet(packet)
                except socket.timeout:
                    break
                except:
                    pass
            
            sock.close()
        except:
            # Fallback to tcpdump
            result = subprocess.run(['timeout', '5', 'tcpdump', '-c', str(count), '-n'], 
                                   capture_output=True, text=True)
            lines = result.stdout.split('\n')
            for line in lines:
                if 'IP' in line:
                    self.packets.append({'raw': line[:100]})
        
        return self.packets
    
    def parse_packet(self, packet):
        try:
            # Ethernet header
            eth_header = packet[:14]
            eth_proto = struct.unpack('!6s6sH', eth_header)[2]
            
            if eth_proto == 0x0800:  # IPv4
                ip_header = packet[14:34]
                iph = struct.unpack('!BBHHHBBH4s4s', ip_header)
                
                src_ip = socket.inet_ntoa(iph[8])
                dst_ip = socket.inet_ntoa(iph[9])
                protocol = iph[6]
                
                proto_name = {1: 'ICMP', 6: 'TCP', 17: 'UDP'}.get(protocol, 'OTHER')
                
                self.packets.append({
                    'src': src_ip,
                    'dst': dst_ip,
                    'protocol': proto_name,
                    'size': len(packet)
                })
        except:
            pass
