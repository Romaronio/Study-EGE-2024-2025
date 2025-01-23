from ipaddress import *
for i in range(32, -1, -1):
	net = ip_network(f'149.238.225.115/{i}', 0)
	k = 0
	if ip_address('149.238.238.149') in net:
		for ip in net:
			ip_bin = bin(int(ip))[2:].zfill(32)
			if ip_bin.count('1') == 15:
				k += 1
		print(k)
		break