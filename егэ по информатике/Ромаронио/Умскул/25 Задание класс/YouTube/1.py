x = 14 ** 3

def f(x):
  mas = [x]
  for i in range(1, x + 1):
    if x ** 1/2 % i == 0:
      mas.append(i)
  return mas
print(f(x))