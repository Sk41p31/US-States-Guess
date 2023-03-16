import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")

image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)


def update_score(score):
    new_turtle = turtle.Turtle()
    new_turtle.ht()
    new_turtle.color("black")
    new_turtle.penup()
    new_turtle.goto(0, 250)
    new_turtle.write(f"Score: {score}/50", move=False, align="center", font=("Courier", 12, "normal"))
    return new_turtle


def reveal_state_name(state):
    new_x = state.x.to_list()[0]
    new_y = state.y.to_list()[0]
    name = state.state.to_list()[0]
    new_turtle = turtle.Turtle()
    new_turtle.ht()
    new_turtle.color("black")
    new_turtle.penup()
    new_turtle.goto(new_x, new_y)
    new_turtle.write(f"{name}", move=False, align="center", font=("Courier", 12, "normal"))


data = pandas.read_csv("50_states.csv")
states = data.state.to_list()
states_guessed = []
old_score = turtle.Turtle()


continue_game = True

while continue_game:
    answer_state = screen.textinput(title="Guess The State", prompt="What's another state's name?")
    answer_state = answer_state.title()

    if answer_state == "Exit":
        break
    if answer_state in states:
        reveal_state_name(data[data.state == answer_state])
        states.pop(states.index(answer_state))
        states_guessed.append(answer_state)
        old_score.clear()
        old_score = update_score(len(states_guessed))

not_guessed = pandas.DataFrame(states)
not_guessed.to_csv("states_to_learn.csv")
