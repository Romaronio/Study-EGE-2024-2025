from ipaddress import *
k = 0
net = ip_network('112.160.0.0/255.255.240.0')
for ip_add in net:
	if f'{ip_add:b}'.count('1') % 3 != 0:
		k += 1
	print(k)