for x in '0123456789':
  for y in '0123456789':
    if int(f'23{x}456{y}89') % 17 == 0:
      print(int(f'23{x}456{y}89'), int(f'23{x}456{y}89') / 17)
