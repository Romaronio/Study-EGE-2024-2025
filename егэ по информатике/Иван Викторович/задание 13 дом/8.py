from ipaddress import *
for i in range(33):
	net1 = ip_network(f'161.158.136.231/{i}', 0)
	net2 = ip_network(f'161.158.138.65/{i}', 0)
	if net1 == net2:
		print(net1.netmask)