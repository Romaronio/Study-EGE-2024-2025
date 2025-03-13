k = 0
from ipaddress import *
net = ip_network(f'211.48.136.64/255.255.255.224')
for ip in net:
  if f'{ip:b}'[-2:] == '11':
    k += 1
# k = 0
# for x in range(64, 96):
#   s = bin(x)[2:]
#   if s[-2:] == '11':
#     k += 1


print(k)