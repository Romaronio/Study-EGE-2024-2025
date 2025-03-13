from ipaddress import *
net = ip_network('172.16.80.0/255.255.248.0', 0)
k = 0
for i in net:
  if f'{i:b}'.count('1') % 2 == 1:
    k += 1
print(k)