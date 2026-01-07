from scapy.all import ARP, Ether, srp
import json

def scan_network(ip_range):
    print(f"Scanning {ip_range}...")
    try:
        arp = ARP(pdst=ip_range)
        ether = Ether(dst="ff:ff:ff:ff:ff:ff")
        result = srp(ether/arp, timeout=3, verbose=False)[0]
        
        devices = []
        for sent, received in result:
            devices.append({'ip': received.psrc, 'mac': received.hwsrc})
        
        # Data ko file mein SAVE karna
        with open("network_log.json", "w") as f:
            json.dump(devices, f, indent=4)
        
        return devices
    except Exception as e:
        print(f"Scanner Error: {e}")
        return []

if __name__ == "__main__":
    # Test ke liye:
    scan_network("192.168.1.1/24")