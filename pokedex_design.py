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

url = 'https://pokeapi.co/api/v2/pokemon/'+pokemon

poke_type = pd.get_type(url)
damage_from = pd.damage_from(url)
new_url = ['https://pokeapi.co/api/v2/pokemon/type/'+i for i in damage_from]
print(new_url)
poke_type_column = [
    [sg.Text("Type: "+poke_type.capitalize())],
    [sg.Text("Damage from: "+"".join(damage_from).capitalize())],
    #[sg.Text("Attackers: "+"".join(pd.get5_attackers(new_url[0])).capitalize())],

    [sg.Text(size=(40, 1), key="-TOUT-")],
]

menu = [[sg.Column(poke_type_column)]]
window = sg.Window('Pokedex', menu)
event, values = window.read()



# Finish up by removing from the screen
window.close()
