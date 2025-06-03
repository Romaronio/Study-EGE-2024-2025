def three(s):
    m = []  # Объявляем список внутри функции
    while s:
        m.append(s % 3)
        s = s // 3
    return m[::-1]  # Возвращаем сформированный список
for x in range(2031, 0, -1):
    s = 3 ** 100 - x
    if three(s).count(0) == 5:  # Проверяем количество нулей
        print(x)
        break