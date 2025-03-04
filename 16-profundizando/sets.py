# Profundizando en set
# un set es una coleccion de elementos unicos y es mutable
# Los elementos de un set deben ser inmutables

# conjunto = {[1,2], [3,4]}
conjunto = {"Luffy", True, 1.2}
print(conjunto)
print(type(conjunto))

#Set vacio
# conjunto = {} Genera un diccionario vacio
# print(type(conjunto))
# Set vacio correcto

conjunto = set()
print(conjunto)
print(type(conjunto))

# Mutable
conjunto.add("Luffy")
print(conjunto)

# Contiene valores unicos
conjunto.add("Luffy")
print(conjunto)

# Crear un set a partir de un iterable
conjunto = set([4,5,6,7,4,5])
print(conjunto)

# Podemos agregar mas elementos o incluso otro set al set que ya definimos
conjunto2 = {100, 200, 300, 300}
conjunto.update(conjunto2)
print(conjunto)
conjunto.update([20,30,40,40])
print(conjunto)

# Copiar un set (copia poco profunda, solo se copia la referencia)
conjunto_copia = conjunto.copy()
print(conjunto_copia)

# Verificar la igualdad
print(f"Es igual en contenido?: {conjunto == conjunto_copia}")
print(f"Es igual en referencia?: {conjunto is conjunto_copia}")

pelo_negro = {"Luffy", "Robin", "Usopp", "Law"}
pelo_rubio = {"Sanji", "Cavendish", "Sabo"}
ojos_oscuros = {"Luffy", "Sabo"}
menores_20 = {"Luffy", "Law", "Usopp"}

# Todos con ojos cafe y pelo rubiuo
print(ojos_oscuros.union(pelo_rubio))
# Invertir el orden con el mismo resultado (conmutativa)

print(pelo_rubio.union(ojos_oscuros))

# (intersection) Solo las personas con ojos oscuros y rubios (conmutativa)
print(ojos_oscuros.intersection(pelo_rubio))

# (difference) Solo recupera los elementos de un conjunto ignorando los de otro set (no conmutativa)
# Solo personas con pelo negro sin ojos oscuros
print(pelo_negro.difference(ojos_oscuros))

# (simetrica) solo devuelve los elementos en comun (conmutativa)
# Pelo negro u ojos oscuros, pero no ambos
print(pelo_negro.symmetric_difference(ojos_oscuros))

# Preguntar si un set esta contenido en otro (subset)
# revismaos si los elementos del primer conjunto estan contenidos en el segundo set
print(menores_20.issubset(pelo_negro))

# Preguntar si un set contiene a otro set (superset)
# revisar si los elementos del primer set estan contenidos en el segundo set
print(menores_20.issuperset(pelo_negro))

# Preguntar si los de pelo negro no tienen pelo rubio (distjoin)
print(pelo_negro.isdisjoint(pelo_rubio))