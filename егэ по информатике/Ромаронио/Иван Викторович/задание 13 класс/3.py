from ipaddress import *
for n in range(33):
	net = ip_network(f'119.167.50.77/{n}', 0)
	if '119.167.48.0' in str(net):
		print(net.netmask)
		break