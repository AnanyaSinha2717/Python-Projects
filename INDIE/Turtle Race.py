from turtle import Turtle, Screen
import random

race_on=False
screen=Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your Bet", prompt='Which turtle will win the race?')
colors=['red', 'yellow', 'green', 'purple', 'blue', 'orange']

all_turtles=[]

y= -75
for i in range(6):
    t=Turtle()
    t.shape("turtle")
    t.pu()
    t.color(colors[i])
    t.goto(-230, y)
    y+=30
    all_turtles.append(t)

if user_bet:
    race_on=True

while race_on==True:

    for t in all_turtles:
        if t.xcor() > 230:
            race_on = False
            win = t.pencolor()
            
            if win==user_bet:
                print(f"You won. {win} turtle wins the race.")
            else:
                print(f'You lost. {win} turtle wins the race.')

        t.fd(random.randint(1, 10))

screen.exitonclick()