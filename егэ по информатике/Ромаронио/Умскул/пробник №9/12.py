from ipaddress import *
k = 0
net = ip_network('201.156.9.120/255.255.255.128', 0)
for ip in net:
    k += 1

print(k, 128 / 21)