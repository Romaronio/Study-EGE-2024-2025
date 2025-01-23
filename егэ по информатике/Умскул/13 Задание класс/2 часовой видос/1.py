from ipaddress import *
k = 0
net = ip_network('192.168.32.176/255.255.255.240')
for ip_add in net:
	if f'{ip_add:b}'.count('1') % 2 == 1:
		k += 1
	print(k, ip_add)