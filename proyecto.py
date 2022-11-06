import os

import requests



def list_nom_hab_fot(nom_pok):

    url = "https://pokeapi.co/api/v2/pokemon/" + nom_pok
    r = requests.get(url)
    if r.status_code == 404:
        pass
    else:
        habilidad = r.json()
        print(f"Nombre : {nom_pok}")
        for foton in habilidad['sprites']['other']['official-artwork'].values():
            print(foton)
            print("Sus Habilideades son :")
            for s in habilidad['abilities']:
                print(f"\t{s['ability']['name'].capitalize()} ")
        print("")

def generacion_pokemon(generacion):
    url = "https://pokeapi.co/api/v2/generation/" + generacion
    r = requests.get(url)
    data = r.json()

    print(f"La Generacion # {generacion} es : {data['main_region']['name']}")
    for a in data['pokemon_species']:
        nom_pok = a['name']
        list_nom_hab_fot(nom_pok)


def forma_pokemon(forma):
    url = "https://pokeapi.co/api/v2/pokemon-shape/" + forma
    r = requests.get(url)
    data = r.json()

    for a in data['pokemon_species']:
        nom_pok = a['name']
        list_nom_hab_fot(nom_pok)
