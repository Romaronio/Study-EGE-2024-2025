from ipaddress import *
net = ip_network('94.149.96.0/255.255.224.0')
k = 0
for ip in net:
	if bin(int(ip))[-2:] == '11' and (bin(int(ip))[2:]).count('1') % 3 == 0:
		k += 1
print(k)