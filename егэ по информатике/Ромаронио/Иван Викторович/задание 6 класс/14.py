from turtle import *
tracer(0)
left(90)
k = 20
x = 3
screensize(5000, 5000)
forward(2 * k)
for _ in range(5):
	forward(x * k)
	right(90)
	forward(3 * k)
	right(90)
	forward(x * k)
	left(90)
	forward(1 * k)
	left(90)
back(2 * k)
pu()
for x in range(-40, 40):
	for y in range(-40, 40):
		goto(x * k, y * k)
		dot(3)
done()

for x in range(10000, 1, -1):
	if (x + 1) * 2 * 5 +  2 * 4 + 1 < 25000:
		print(x)
		break