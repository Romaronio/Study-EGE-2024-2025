from ipaddress import *
k = 0
for i in range(33):
	net = ip_network(f'175.122.80.13/{i}', 0)
	if '175.122.80.0' in str(net):
		if net.num_addresses >= 58:
			k += 1
print(k)
