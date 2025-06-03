# sum = []
# for n in range(1, 1000):
#     s = bin(n)[2:]
#     if n % 6 == 0:
#         s = str(s.count('1') % 2) + s
#     else:
#         s = s + '0'
#     if (str(int(s)).count('0') + str(int(s)).count('1')) % 2 == 0:
#         s = s + '0'
#     else:
#         s = s + '1'
#     s = int(s, 2)
#     M = abs(n - s)
#     if M > 2022:

#         M = hex(M)[2:]
#         dict = 0
#         for i in M:
#             if i in 'abcdef':
#                 if i == 'a':
#                     dict += 10
#                 elif i == 'b':
#                     dict += 11
#                 elif i == 'c':
#                     dict += 12
#                 elif i == 'd':
#                     dict += 13
#                 elif i == 'e':
#                     dict += 14
#                 elif i == 'f':
#                     dict += 15
#             if i in '0123456789':
#                 dict += int(i)
#         sum.append(dict)
# print(sum)


print(hex(2571)[2:])
