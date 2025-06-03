from turtle import *
left(90)
k = 20
screensize(5000, 5000)
tracer(0)

for _ in range(24):
  forward(3 * k)
  left(60)

pu()
for x in range(-40, 40):
  for y in range(-40, 40):
    goto(x * k, y * k)
    dot(3)

done()