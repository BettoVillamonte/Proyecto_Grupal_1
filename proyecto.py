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

        
def hablidad_pokemon(habilidad):
    url = "https://pokeapi.co/api/v2/ability/" + habilidad
    r = requests.get(url)
    data = r.json()

    for ver in data['pokemon']:
        nom_pok = ver['pokemon']['name']
        list_nom_hab_fot(nom_pok)


def habitat_pokemon(habitat):
    url = "https://pokeapi.co/api/v2/pokemon-habitat/" + habitat
    r = requests.get(url)
    data = r.json()

    for ver in data['pokemon_species']:
        nom_pok= ver['name']
        list_nom_hab_fot(nom_pok)

        
def tipo_pokemon(tipo):
    url = "https://pokeapi.co/api/v2/type/" + tipo
    r = requests.get(url)
    data = r.json()
    for ver in data['pokemon']:
        nom_pok=ver['pokemon']['name']
        list_nom_hab_fot(nom_pok)
        
 
def menu():
    os.system('cls')
    print("Selecciona una opción")
    print("\t1 Listar pokemons por generación")
    print("\t2 Listar pokemons por forma")
    print("\t3 Listar pokemons por habilidad")
    print("\t4 Listar pokemons por habitat")
    print("\t5 Listar pokemons por tipo")
    print("\t6 - salir")

  

        
     