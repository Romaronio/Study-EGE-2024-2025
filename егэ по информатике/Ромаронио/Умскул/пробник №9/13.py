for x in '0123456789AB':
    if (int(f'32D{x}', 16) + int(f'43{x}B', 12)) % 15 == 0:
        print(x)

print((int(f'32D4', 16) + int(f'434B', 12)))