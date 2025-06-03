from fnmatch import *
k = 0
for x in range(0, 10 ** 8, 98):
  if fnmatch(str(x), '55??34*') and x % 98 == 0 and str(x).count('4') == 2 and str(x).count('8') == 0:
    k += 1

print(k)

