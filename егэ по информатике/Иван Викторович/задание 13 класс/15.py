from ipaddress import *
k = 0
net = ip_network('202.75.38.160/255.255.255.240', 0)
for ip in net:
	biin = bin(int(ip))[2:].zfill(32)
	if '111' in biin:
		k += 1
print(k)
