from ipaddress import *
for a in range(256):
	try:
		net = ip_network(f'117.157.2.8/255.255.{a}.0', 0)
		if all((bin(int(ip))[2:].zfill(32))[:16].count('1') >= (bin(int(ip))[2:].zfill(32))[16:].count('1') for ip in net):
			print(a)
			break
	except: pass