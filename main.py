import turtle
import pandas

state_data = pandas.read_csv("50_states.csv")


list_of_states = state_data.state.tolist()
states_guessed = 0
correct_guesses = []
game_start = True

screen = turtle.Screen()
screen.title("U.S. States Game")
screen.setup(width=725, height=491)
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

while states_guessed < len(list_of_states):
    answer_state = screen.textinput(title= f"States Guessed: {states_guessed}/50",
                                    prompt="Guess a state:").title()
    if answer_state == "Exit":
        missing_states = [state for state in list_of_states if state not in correct_guesses]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    for state in list_of_states:
        if answer_state in correct_guesses:
            pass
        elif answer_state == state:
            location_x = int(state_data[state_data.state == answer_state].x.iloc[0])
            location_y = int(state_data[state_data.state == answer_state].y.iloc[0])
            new_state = turtle.Turtle()
            new_state.hideturtle()
            new_state.penup()
            new_state.goto(location_x, location_y)
            new_state.write(arg= answer_state, font=("Arial", 6, "bold"), align="left")
            states_guessed += 1
            correct_guesses.append(state)


