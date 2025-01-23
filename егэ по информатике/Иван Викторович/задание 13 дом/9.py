from ipaddress import *
for i in range(32, -1, -1):
	net1 = ip_network(f'98.162.78.100/{i}', 0)
	net2 = ip_network(f'98.162.78.90/{i}', 0)
	if net1 == net2:
		print(i)