for n in range(1, 1000):
  s = '>' + '2' * n + '4' * 54 + '8' * 33

  while '>2' in s or '>4' in s or '>8' in s:
    if '>2' in s:
      s = s.replace('>2', '28>', 1)
    if '>4' in s:
      s = s.replace('>4', '22>8', 1)
    if '>8' in s:
      s = s.replace('>8', '244>', 1)
  if s.count('2') * 2 + s.count('4') * 4 + s.count('8') * 8 >= 10000:
    print(n, s)
    break