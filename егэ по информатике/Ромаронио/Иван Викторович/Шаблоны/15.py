def f(x, y): #создаем вункцию которая проверяет условие
	return(x * y < a) or (x < y) or (9 < x)
for a in range(10000): #делаем перебор значений а
	if all(f(x, y) for x in range(1000) for y in range(1000)): # при этом а проверяем какие в каком случае выражение выдаст true или единицу
		print(a) # выводим это значение а
		break