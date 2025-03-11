# Ejemplo atributos publicos, protegidos y privados

class MiClase:
  def __init__(self, publico, protegido, privado):
    self.publico = publico
    self._protegido = protegido
    self.__privado = privado
  
objeto = MiClase("Valor publico", "Valor protegido", "Valor privado")
# Acceso al atributo publico
print(objeto.publico)
  
# Modificar el valor publico
objeto.publico = "Nuevo valor publico"
print(objeto.publico)

# Acceso al valor protegido
# Solo se puede acceder dentro de la clase o clases hijas
# No es buena practica
print(objeto._protegido)
# Modificar atributo protegido
objeto._protegido = "Nuevo valor protegido"
print(objeto._protegido)

# Acceder al valor privado
# print(objeto.__privado) No se puede utilizar directamente
# Pero, conviere: objeto._clase__atributo_privado
print(objeto._MiClase__privado)
# Modificar valor privado

objeto._MiClase__privado = "Nuevo valor privado"
print(objeto._MiClase__privado)
