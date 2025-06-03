def three(x):
    s = ''
    while x:
        s = str(x % 3) + s
        x = x // 3
    return s

for n in range(1, 1000):
    s = three(n)
    if n % 3 == 0:
        s = '121' + s[2:]
    else:
        s = s + '12'
    if int(s, 3) > 800:
        print(n, int(s, 3))