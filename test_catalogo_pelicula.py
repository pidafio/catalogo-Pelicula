from dominio.pelicula import Pelicula
from servicio.catalogo_peliculas import CatalogoPelicula

opcion= None

while opcion !=4:
      try:
              print('Opciones:')
              print('1. Agregar Pelicula')
              print('2. Listar Pelicula')
              print('3. Eliminar catalogo pelicula')
              print('4. Salir')
              opcion = int(input('escribe tu opcion (1-4): '))

              if opcion== 1:
                  nombre_pelicula= input('proporciona el nombre de la pelicula: ')
                  pelicula = Pelicula(nombre_pelicula)
                  CatalogoPelicula.agregar_pelicula(pelicula)
              elif opcion==2:
                    CatalogoPelicula.listar_peliculas()
              elif opcion==3:
                    CatalogoPelicula.eliminar_peliculas()

      except Exception as e:
               print(f'Ocurrio un error {e}')
               opcion=None

else:
    print('salimos del programa')
