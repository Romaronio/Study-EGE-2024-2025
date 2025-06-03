from time import process_time_ns

for n in range(3, 10000):
    s = '7' + '2' * n
while '72' in s or '322' in s or '2222' in s:
    if '72' in s:
        s = s.replace('72', '2', 1)
    if '322' in s:
        s = s.replace('322', '27', 1)
    if '222' in s:
        s = s.replace('222', '3', 1)
    print(s.count('2') * 2 + s.count('7') * 7 + s.count('3') * 3)