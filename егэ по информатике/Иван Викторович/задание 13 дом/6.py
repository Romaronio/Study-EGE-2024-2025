from ipaddress import *
for i in range(33):
	net = ip_network(f'190.120.251.78/{i}', 0)
	if '190.120.251.0' in str(net):
		print(32 - i)