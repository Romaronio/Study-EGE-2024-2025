f = open('26.2.txt')
s = int(f.readline())
mas = [int(s) for s in f]
mas.sort()
max_sale = [i for i in mas[7500:]]
min_sale = [i for i in mas[:2500]]
print(sum(mas[:7500]) + sum(max_sale) * 0.5)
print(sum(mas[2500:]) + sum(min_sale) * 0.5)