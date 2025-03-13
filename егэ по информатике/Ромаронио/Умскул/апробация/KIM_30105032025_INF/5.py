# for n in range(1, 1000):
#   s = bin(n)[2:]
#   if s.count('1') % 2 == 0:
#     s = s + '0'
#     s = '10' + s[2:]
#   else:
#     s = s + '1'
#     s = '11' + s[2:]
#   if int(s, 2) > 19:
#     print(int(s, 2), s, n)
#     break

print(bin(7)[2:])
print(int('1111', 2))