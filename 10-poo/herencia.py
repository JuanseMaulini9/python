class Animal:
  def comer(self):
    print("Como muchas veces al dia")
    
  def dormir(self):
    print("Duermo muchas horas")
    
class Perro(Animal):
  def hacer_sonido(self):
    print("wau")
  def dormir(self):
    print("Duermo 15 horas al dia")

print("Ejemplo de herencia en python")
print("Clase padre, soy un animal")
animal1 = Animal()
animal1.comer()
animal1.dormir()

print("\nClase Hija, soy un perro")
perro1 = Perro()
perro1.comer()
perro1.dormir()
perro1.hacer_sonido()