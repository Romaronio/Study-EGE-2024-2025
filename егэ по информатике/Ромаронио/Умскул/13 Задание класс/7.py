from ipaddress import *
for n in range(9):
	a = int('1' * n + '0' * (8 - n), 2)
	net = ip_network(f'127.254.{a}.19/255.255.224.0', 0)
	for ip_add in net:
		if f'{ip_add:b}'[:16].count('1') >= f'{ip_add:b}'[16:].count('1') == False:
			break
	else: 
		print(a)
