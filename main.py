import pandas

import turtle
from turtle import Turtle, Screen

screen = Screen()
screen.title("U.S state guessing game")

image = 'blank_states_img.gif'


screen.addshape(image)
bg_image = Turtle()
bg_image.shape(image)


# def get_mouse_click_coor(x, y):
#     print(x,y)

# when we click on screen the turtle.onscreenclick method will pass the corrdinates of
# our click to the methods get_mouse_click_coor() this way we will get the coordinates of our click

# turtle.onscreenclick(get_mouse_click_coor)
#
# # this is an alternativeway of  scree.exitonclick
# turtle.mainloop()

#

#  from csv and read all the coordinates



data = pandas.read_csv('50_states.csv')
# print(data[data.state == answer_state])
state_list = data['state'].to_list()
# print(state_list)
print(len(state_list))
correct_guess=[]
points = 0
game_is_on = True


while game_is_on:


    answer_state = screen.textinput(title=f'{points} / 50 States Correct', prompt='What is the another states name')
    answer_state = answer_state.title()

    if answer_state == "Exit":
        missing_states = []
        missing_states = [state for state in state_list if state not in correct_guess]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn")
        game_is_on = False



    if answer_state in state_list and answer_state not in  correct_guess:





        cor = data[data.state == answer_state]
        x_cor = int(cor.x)
        y_cor = int(cor.y)
        # print(x_cor, y_cor)
        new_state = Turtle()
        new_state.hideturtle()
        new_state.penup()
        new_state.goto(x_cor, y_cor)
        new_state.write(answer_state, align='center', font=('Arial', 8, 'normal'))
        points += 1
        correct_guess.append(answer_state)


screen.exitonclick()