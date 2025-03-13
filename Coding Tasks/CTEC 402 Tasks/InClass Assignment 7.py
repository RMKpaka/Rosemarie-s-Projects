from scapy.all import sniff

def packet_callback(packet):
    print(packet.summary())

# Sniff network packets
print("Starting packet sniffer... Press Ctrl+C to stop.")
sniff(prn=packet_callback, count=10)  # Adjust count or remove it for continuous sniffing
