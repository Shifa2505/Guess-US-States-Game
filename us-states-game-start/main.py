import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# to get the x and y values of the state and log in to the csv file
# def get_mouse_click_coor(x, y):
#     print(x, y)
#
#
# turtle.onscreenclick(get_mouse_click_coor)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 guessed right.", prompt="What's another State's name?").title()
    print(answer_state)

    # if answer_state == to one of the state in 50_states.csv.
    #     if right:
    #         print the state at proper x and y coor

    if answer_state == "Exit":
        not_guessed_states = []
        for state in all_states:
            if state not in guessed_states:
                not_guessed_states.append(state)
        print(not_guessed_states)
        new_data = pandas.DataFrame(not_guessed_states)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer_state in all_states:
        print("right")
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)
        guessed_states.append(answer_state)

# turtle.mainloop()
# screen.exitonclick()

