x = 100_000_000
def dev(x):
  d = set()
  for i in range(1, int(x ** 1/2) + 1):
    if x % i == 0:
      d.add(i)
      d.add(x//i)
  return sorted(d)
delite = dev(x)
print(delite)











































