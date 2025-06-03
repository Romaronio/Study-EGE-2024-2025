f = open('17.txt')
mas = [int(s.strip()) for s in f]
res = []
k = 0
max_sum = 0

for i in range(len(mas) - 1):
  num1, num2 = mas[i], mas[i + 1]
  if num1 % 2 == 1 and num2 % 2 == 1:
    k += 1
    current_sum = num1 + num2
    if max_sum < current_sum:
      max_sum = current_sum


print(k, max_sum)



