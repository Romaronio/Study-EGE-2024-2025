from ipaddress import *
k = 0
net = ip_network('176.54.23.0/255.255.224.0', 0)
for ip_add in net:
	if f'{ip_add}'.count('2') % 3 == 0:
		k += 1
print(k)