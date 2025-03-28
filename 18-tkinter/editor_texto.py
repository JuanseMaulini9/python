import tkinter as tk

class Editor(tk.Tk):
  def __init__(self):
    super().__init__()
    self.title("Editor de texto")
    
    #Configurar tamaño minimo de la ventana
    self.rowconfigure(0, minsize=600, weight=1)
    #Configuracion minima de la segunda columna
    self.columnconfigure(1, minsize=600, weight=1)
    # Atributo de campo de texto
    self.campo_texto = tk.Text(self, wrap=tk.WORD)