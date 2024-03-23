from scapy.all import *

eth = Ether()
arp = ARP()

eth.dst = "ff:ff:ff:ff:ff:ff"
arp.pdst = "INPUT IP" # Kali 'inet' IP that can be found in 'ifconfig' section, try adding "/24" at the end.
bcPckt = eth/arp
# bcPckt.show()

ans, unans = srp(bcPckt, timeout=5)

#ans.summary()
print("#"*30)
#unans.summary()

for snd, rcv in ans:
    #rcv.show()
    print(rcv.src, " : ", rcv.psrc)