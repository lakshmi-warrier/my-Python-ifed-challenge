import requests
import json


def get_type(url):
    '''    
    Gets the type of Pokemon

    PARAMETERS:
    -------------
    url: string

    RETURNS:
    -------------
    type of Pokemon : string

    '''

    response = requests.get(url)

    name = response.json()['species']['name']
    print(name)

    poke_types = []
    poke_type_list = response.json()['types']
    for i in range(len(poke_type_list)):
        poke_types.append(poke_type_list[i]['type']['name'])
        print(poke_types)

    return ", ".join(poke_types)


def damage_from(url):
    '''    
    Gets the type of damage

    PARAMETERS:
    -------------
    url: string

    RETURNS:
    -------------
    type of damage : list

    '''
    response = requests.get(url)

    list_to_return = []

    types = response.json()['types']
    for i in range(len(types)):
        url = types[i]['type']['url']

        response = requests.get(url)
        dam_rel = response.json()['damage_relations']

        # extracting every key with substring damage_from, except no_damage_from
        damage_list = [value for key, value in dam_rel.items() if (
            'damage_from' in key and 'no' not in key)]
        # damage_from is a list of lists

        for damage_from in damage_list:
            # iterating through lists
            for damage in damage_from:
                #damage - dictionary
                list_to_return.append(damage['name'])
                print(damage['name'])
    return list_to_return


def get5_attackers(url):
    response = requests.get(url)

    print("Double damage from:")
    double_dam_url = []
    dam_rel = response.json()['damage_relations']

    for dam in range(len(dam_rel['double_damage_from'])):
        double_dam_url.append(dam_rel['double_damage_from'][dam]['url'])
        print(dam_rel['double_damage_from'][dam]['name'])
    print((double_dam_url[0]))

    attackers = []
    for dam_url in double_dam_url:
        response = requests.get(dam_url)
        pokemon = response.json()['pokemon']
        for ind in range(5):
            attackers.append(pokemon[ind]['pokemon']['name'])
            print(pokemon[ind]['pokemon']['name'])

    return attackers
