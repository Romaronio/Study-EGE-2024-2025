from ipaddress import *
net = ip_network('112.160.0.0/255.255.240.0')
k = 0
for ip_add in net:
	if f'{ip_add}:b'.count('1') % 5 == 0:
		k += 1
print(k, ip_add)