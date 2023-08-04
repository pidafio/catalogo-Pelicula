import os

class CatalogoPelicula:
    ruta_archivo = 'pelicula.txt'

    @classmethod
    def agregar_pelicula(cls, pelicula):
        with open(cls.ruta_archivo, 'a', encoding='utf8') as archivo:
            archivo.write(f'{pelicula.nombres}\n')

    @classmethod
    def listar_peliculas(cls):
        with open(cls.ruta_archivo, 'r' , encoding='utf8') as archivo:
            print('catalogo peliculas'.center(50, '-'))
            print(archivo.read())
    @classmethod
    def eliminar_peliculas(cls):
        os.remove(cls.ruta_archivo)
        print(f'archivo eliminado: {cls.ruta_archivo}')
