
def Del(x):
    s = set()
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            s.add(x // i)
            s.add(i)
    return sorted(s)

for x in range(100_000, 100_100):
    if len(Del(x)) == 0:
        continue
    if (max(Del(x)) + min(Del(x))) % 11 == 0:
        print(x, max(Del(x)) + min(Del(x)))