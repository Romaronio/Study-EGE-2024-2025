f = open('24_2424.txt')

for s in f:
  for i in range(17, 200):
    if i * 'XYZ' in s:
      print(True)
      print(17 * 3)
#   s = s.replace('\n','')
#   s = s.replace('\t','')
#   s = s.replace(' ','')
#   s = s.replace('Y', 'X')
#   s = s.replace('Z', 'X')
#   for i in s:
#     if i in 'ABCDEFGHIJKLMNOPQRSTUVWYZ':
#       s = s.replace(i, 'N')
#   s = s.split('N')
#   for n in range(1000):
#     if n * 'X' in s:
#       res_mas.append(int(n))
# print(max(res_mas))