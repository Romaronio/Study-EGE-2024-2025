from ipaddress import *
k = 0
net = ip_network("252.67.33.87/255.255.0.0", 0)
for ip_add in net:
	if f"{ip_add:b}"[:16].count('1') < f"{ip_add:b}"[16:].count('1'):
		k += 1
print(k)