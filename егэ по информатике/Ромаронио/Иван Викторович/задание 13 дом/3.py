from ipaddress import *
for i in range(32, -1, -1):
	net = ip_network(f'117.191.208.37/{i}', 0)
	if '117.191.192.0' in str(net):
		print(net.netmask)