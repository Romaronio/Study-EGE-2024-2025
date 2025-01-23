from ipaddress import *
for mask in range(32, -1, -1):
	ip_net = ip_network(f'121.96.174.205/{mask}', 0)
	k = 0
	for ip_add in ip_net:
		if f'{ip_add:b}'.count('1') == 12:
			k += 1
	if k == 10:
		print(mask)
		break