from ipaddress import *
net = ip_network('202.75.38.176/255.255.255.240')
k = 0
for ip in net:
	if '000' not in bin(int(ip))[2:] and not '111' in bin(int(ip))[2:]:
		k += 1
print(k)