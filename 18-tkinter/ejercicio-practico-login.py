import tkinter as tk
from tkinter import ttk, messagebox

class Login(tk.Tk):
  def __init__(self):
    super().__init__()
    
    # Crear y configurar el objeto
    self.geometry("300x130")
    self.title("Login")
    self.resizable(0,0)

    # configuracion del grid
    self.columnconfigure(0, weight=1)
    self.columnconfigure(1, weight=3)

    self._create_components()
    
    # definir el metodo crear componentes
  def _create_components(self):
    # usuario
    usuario_label = ttk.Label(self, text="Usuario:")
    usuario_label.grid(row=0, column=0, sticky=tk.E, padx=5, pady=5)
    self.usuario_input = ttk.Entry(self)
    self.usuario_input.grid(row=0, column=1, sticky=tk.W, padx=5, pady=5)
  
    # password
    password_label = ttk.Label(self, text="Password:")
    password_label.grid(row=1, column=0, sticky=tk.E, padx=5, pady=5)
    self.password_input = ttk.Entry(self, show="*")
    self.password_input.grid(row=1, column=1, sticky=tk.W, padx=5, pady=5)

    # Boton login 
    login_button = ttk.Button(self, text="Login", command=self._login)
    login_button.grid(row=3, column=0, columnspan=2)
  
  def _login(self):
    messagebox.showinfo("Datos Login", f"Usuario: {self.usuario_input.get()}, Password: {self.password_input.get()}")


if __name__ == "__main__":
  login_ventana = Login()
  login_ventana.mainloop()