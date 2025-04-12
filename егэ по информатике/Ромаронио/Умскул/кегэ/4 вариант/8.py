from itertools import *
k = 0
for i in product(['Q', 'W', 'E', 'R', 'T', 'Y', 'N', 'O'], repeat=7):
  s = ''.join(i)
  if 'QWERTY' in s:
    continue
  if s.count('Q') > 2:
    continue
  if s.count('W') > 2:
    continue
  if s.count('E') > 2:
    continue
  if s.count('R') > 2:
    continue
  if s.count('T') > 2:
    continue
  if s.count('Y') > 2:
    continue
  if s.count('N') > 2:
    continue
  if s.count('O') > 2:
    continue
  k += 1
print(k)
