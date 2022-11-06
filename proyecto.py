

print ("MENU Registros\n\n1)-nuevo\n2)-Mostrar\n3)-Eliminar registro")
opcion = input("Elige una opcion: ")
if opcion == "1":
    print ("Nuevo registro\n")

    import csv

    archivo = open('libro_1.csv', 'a')

    id = str(input("Ingresar ID:"))
    titulo = str(input("Ingresar el titulo del libro a registrar:"))
    genero = str(input("Ingresar el genero del libro a registrar:"))
    ISBN = str(input("Ingresar el ISBN del libro a registrar:"))
    editorial = str(input("Ingresar la editorial del libro a registrar:"))
    autor_es = str(input("Ingresar el/los autor(es) del libro a registrar:"))

    print(f"Se ha ingresado: {id},{titulo},{genero},{ISBN},{editorial},{autor_es} ")
    archivo.write(id)
    archivo.write(",")
    archivo.write(titulo)
    archivo.write(",")
    archivo.write(genero)
    archivo.write(",")
    archivo.write(ISBN)
    archivo.write(",")
    archivo.write(editorial)
    archivo.write(",")
    archivo.write(autor_es)
    archivo.write(",")
    archivo.write("\n")
   
   
    archivo.close()
elif opcion == "2":
    print("Mostrar Registros\n")
    archivo = open("libro_1.csv")

    print(archivo.read())
    archivo.close()

elif opcion == "3":
    archivo = open('libro_1.csv', 'w')
    archivo.truncate()

    print ("Registros ELiminados")
    archivo.close()
else:
    print("Debes de elegir una opcion anterior")
    

# print("Generacion de Pokemos 1,2,3,4,5,6,7,8")
# print("Formas de pokemos: ball, squiggle,fish, arms, blob,upright, legs, quadruped,wings,tentacles,heads,humanoid,bug-wings,armor ")
# print("Las habilidades que poseen: stench,drizzle,speed-boost,battle-armor,sturdy,damp,limber,compound-eyes")
# print("sus habitat son: cave, forest,grassland, mountain, rare, rough-terrain, sea, urban, waters-edge")
# print ( "los tipos son: normal,fighting, flying, poison, ground, steel,rock,grass,fairy")