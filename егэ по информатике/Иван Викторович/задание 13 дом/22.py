from ipaddress import *
for i in range(256):
	try:
		net = ip_network(f'134.97.250.117/255.255.{i}.0', 0)
		if all((bin(int(ip))[2:].zfill(32))[:16].count('0') >= (bin(int(ip))[2:].zfill(32))[16:].count('0') for ip in net):
			print(i)
			break
	except: pass