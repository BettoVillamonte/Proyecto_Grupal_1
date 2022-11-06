
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
            
            
            

