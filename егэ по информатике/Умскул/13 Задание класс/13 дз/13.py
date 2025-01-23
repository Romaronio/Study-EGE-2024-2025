from ipaddress import *
k = 0
net = ip_network('231.168.192.196/255.255.255.240', 0)
for ip_add in net:
	if f'{ip_add:b}'.count('1') % 2 == 1:
		k += 1
print(k)