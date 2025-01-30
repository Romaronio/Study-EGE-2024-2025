from ipaddress import *
k = 0
net = ip_network('141.14.138.235/255.255.224.0', 0)
for ip_add in net:
	if int(f'{ip_add:b}'[:8], 2) == 141:
		if int(f'{ip_add:b}'[:8], 2) <= 200:
			if int(f'{ip_add:b}'[8:16], 2) <= 200:
				if int(f'{ip_add:b}'[16:24], 2) <= 200:
					if int(f'{ip_add:b}'[24:32], 2) <= 200:
						if int(f'{ip_add:b}'[24:32], 2) % 2 == 0:
							k += 1
print(k)