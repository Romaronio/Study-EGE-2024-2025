f = open('26.2.txt')
s = f.readline()
a = [int(s) for s in f]
a.sort()
a_sale_min = [i / 2 for i in a[:2500]]
print(a_sale_min)
a.sort(reverse=True)
a_sale_max = [i / 2 for i in a[:2500]]
print(a_sale_max)

print(sum(a) - sum(a_sale_min))
print(sum(a) - sum(a_sale_max))
















