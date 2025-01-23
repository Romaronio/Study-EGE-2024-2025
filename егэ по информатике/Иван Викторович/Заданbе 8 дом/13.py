from itertools import product
print([''.join(i) for i in product('акру', repeat=5)].index('укара') + 1)