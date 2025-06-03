from ipaddress import *
net = ip_network('144.168.52.210/255.255.255.240', 0)
for i in net:
    print(i)