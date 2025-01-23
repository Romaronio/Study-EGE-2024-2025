from ipaddress import *
net = ip_network('142.96.56.118/255.255.255.240', 0)
k = 0
for ip_add in net:
	if f'{ip_add:b}'[:16].count('1') < f'{ip_add:b}'[16:].count('1'):
		k += 1
print(k)