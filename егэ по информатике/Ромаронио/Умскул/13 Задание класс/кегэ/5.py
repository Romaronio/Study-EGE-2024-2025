from ipaddress import *
for mask in range(33):
  net = ip_network(f'148.195.140.28/{mask}', 0)
  print(net, net.netmask)

