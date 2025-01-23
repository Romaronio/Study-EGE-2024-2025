from ipaddress import *
net = ip_network('106.184.0.0/255.248.0.0')
k = 0
for ip in net:
	if (bin(int(ip))[2:]).count('1') % 2 == 1:
		k += 1
print(k)