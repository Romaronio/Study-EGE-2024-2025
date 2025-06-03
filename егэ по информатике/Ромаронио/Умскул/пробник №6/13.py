from ipaddress import *
net = ip_network('192.168.32.160/255.255.255.240', 0)
n = 0
k = 0
for ip in net:
  ip = f'{ip:b}'
  n += 1
  if ip.count('1') % 2 == 0:
    k += 1

print(k, n)