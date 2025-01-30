from ipaddress import *
for i in range(33):
	net = ip_network(f'111.81.27.224/{i}', 0)
	if '111.81.27.192' in str(net):
		print(net.netmask)