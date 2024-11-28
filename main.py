from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forward():
    tim.forward(15)
def move_back():
    tim.backward(15)
def move_left():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)
def move_right():
    tim.right(10)
def clear_screen():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.listen()
screen.onkey(move_forward,"w")
screen.onkey(move_back,"s")
screen.onkey(move_left,"a")
screen.onkey(move_right,"d")
screen.onkey(clear_screen,"c")
screen.exitonclick()
