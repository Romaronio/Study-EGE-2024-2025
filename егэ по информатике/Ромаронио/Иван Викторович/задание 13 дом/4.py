from ipaddress import *
for i in range(33):
	net = ip_network(f'170.155.137.181/{i}', 0)
	if '170.155.136.0' in str(net):
		print(net.netmask)