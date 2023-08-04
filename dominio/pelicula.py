class Pelicula:
    def __init__(self, nombre):
        self._nombre=nombre
    def __str__(self):
        print(f'Pelicula:{self._nombre}')
    @property
    def nombres(self):
        return self._nombre
    @nombres.setter
    def nombres(self, nombre):
        self._nombre=nombre