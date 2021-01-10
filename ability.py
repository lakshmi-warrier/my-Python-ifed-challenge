import requests

def ability(pokemon):
    response = requests.get('https://pokeapi.co/api/v2/pokemon/'+pokemon)
    abilities = response.json()['abilities']

    ablility_list = []
    for ind in range(len(abilities)):
        ablility_list.append(abilities[ind]['ability']['name'])
    return ablility_list

