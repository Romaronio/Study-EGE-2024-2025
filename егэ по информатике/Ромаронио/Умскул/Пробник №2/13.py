from ipaddress import *
k = 0
net = ip_network("202.212.201.183/202.212.192.0", 0)
print(net)
for ip_add in net:
	if f"{ip_add:b}"[:16].count('1') < f"{ip_add:b}"[16:].count('1'):
		k += 1
print(k)