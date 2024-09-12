import turtle
from turtle import Turtle
timmy=Turtle()
new_screen=turtle.Screen()
new_screen.listen()
def f():
	timmy.forward(10)
def a_l():
	timmy.left(10)
def a_r():
	timmy.right(10)
def b():
	timmy.backward(10)


turtle.onkeypress(a_l,"A")

turtle.onkeypress(f, "W")

turtle.onkeypress(b, "S")

turtle.onkeypress(a_r, "D")



new_screen.exitonclick()