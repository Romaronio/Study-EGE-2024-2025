from ipaddress import *
for mask in range(33):
  net = ip_network(f'111.81.208.27/{mask}', 0)
  print(net, net.netmask)

# print(bin(208)[2:])
# print(bin(192)[2:])
# 11010000
# 11000000
# print(int('11000000', 2))