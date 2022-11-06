
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


