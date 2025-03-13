from ipaddress import *
net = ip_network(f'184.178.54.144/255.255.255.240')
for ip in net:
  print(f'{ip:b}')
  print(bin(int(ip))[2:].zfill(32))
# print(bin(184)[2:])
# for x in range(144, 160):