from ipaddress import *
for n in range(32, -1, -1):
	net = ip_network(f'215.181.200.27/{n}', 0)
	if '215.181.192.0' in str(net):
		print(net.netmask)