from ipaddress import *
for n in range(33):
	net1 = ip_network(f'10.96.180.231/{n}', 0)
	net2 = ip_network(f'10.96.140.118/{n}', 0)
	if net1 != net2:
		print(32 - n)
		break