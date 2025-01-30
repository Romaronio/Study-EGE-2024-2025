from ipaddress import *
for i in range(32, -1, -1):
	net = ip_network(f'147.222.199.75/{i}', 0)
	k = 0
	if ip_address('147.222.222.147') in net:
		for ip in net:
			ip_bin = bin(int(ip))[2:].zfill(32)
			if ip_bin.count('1') == 14:
				k += 1
		print(k)
		break