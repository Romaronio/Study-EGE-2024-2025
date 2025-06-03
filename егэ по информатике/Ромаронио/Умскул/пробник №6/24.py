f = open('24.txt')
s = f.readline()
s = s.replace('A', 'Г').replace('E', 'Г').replace('B', 'С').replace('C', 'С').replace('D', 'С')
for i in range(10):
  if 'ССГ' * i in s:
    print(i)
