f = open('17.txt')
vse_chisla = []
chet = []
k = 0
mod_raz = []
for s in f:
  s = int(s)
  vse_chisla.append(s)
  if s % 2 == 0:
    chet.append(s)

cr_znach = sum(vse_chisla) / len(vse_chisla)

for i in range(len(vse_chisla) - 1):
  if vse_chisla[i] > cr_znach or vse_chisla[i - 1] > cr_znach:
    if '11' in str(vse_chisla[i]) or '11' in str(vse_chisla[i - 1]):
      k += 1
      mod_raz.append(abs(vse_chisla[i] - vse_chisla[i - 1]))

print(k, max(mod_raz))

