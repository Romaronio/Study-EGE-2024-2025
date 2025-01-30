from ipaddress import *
k = 0
for i in range(33):
	net = ip_network(f'115.53.128.88/{i}', 0)
	if '115.53.128.0' in str(net):
		if net.num_addresses >= 1000:
			k += 1
print(k)