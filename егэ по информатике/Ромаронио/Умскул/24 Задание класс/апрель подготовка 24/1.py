# f = open('24_1.txt')
# s = f.readline()
# s = s.replace('*', '#').replace('+', '#')
# res_mas = []
# mas = []
# for i in s.split('#'):
#   mas.append(i)
#
# for n in mas:
#   if len(n) > 0 and n[0] not in 'AB':
#     res_mas.append(n)
#
# print(len(max(res_mas, key=len)))

import re
f = open('24_1.txt')
s = f.readline()
is_valid = re.findall('[123456789][1234567890AB]*', s)


