from ipaddress import *
for i in range(32, -1, -1):
	net1 = ip_network(f'161.137.200.35/{i}', 0)
	net2 = ip_network(f'161.137.150.118/{i}', 0)
	if net1 == net2:
		k = 0
		for ip1 in net1:
			if bin(int(ip1))[2:].count('1') % 2 == 1:
				k += 1
		print(k)
		break
	