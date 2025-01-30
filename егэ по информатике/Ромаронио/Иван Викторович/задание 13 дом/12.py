from ipaddress import *
net = ip_network('206.158.124.67/255.255.224.0', 0)
k = 0
for ip in net:
	if str(ip) == '206.158.124.67':
		print(k)
	k += 1