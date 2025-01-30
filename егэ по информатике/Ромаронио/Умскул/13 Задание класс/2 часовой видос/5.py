from ipaddress import *
k = 0
net = ip_network('252.67.33.87/255.248.0.0', 0)
for ip_add in net:
	if (bin(int(ip_add))[2:].zfill(32)[16:].count('1') / bin(int(ip_add))[2:].zfill(32)[:16].count('1')) > 2:
		k += 1
print(k)