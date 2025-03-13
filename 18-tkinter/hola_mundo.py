# GUI Graphical user interface
# Tkinter
# Importamos el modulo de tkinter
import tkinter as tk
# Importar el modulo del tema de tkinter
from tkinter import ttk

# Creamos un objeto usando la clase tk
ventana = tk.Tk()
# Modificar el tamaño de la ventana (pixeles)
ventana.geometry("600x400")
# Cambiamos el nombre de la ventana
ventana.title("Hola mundo")
# Configuramos el icono de la aplicacion

ventana.iconbitmap("18-tkinter\icono.ico")

# Creamos el motodo evento_click
def evento_click():
  boton1.config(text="boton presionado")
  print("Ejecucion del evento_click")
  # Crear un nuevo componente y lo mostramos
  boton2 = ttk.Button(ventana, text="Nuevo boton")
  boton2.pack()

# Crear un boton (componente o widget), el objeto padre es la ventana
boton1 = ttk.Button(ventana, text="Dar click", command=evento_click)
# Utilizar el pack layout manager para mostrar el boton de la ventana
boton1.pack()

# Iniciamos la ventana (esta linea la ejecutamos al final)
# Si se ejecuta antes no se muestran los cambios
ventana.mainloop()