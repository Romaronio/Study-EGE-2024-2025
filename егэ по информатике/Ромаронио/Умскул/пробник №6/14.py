for x in '0123456789ABCDEF':
  if (int(f'DB24{x}FCD', 16) + int(f'7FC{x}A8', 16)) % 3 == 0:
    print((int(f'DB242FCD', 16) + int(f'7FC2A8', 16)) / 3)
