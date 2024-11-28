import turtle
from turtle import Turtle, Screen
import random
traduceri_culori = {
    "red": "rosie",
    "orange": "portocalie",
    "yellow": "galbena",
    "green": "verde",
    "blue": "albastra",
    "purple": "mov",
}

# Funcție pentru traducerea unei culori
def traduce_culoare(culoare_engleza):
    return traduceri_culori.get(culoare_engleza, culoare_engleza)
is_race_on = False
screen = Screen()
screen.setup(700, 600)
user_bet = screen.textinput(title="Pariaza", prompt="Ce broasca va castiga? Alege culoarea: ")
colors = ["red", "orange" , "yellow", "green", "blue", "purple"]
y_position = [240, 160, 80, 0, -80, -160]
all_turtles=[]

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-320, y=y_position[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on =True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 310:
            is_race_on = False
            wincolor = turtle.pencolor()
            if wincolor == user_bet:
                print(f"Ai castigant !  broasca {traduce_culoare(wincolor)} a ajuns prima !")
            else:
                print(f"Ai pierdut !  broasca {traduce_culoare(wincolor)} a ajuns prima !")
        random_dist=random.randint(0, 10)
        turtle.forward(random_dist)



screen.exitonclick()