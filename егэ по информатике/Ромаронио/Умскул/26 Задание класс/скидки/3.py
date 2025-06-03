# f = open('26.3.txt')
# n = f.readline()
# s = [int(i) for i in f]
# s.sort()
# max_sale = []
# min_sale = []
# mas = []
# print(sum([i for i in s]))
# obshay_stoimost = [i for i in s]
# for i in range(len(s)):
#   mas.append([[s[i], s[i + 1], s[i + 2]] for i in range(len(s) - 2)])
#   break
# for i in mas:
#   for n in i:
#     min_sale.append(max(n))
#
# for i in mas:
#   for n in i:
#     min_sale.append(min(n))
#
# print(sum(obshay_stoimost), sum(min_sale))




f = open('26.3.txt')
n = int(f.readline())
a = [int(s) for s in f]
a.sort(reverse=True)
sale1 = sum(a[:n//3])
print(sum(a) - sale1)
sale2 = 0
for i in range(n):
  if (i + 1) % 3 == 0:
    sale2 += a[i]
print(sum(a) - sale2)






