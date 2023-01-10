import random
import pandas
import turtle

screen = turtle.Screen()
screen.title('U.S.A.')
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv('50_states.csv')
all_state = data.state.to_list()

names = ['Juan','Pedro','Susana','Luis']
puntuacion = { name: random.randint(1,100) for name in names}
students = { student:score for (student, score) in puntuacion.items() if score > 60  }
print(puntuacion)
print(puntuacion.items())

mising_states = []
guessed_states = []
while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f'Estados {len(guessed_states)}/50', prompt='Cual es el nombre del estado').title() #capitalizar
    if answer_state == 'Exit':
        mising_states = [ state for state in all_state if not state in guessed_states ]
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

