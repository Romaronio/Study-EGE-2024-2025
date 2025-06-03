from ipaddress import *
mas = []
net = ip_network('185.8.0.0/255.255.128.0')
for ip in net:
  s = f'{ip:b}'.count('1')
  mas.append(s)

print(max(mas))
