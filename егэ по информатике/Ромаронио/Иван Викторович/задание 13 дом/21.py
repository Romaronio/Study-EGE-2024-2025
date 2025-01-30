from ipaddress import *
for i in range(255, -1, -1):
	net = ip_network(f'196.233.{i}.52/255.255.255.248', 0)
	if all((bin(int(ip))[2:].zfill(32))[:16].count('1') > (bin(int(ip))[2:].zfill(32))[16:].count('1') for ip in net):
		print(i)
		break