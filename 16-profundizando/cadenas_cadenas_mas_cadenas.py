# multiplicacion str
# resultado = 3*"Hola"
# print(f"Resultado: {resultado}")


# # multiplicacion de tuplas
# resultado = 5*("Hola", 10)
# print(f"Resultado: {resultado}")

# #multiplicacion de listas
# resultado = 10*[0]
# print(f"Resultado: {resultado}, largo: {len(resultado)}")

# caracteres de escape
# resultado = "Hola \" Mundo"
# # print(resultado)

# resultado = 'Se va a eliminar el punto.\b'
# print(resultado)

# # Caracter \
# resultado = "c:\\directorio\\hola"
# # print(resultado)

# # raw string 
# resultado = r"Cadena con \n salto de linea"
# print(resultado)

# caracteres unicode
# print("Hola\u0020Mundo")
# print("Noracion simple:", "\u0041")
# print("Notacion extendida:", "\U00000041")
# print("Notacion hexadecimal:", "\x41")
# print("Corazon:", "\u2665")
# print("Cara sonriendo:", "\U0001f600")
# print("Serpiente:", "\U0001f40d")

# Caracteres ascii
# caracter = chr(65)
# print("A:",caracter)

# caracter = chr(64)
# print("@:",caracter)

# caracter = chr(97)
# print("a:",caracter)

caracteres_en_bytes = b"Hola Mundo"
print(caracteres_en_bytes)

mensaje = b"Universidad python"
print(mensaje[0])
print(chr(mensaje[0]))

lista_caracteres = mensaje.split()
print(lista_caracteres)

# Convertir de str a bytes
string = 'Programación con Python'
print("string original:", string)

bytes = string.encode("UTF-8")
print("bytes codificado:", bytes)

# Convertir de bytes a string
string2 = bytes.decode("UTF-8")
print("string decodificado:", string2)
print(string == string2)