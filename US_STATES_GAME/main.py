import turtle
import pandas


screen = turtle.Screen()
screen.title("U.S. States game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


''' HOW TO GET X,Y COOR BY CLICK:------------------
def get_mouse_click_coor(x, y):
    print(x, y)

turtle.onscreenclick(get_mouse_click_coor)

turtle.mainloop() # CODE WILL RUN IN LOOP--OPPOSITE OF exitonclick()
'''

score = 0
answer_list = []


data = pandas.read_csv("50_states.csv")
state_name = data.state.to_list()


while score < 50:
    answer_input = screen.textinput(
        title=f"{score}/50", prompt="Enter the name of a state").title()
    if answer_input in answer_list:
        score += 0

    else:
        if answer_input in state_name:
            answer_list.append(answer_input)
            t = turtle.Turtle()
            score += 1
            state_data = data[data.state == answer_input]
            t.ht()
            t.pu()
            t.goto(int(state_data.x), int(state_data.y))
            t.write(answer_input)

        else:
            score += 0

turtle.write("YOU WIN !!", align="center", font=("Arial", 16, "bold"))
screen.exitonclick()
