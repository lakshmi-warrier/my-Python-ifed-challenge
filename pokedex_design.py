from typing import Text
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
window.close()

url = 'https://pokeapi.co/api/v2/pokemon/'+pokemon

poke_type = pd.get_type(url)
damage_from = pd.damage_from(url)[0]

new_url = [i for i in pd.damage_from(url)[1]]
#attacker_dict = pd.get5_attackers(new_url)
print(new_url)
poke_column = [
    [sg.Text("Type: "+poke_type.capitalize())],
    [sg.Text("Damage from: "+", ".join(damage_from).capitalize())],
    [sg.Text("Attackers: ")],
    [sg.Text((pd.get5_attackers(i))) for i in new_url],

    #[sg.Text(size=(40, 1), key="-TOUT-")],
]

menu = [[sg.Column(poke_column)]]
window = sg.Window('Pokedex', menu)
event, values = window.read()

window.close()

