from ipaddress import *
for mask in range(33):
    net = ip_network(f'76.155.48.2/{mask}', 0)
    print(net)
