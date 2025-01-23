from ipaddress import *
ip_ad1 = ip_address('200.60.130.4')
ip_ad2 = ip_address('200.60.140.44')
ip_ad3 = ip_address('200.60.150.48')
for mask in range(0, 33):
	ip_net = ip_network(f'200.60.130.4/{mask}', 0)
	if ((ip_ad1 in ip_net) + (ip_ad2 in ip_net) + (ip_ad3 in ip_net)) == 2:
		k = 0
		for ip_add in ip_net:
			if f'{ip_add:b}'.count('1') == 10:
				k += 1
		print(k)