import random
import turtle
from turtle import Turtle


new_screen=turtle.Screen()
new_screen.setup(width=500,height=400)
colors=["brown","red","green","yellow","orange","blue"]
angles=[-100,-50,0,50,100]
velocity=[0,10,20,30,40]


bet=new_screen.textinput(title= "Make a bet", prompt= "Which color is going to win?")
bet=bet.lower()
c=0
turtles=[]
race=True
for n in angles:
    animal=Turtle()
    animal.color(colors[c])

    animal.shape("turtle")
    animal.penup()
    animal.goto(-250,n)
    turtles.append(animal)
    c+=1
while race is True:


    for n in turtles:
        random_velocity=float(random.choice(velocity))
        n.forward(random_velocity)

        if n.xcor() >= 200:
            race = False

            winning_turtle=n.color()[0]


            if bet==winning_turtle:
                print(f"You won! The {winning_turtle} turtle is the fastest!")
            else:
                print(f"Oh... The winner is the {winning_turtle} turtle.")


new_screen.exitonclick()




winning_animal=animal.color()[0]


