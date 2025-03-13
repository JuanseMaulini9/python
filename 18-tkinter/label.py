import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()
ventana.geometry("600x400")
ventana.title("Manejo de componentes")
ventana.iconbitmap("18-tkinter\icono.ico")

entrada_var1 = tk.StringVar(value="valor por default")
entrada1 = ttk.Entry(ventana, width=30, textvariable=entrada_var1)
entrada1.grid(row=0, column=0)

# Etiqueta
etiqueta1 = tk.Label(ventana, text="Aqui se mostrara el contenido de la caja de texto")
etiqueta1.grid(row=1, column=0, columnspan=2)

def enviar():
  # modificamos el texto del label
  etiqueta1.config(text=entrada_var1.get())
 
  
  
# Creamos un boton 
boton1 = ttk.Button(ventana, text="Enviar", command=enviar)
boton1.grid(row=0, column=1)


ventana.mainloop()
