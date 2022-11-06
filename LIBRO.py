
from typing import List

from Book import *


class Biblioteca:


    def __init__(self):
        self._books = []
        self._file_name = None

    @property
    def file_name(self):
        return self._file_name

    @file_name.setter
    def file_name(self, value):
        self._file_name = value

    def load_book_line_by_line(self, file_name):
        print("== Lectura desde disco duro ==")
        archivo = open(file_name)
        self._file_name = file_name
        lines = archivo.readlines()
        self._books.clear()
        for line in lines:
            book_temp = Book(1, "", "", "", "", "")
            array = line.split(',')
            count_column = 0
            for item in array:
                if count_column == 0:
                    book_temp.id = item
                elif count_column == 1:
                    book_temp.title = item
                elif count_column == 2:
                    book_temp.genre = item
                elif count_column == 3:
                    book_temp.editorial = item
                elif count_column == 4:
                    book_temp.isbn = item
                elif count_column == 5:
                    book_temp.authors = item
                else:
                    book_temp.authors += ',' + item
                count_column += 1
            book_temp.print()
            self._books.append(book_temp)

            

    def create_book(self):
        print(" == Registro de Libro ==")
        book2 = Book(1, "", "", "", "", "")
        id = input("Ingresar ID: ")
        title = input("Ingresar titulo: ")
        genre = input("Ingresar Genero: ")
        editorial = input("Ingresar editorial: ")
        isbn = input("Ingresar el ISBN: ")
        authors = input("Ingresar autor(es): ")
        book2.create_book(int(id), title, genre, isbn, editorial, authors)
        print("libro registrado con exito")
        book2.print()
        self._books.append(book2)
            


    def listar(self):
        print("== Listado de libros ==")
        for book in self._books:
            book.print()

    def eliminar(self, id_eliminar):
        print("== Eliminando libro ==")
        found = -1
        position = 0
        for book in self._books:
            if book.id == int(id_eliminar):
                found = position
            position += 1
        if found != -1:
            del self._books[found]
            print("Libro eliminado con exito")


    def buscar_por_isbn_titulo(self):
        print("Busqueda por ISBN o por titulo")
        opcion = int(input("Ingrese 1 para buscar por ISBN o 2 para buscar por titulo: "))
        if opcion == 1:
            texto_buscar = input("Ingresa el ISBN a buscar: ")
            self.print_collection(self.busqueda_tipo(opcion, texto_buscar))
        elif opcion == 2:
            texto_buscar = input("Ingrese el titulo a buscar: ")
            self.print_collection(self.busqueda_tipo(opcion, texto_buscar))
        else:
            print("Opcion de busqueda invalida")

            

    def buscar_por_otros(self):
        print("== Busqueda por autor(es), genero, editorial ==")
        opcion = int(
            input("Ingrese 1 para buscar por autor(es), 2 para buscar por genero o 3 para buscar por editorial: "))
        if opcion == 1:
            texto_buscar = input("Ingresa los autor(es) a buscar: ")
            self.print_collection(self.busqueda_tipo(3, texto_buscar))
        elif opcion == 2:
            texto_buscar = input("Ingrese el genero a buscar: ")
            self.print_collection(self.busqueda_tipo(4, texto_buscar))
        elif opcion == 3:
            texto_buscar = input("Ingrese la editorial a buscar: ")
            self.print_collection(self.busqueda_tipo(5, texto_buscar))
        else:
            print("Opcion de busqueda invalida")
            
    def busqueda_tipo(self, tipo_busqueda, texto_a_buscar):
        libros_encontrados: List[Book] = []
        for book in self._books:
            if tipo_busqueda == 1:
                if texto_a_buscar.lower() in book.isbn.lower():
                    libros_encontrados.append(book)
            if tipo_busqueda == 2:
                if texto_a_buscar.lower() in book.title.lower():
                    libros_encontrados.append(book)
            if tipo_busqueda == 3:
                if texto_a_buscar.lower() in book.authors.lower():
                    libros_encontrados.append(book)
            if tipo_busqueda == 4:
                if texto_a_buscar.lower() in book.genre.lower():
                    libros_encontrados.append(book)
            if tipo_busqueda == 5:
                if texto_a_buscar.lower() in book.editorial.lower():
                    libros_encontrados.append(book)
            if tipo_busqueda == 6:
                if texto_a_buscar == book.id:
                    libros_encontrados.append(book)
            if tipo_busqueda == 7:
                if book.cant_autores == int(texto_a_buscar):
                    libros_encontrados.append(book)
        return libros_encontrados

    
    
    
    def edit_book(self):
        libro_id = int(input("Ingrese el ID del libro a modificar: "))
        libros_encontrados = self.busqueda_tipo(6,libro_id)
        libro_a_modificar = libros_encontrados[0]
        title = input("Ingresar titulo: ")
        genre = input("Ingresar Genero: ")
        editorial = input("Ingresar editorial: ")
        isbn = input("Ingresar el ISBN: ")
        authors = input("Ingresar autor(es): ")
        libro_a_modificar.update(title, genre, editorial, isbn, authors)
        print("Libro actualizado con exito")
        libro_a_modificar.print()

    def save_all(self):
        print("== Guardado con exito ==")
        archivo = open(self._file_name, 'r+')
        archivo.truncate(0)
        for libro in self._books:
            archivo.write(str(libro.id))
            archivo.write(",")
            archivo.write(libro.title)
            archivo.write(",")
            archivo.write(libro.genre)
            archivo.write(",")
            archivo.write(libro.editorial)
            archivo.write(",")
            archivo.write(libro.isbn)
            archivo.write(",")
            archivo.write(libro.authors)
        archivo.close()

    def busqueda_cant_autores(self):
        print("== Busqueda por  cantidad de autores ==")
        texto_a_buscar = int(input("Ingrese la cantidad de autores a buscar: "))
        self.print_collection(self.busqueda_tipo(7, texto_a_buscar))    

    def ordenar_libros(self):
        print(" == Ordenar libros por Titulo ==")
        libros_por_ordenar: List[Book] = self._books
        libros_ordenados = sorted(libros_por_ordenar, key =lambda i: i.title)
        self._books = libros_ordenados
        print("Ordenamiento realizado con exito")
        self.listar()


    def print_collection(self, listaLibros:List[Book]):
        for libro in listaLibros:
            libro.print()

