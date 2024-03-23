from scapy.all import *

ip = IP()
icmp = ICMP()

pingPckt = ip/icmp

addr = "10.0.2."

ipList = []

for i in range(256):
    pingPckt[IP].dst = addr+str(i)
    response = sr1(pingPckt, timeout=0.5, verbose=False)
    print(response)
    if(response):
        print(pingPckt[IP].dst,"is up")
        ipList.append(pingPckt[IP].dst)
    else:
        pass

print(ipList)