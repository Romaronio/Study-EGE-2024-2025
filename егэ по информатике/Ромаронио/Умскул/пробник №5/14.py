for x in '0123456789ABCDEF':
  if (int(f'D49{x}1', 16) + int(f'48A3{x}', 16)) % 14 == 0:
    print(x, (int(f'D49D1', 16) + int(f'48A3D', 16)) // 14)