from ipaddress import *
for i in range(32, -1, -1):
	net1 = ip_network(f'151.172.115.121/{i}', 0)
	net2 = ip_network(f'151.172.115.156/{i}', 0)
	if net1 != net2:
		print()