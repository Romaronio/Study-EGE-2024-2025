from itertools import product
print([''.join(i) for i in product('аоу', repeat = 5)].index('уауау') + 1)