import requests, json

def get_type(pokemon):
    '''    
    Gets the type of Pokemon

    PARAMETERS:
    -------------
    pokemon: string
    
    RETURNS:
    -------------
    type of Pokemon - str
    
    '''

    url = 'https://pokeapi.co/api/v2/pokemon/'+pokemon
    response = requests.get(url)

    name = response.json()['species']['name']
    print(name)

    poke_type = response.json()['types'][0]['type']['name']
    print(poke_type)
    return str(poke_type)


def damage_from(url):
    response = requests.get(url)

    '''
    ##Add a for loop here - for more than 1 type
    '''
    types = response.json()['types']
    for i in range(len(types)):
        url = types[i]['type']['url']

        response= requests.get(url)
        dam_rel = response.json()['damage_relations']

        #extracting every key with substring damage_from, except no_damage_from
        damage_list = [value for key, value in dam_rel.items() if ('damage_from' in key and 'no' not in key)]
        # damage_from is a list of lists

        for damage_from in damage_list:
            #iterating through lists
            for damage in damage_from:
                #damage - dictionary
                print(damage['name'])