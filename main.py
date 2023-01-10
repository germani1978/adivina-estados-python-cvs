import pandas
import turtle

screen = turtle.Screen()
screen.title('U.S.A.')
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv('50_states.csv')
all_state = data.state.to_list()


mising_states = []
guessed_states = []
while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f'Estados {len(guessed_states)}/50', prompt='Cual es el nombre del estado').title() #capitalizar
    if answer_state == 'Exit':
        for state in all_state:
            if not state in guessed_states:
                mising_states.append(state)
                
        new_data = pandas.DataFrame(mising_states)
        new_data.to_csv('states_unknow.csv')
        break
    if answer_state in all_state:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)

