from ipaddress import *
for mask in range(33):
  net1 = ip_network(f'157.220.185.237/{mask}', 0)
  net2 = ip_network(f'157.220.184.230/{mask}', 0)
  if net1 == net2:
    if mask == 15:
      print(net1.num_addresses)



