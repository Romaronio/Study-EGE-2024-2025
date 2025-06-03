from ipaddress import *
net = ip_network('154.24.txt.165.32/255.255.255.224')
k = 0
for ip in net:
	biin = bin(int(ip))[2:].zfill(32)
	if (biin[:16]).count('1') < (biin[16:]).count('1'):
		k += 1
print(k)