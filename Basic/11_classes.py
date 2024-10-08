### Clases ###

class EmptyPerson: 
  pass

print(EmptyPerson)
print(EmptyPerson())

class Person:
  def __init__(self, name, surname, alias = "No tiene alias"):
    self.full_name = f"{name} {surname} ({alias})" # Propiedad publica
    self.__name = name # Propiedad privada
    
  def walk(self):
    print(f"{self.full_name} esta caminando")
    
  def get_name(self):
    return self.__name
  
my_person = Person("Juanse", "Maulini")
print(my_person.full_name)
print(my_person.get_name())
my_person.walk()

my_other_person = Person("Luffy", "Monkey D.", "Mugiwara")
print(my_other_person.full_name)
my_other_person.walk()
my_other_person.full_name = "Roronoa Zoro (Rey del infierno)"
print(my_other_person.full_name)


