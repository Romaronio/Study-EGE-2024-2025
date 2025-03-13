from ipaddress import *
net = ip_network(f'192.168.156.235/255.255.255.240', 0)
for ip, x in enumerate(net):
  print(ip, x)