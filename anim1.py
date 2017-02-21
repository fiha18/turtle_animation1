import turtle

window=turtle.Screen()
window.bgcolor("blue")
bro=turtle.Turtle()
bro.color("greenyellow")
for i in range(1,37):
	bro.right(10)
	for j in range(1,5):
		bro.forward(100)
		bro.right(90)
		bro.speed(0)


angi=turtle.Turtle()
angi.shape("classic")
angi.color("red")
for i in range(1,37):
	angi.right(10)
	for j in range(1,5):
		angi.forward(70.7)
		angi.right(90)
		angi.speed(0)
par=turtle.Turtle()
par.shape("classic")
par.color("green")
for i in range(1,37):
	par.right(10)
	for j in range(1,5):
		par.forward(50)
		par.right(90)
		par.speed(0)
car=turtle.Turtle()
car.shape("classic")
car.color("yellow")
for i in range(1,37):
	car.right(10)
	for j in range(1,5):
		car.forward(35.35)
		car.right(90)
		car.speed(0)
mar=turtle.Turtle()
mar.shape("classic")
mar.color("wheat")
for i in range(1,37):
	mar.right(10)
	for j in range(1,5):
		mar.forward(25)
		mar.right(90)
		mar.speed(0)

window.exitonclick()
