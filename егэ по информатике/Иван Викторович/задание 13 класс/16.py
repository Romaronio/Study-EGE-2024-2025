from ipaddress import *
k = 0
net = ip_network('102.141.0.0/255.255.192.0', 0)
for ip in net:
	biin = bin(int(ip))[2:].zfill(32)
	if biin.count('1') % 7 == 0:
		if biin[-4:] == '1011':
			k += 1
print(k)