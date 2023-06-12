class Saludo:
    def __init__(self, nombre=str):
        self.__nombre=nombre
    def saludo_carlos(self):
        return f'Hola {self.__nombre} usando libreria'