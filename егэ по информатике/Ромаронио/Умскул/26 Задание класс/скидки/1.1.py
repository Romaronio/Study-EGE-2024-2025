f = open('26.1.txt')
s = f.readline()
mas = [int(s) for s in f]
sale_product = []
sale_price = []
not_sale_price = []
not_sale_product = []
mas.sort()

for i in mas:
  if i > 120:
    sale_product.append(i)
  else:
    not_sale_product.append(i)

for i in sale_product[:449]:
  sale_price.append(i - i * 0.25)

for i in sale_product[449:]:
  not_sale_price.append(i)

print(sum(sale_price) + sum(not_sale_price) + sum(not_sale_product), max(sale_price) + max(sale_price) * 0.25)




