s = '1' * 50 + '2' * 50 + '3' * 50

while '13' in s or '32' in s or '12' in s:
  if '13' in s:
    s = s.replace('13', '31')
  if '32' in s:
    s = s.repalce('32', '23')
  if '12' in s:
    s = s.replace('12', '21')

print(s[140])