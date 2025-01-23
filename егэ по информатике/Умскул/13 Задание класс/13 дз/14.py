from ipaddress import *
k = 0
net = ip_network('181.165.17.108/255.255.192.0', 0)
for ip_add in net:
	if f'{ip_add:b}'.count('0') % 9 == 0:
		k += 1
print(k)