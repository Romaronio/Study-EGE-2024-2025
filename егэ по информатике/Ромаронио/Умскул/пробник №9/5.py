def seven(x):
    s = ''
    while x:
        s = str(x % 7) + s
        x = x // 7
    return s

mas = []

for n in range(1, 1000):
    s = seven(n)
    if n % 5 == 0:
        s = '4' + s[1:] + '1'
    else:
        s = s.replace('3', '2') + '6'
    if int(s, 7) > 509:
        mas.append(int(s, 7))

print(min(mas))