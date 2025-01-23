from ipaddress import *
for n in range(9):
	a = int('1' * n + "0" * (8 - n), 2)
	net = ip_network(f'255.224.33.160/255.255.{a}.0', 0)
	for ip_net in net:
		if (f'{ip_net:b}'[:16].count('1') >= f'{ip_net:b}'[16:].count('1')) == False:
			break
	else:
		print(a, ip_net)