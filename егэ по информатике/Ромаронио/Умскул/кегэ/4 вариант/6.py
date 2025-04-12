from turtle import *
left(90)
tracer(0)
screensize(5000, 5000)
k = 30

left(15)
for _ in range(7):
  left(30)
  forward(10 * k)
  left(60)

pu()
for x in range(-40, 40):
  for y in range(-40, 40):
    goto(x * k, y * k)
    dot(3)

done()
print(7 * 14)