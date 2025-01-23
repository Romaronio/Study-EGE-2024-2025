from ipaddress import *
for i in range(32, -1, -1):
	net1 = ip_network(f'154.63.206.129/{i}', 0)
	net2 = ip_network(f'154.63.100.75/{i}', 0)
	if net1 == net2:
		k = 0
		for ip1 in net1:
			if bin(int(ip1))[2:].count('1') % 2 == 0:
				k += 1
		print(k)
		break
