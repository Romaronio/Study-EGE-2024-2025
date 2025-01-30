from ipaddress import *
for a in range(255, -1, -1):
	net = ip_network(f'227.31.{a}.139/255.255.255.224', 0)
	if all((bin(int(ip))[2:].zfill(32))[:16].count('0') <= (bin(int(ip))[2:].zfill(32))[16:].count('0') for ip in net):
		print(a)
		break