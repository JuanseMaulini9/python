import math
from decimal import Decimal

#NaN - Not a Number
#NaN no es sensible a mayusculas o minusculas
#NaN es un tipo de dato numerico indefinido
a = float("2.9")
# print(f"a: {a}")
# print(f"Es NaN (not a number)?: {math.isnan(a)} ")

a = Decimal("NaN")
print(f"a: {a}")
print(f"Es NaN (not a number)?: {math.isnan(a)} ")