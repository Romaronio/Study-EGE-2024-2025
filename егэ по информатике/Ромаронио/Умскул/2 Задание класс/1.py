def vozrast(born_year, new_year):
	print(new_year - born_year)
# year = {'born_year': 2000, 'new_year': 2024}
# vozrast(**year)
keys = ['born_year', 'new_year']
val = [2000, 2024]
s = dict(zip(keys, val))
print(s)