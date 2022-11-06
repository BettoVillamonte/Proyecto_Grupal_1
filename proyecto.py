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
