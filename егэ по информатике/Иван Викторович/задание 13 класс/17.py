from ipaddress import *
k = 0
net = ip_network('186.135.80.0/255.255.252.0', 0)
for ip in net:
	biin = bin(int(ip))[2:].zfill(32)
	if biin[:16].count('1') > biin[16:].count('1'):
		k += 1
print(k)	