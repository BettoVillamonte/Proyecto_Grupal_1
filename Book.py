class Book:

    def __init__(self, id, title, genre, isbn, editorial, authores):
        self._id = id
        self._title = title
        self._genre = genre
        self._isbn = isbn
        self._editorial = editorial
        self._authors = authores
        self._cant_autores = 0

    def create_book(self, id, title, genre, isbn, editorial, authores):
        self.id = id
        self.title = title
        self.genre = genre
        self.isbn = isbn
        self.editorial = editorial
        self.authors = authores

    @property
    def cant_autores(self):
        return self._cant_autores

    @cant_autores.setter
    def cant_autores(self, value):
        self._cant_autores = value

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, nuevo):
        if int(nuevo) < 0:
            print("El ID debe ser mayor a 0")
        else:
            self._id = int(nuevo)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, nuevo):
        if nuevo is None:
            print("El titulo no debe ser Null o vacio, valor no actualizado")
        else:
            self._title = nuevo

    @property
    def genre(self):
        return self._genre

    @genre.setter
    def genre(self, value):
        if value is None:
            print("El genero no debe ser Null o vacio, valor no actualizado")
        else:
            self._genre = value

    @property
    def isbn(self):
        return self._isbn

    @isbn.setter
    def isbn(self, value):
        if value is None:
            print("El ISBN no debe ser Null o vacio, valor no actualizado")
        else:
            self._isbn = value

    @property
    def editorial(self):
        return self._editorial

    @editorial.setter
    def editorial(self, value):
        if value is None:
            print("La Editorial no debe ser Null o vacio, valor no actualizado")
        else:
            self._editorial = value

    @property
    def authors(self):
        return self._authors

    @authors.setter
    def authors(self, value):
        if value is None:
            print("Autor(es) no debe ser Null o vacio, valor no actualizado")
        else:
            self._authors = value
            self.cant_autores = len(self._authors.split(","))

    def print(self):
        print((f"ID: {self.id}, Titulo: {self.title}, Genero: {self.genre}, "
              f"ISBN: {self.isbn}, Editorial: {self.editorial}, "
              f"Autor(es): {self.authors}").strip())

    def update(self, new_title, new_genre, new_isbn, new_editorial, new_authores):
        self.title = new_title
        self.genre = new_genre
        self.isbn = new_isbn
        self.editorial = new_editorial
        self.authors = new_authores

