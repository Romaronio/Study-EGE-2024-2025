f = open('26.3.txt')
s = int(f.readline())
mas = [int(s) for s in f]
res_mas = []
mas.sort(reverse=True)
fink_sale_price = [i for i in mas[:3333]]
for i in range(2, len(mas), 3):
  res_mas.append(mas[i])
print(sum(mas) - sum(fink_sale_price), sum(mas) - sum(res_mas))

