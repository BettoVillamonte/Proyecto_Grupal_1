class libro():
    def __init__(self,id,título,género,ISBN,editorial,autor):
        self.id=id
        self.título = título
        self.género = género
        self.ISBN = ISBN
        self.editorial = editorial
        self.autor = autor



print("Opción 1: Leer libro\n")
print("Opción 2: Listar libros\n")
print("Opción 3: Agregar libro\n")
print("Opción 4: Eliminar libro\n")
print("Opción 5: Buscar libro por ISBN o título\n")
print("Opción 6: Ordenar libros por titulo\n")
print("Opción 7: Buscar libros por autor, editorial o género\n")
print("Opción 8: Buscar libros numero de autores\n")
print("Opción 9: Modificar datos de un libro\n")
print("Opción 10: Guardar libros\n")


import csv

libros_db = "datos.csv"


def Listado():
    with open(libros_db) as csv_file:
        csv_iterable = csv.DictReader(csv_file)

        for row in csv_iterable:
            print(row['id'], ",", row['titulo'], ",", row['genero']
                  , ",", row['isbn'], ",", row['editorial'], ",", row['autores'])
            
def listarlibros():
    with open(libros_db) as csv_file:
        csv_iterable = csv.DictReader(csv_file)

        print("Estos son los Libros")
        for row in csv_iterable:
            print(row['titulo'])

Listado()
listarlibros() 

