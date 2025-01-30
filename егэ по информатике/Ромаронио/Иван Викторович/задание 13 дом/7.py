from ipaddress import *
for i in range(33):
	net = ip_network(f'93.138.161.49/{i}', 0)
	if '93.138.160.0' in str(net):
		print(i)