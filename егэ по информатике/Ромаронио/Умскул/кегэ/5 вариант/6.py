from turtle import *
tracer(0)
left(90)
k = 20
screensize(-5000, 5000)
x = 0
y = 0
for _ in range(10):
  goto((x + 3) * k, (y - 4) * k)
  goto((x - 7) * k, (y + 24) * k)
  goto((x + 12) * k, (y + 5) * k)
pu()
for x in range(-40, 40):
  for y in range(-40, 40):
    goto(x * k, y * k)
    dot(3)

done()


