from ipaddress import *
for i in range(33):
	net = ip_network(f'113.191.169.34/{i}', 0)
	if '113.191.160.0' in str(net):
		print(i)