from turtle import *
k = 20
tracer(0)
left(90)
screensize(5000, 5000)

for _ in range(4):
  forward(3 * k)
  right(90)
  forward(3 * k)
  right(90)
  forward(1 * k)
  right(90)
  forward(1 * k)
  right(90)

pu()
for x in range(-40, 40):
  for y in range(-40,40):
    goto(x * k, y * k)
    dot(3)
done()
























