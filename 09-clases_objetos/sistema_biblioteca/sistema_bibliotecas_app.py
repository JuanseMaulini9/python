import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from sistema_biblioteca.biblioteca import Biblioteca
from sistema_biblioteca.libro import Libro

bibliotecaNacional = Biblioteca("Biblioteca Nacional")
print(f"*** Bienvenidos a la {bibliotecaNacional.nombre}***")

# definicion de libros
libro1 = Libro("One piece", "Eichiro Oda", "Piratas")
libro2 = Libro("Naruto", "Masashi Kishimoto", "Ninjas")
libro3 = Libro("Dragon Ball", "Akira Toriyama", "Aventura")
libro4 = Libro("Wanted", "Eichiro Oda", "historias cortas")
libro5 = Libro("Jujutsu kaisen", "GeGe Akutami", "Aventura")

bibliotecaNacional.agregar_libro(libro1)
bibliotecaNacional.agregar_libro(libro2)
bibliotecaNacional.agregar_libro(libro3)
bibliotecaNacional.agregar_libro(libro4)
bibliotecaNacional.agregar_libro(libro5)

autor = "Eichiro Oda"
bibliotecaNacional.buscar_libro_por_autor(autor)

genero = "Aventura"
print(f"\nLibros de {genero}:")
bibliotecaNacional.buscar_libros_por_genero(genero)

bibliotecaNacional.mostrar_todos_los_libros()