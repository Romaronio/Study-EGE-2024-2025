count = 0
for i in range(1, 34000):
    a = str(oct(i))[2:]
    if (len(a) == 5) and (a.count('6') == 1):
        if a.index('6') in {0, len(a)-1} and int(a[abs(a.index('6') - 1)]) % 2 == 0:
            count += 1
        elif int(a[a.index('6')- 1]) % 2 == 0 and int(a[a.index('6') + 1]) % 2 == 0:
            count += 1
print(count)