if __name__ == "__main__":
    biblioteca1 = Biblioteca()

    def run_program():
        print("Bievenido a mi pograma:")
        print("-" * 10, "Menú", "-" * 10)
        print("1) Leer archivo de disco duro (.txt o csv) que cargue 3 libros.\n"
              "2) Listar libros.\n"
              "3) Agregar libro.\n"
              "4) Eliminar libro.\n"
              "5) Buscar libro por ISBN o por título.\n"
              "6) Ordenar libros por título.\n"
              "7) Buscar libros por autor, editorial o género.\n"
              "8) Buscar libros por número de autores.\n"
              "9) Editar o actualizar datos de un libro (título, género, ISBN, editorial y autores).\n"
              "10) Guardar libros en archivo de disco duro (.txt o csv)")
        option = input("Ingrese una de estas opciones: ")
         

        if option == "1":
            file_name = input("Ingrese nombre de archivo + extension (Ejemplo: libro_1.csv) : ")
            biblioteca1.load_book_line_by_line(file_name)
        elif option == "2":
            biblioteca1.listar()
        elif option == "3":
            biblioteca1.create_book()
        elif option == "4":
            id = input("Ingresar ID a eliminar: ")
            biblioteca1.eliminar(id)
        elif option == "5":
            biblioteca1.buscar_por_isbn_titulo()
        elif option == "6":
            biblioteca1.ordenar_libros()
        elif option == "7":
            biblioteca1.buscar_por_otros()
        elif option == "8":
            biblioteca1.busqueda_cant_autores()
        elif option == "9":
            biblioteca1.edit_book()
        elif option == "10":
            biblioteca1.save_all()
        x = "y"
            
