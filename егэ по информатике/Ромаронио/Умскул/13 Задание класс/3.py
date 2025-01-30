from ipaddress import *
ip_net = ip_network('192.168.32.160/255.255.255.240')
k = 0
for ip_add in ip_net:
	if f'{ip_add:b}'.count('1') % 2 == 0:
		k += 1
print(k)
