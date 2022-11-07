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

  
while True:
    menu()
    opcionMenu = input("Ingrese un numero  -> ")
        
     
        
    if opcionMenu == "1":
        print("")
        print("Has pulsado la opción 1...")
#Sugerencias
        print("\t     Generaciones : 1,2,3,4,5,6,7,8")
        pokemon = int(input("Ingrese Generacion :"))

        if pokemon >8 or pokemon==0:
            print("Esa generacion no existe")
        else:
            generacion_pokemon(str(pokemon))

    elif opcionMenu == "2":
        print("")
        print("Has pulsado la opción 2...")
#Sugerencias
        pokemon = input("Ingrese Forma :")
        forma_pokemon(pokemon)

    elif opcionMenu == "3":
        print("")
        print("Has pulsado la opción 3...")
#Sugerencias
        pokemon = input("Ingrese Habilidad :")
        hablidad_pokemon(pokemon)
    elif opcionMenu == "4":
        print("")
        print("Has pulsado la opción 4...")
# Sugerencias
        pokemon = input("Ingrese Habitat :")
        habitat_pokemon(pokemon)

    elif opcionMenu == "5":
        print("")
        print("Has pulsado la opción 5...")
# Sugerencias
        pokemon = input("Ingrese Tipo :")
        tipo_pokemon(pokemon)
    elif opcionMenu == "6":
        break
    else:
        print("")
        input("No has pulsado ninguna opción correcta...\nda Enter para volver al Menu")
        print("")
        
 
