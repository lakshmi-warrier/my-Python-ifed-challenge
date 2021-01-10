import PySimpleGUI as sg
import pokedex as pd

# Define the window's contents
layout = [[sg.Text("Name of the pokemon")],     # Part 2 - The Layout
          [sg.Input()],
          [sg.Button('Ok')],
        ]

# Create the window
window = sg.Window('Pokedex', layout)
# Display and interact with the Window
event, values = window.read()

pokemon = values[0].lower()
print('Pokemon: ', pokemon)

poke_type = pd.get_type(pokemon)


poke_type_column = [
    [sg.Text(poke_type)],

    [sg.Text(size=(40, 1), key="-TOUT-")],
]

menu = [[sg.Column(poke_type_column)]]
window = sg.Window('Pokedex', menu)
event, values = window.read()



# Finish up by removing from the screen
window.close()
