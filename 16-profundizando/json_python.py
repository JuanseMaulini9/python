# Leer archivo json
# JSON = Javascript Object Notation
import json
import urllib.request
# peticion = urllib.request.Request(
#     'http://globalmentoring.com.mx/api/personas.json',
#     data=None,
#     headers={
#         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
#     }
# )

# respuesta = urllib.request.urlopen('http://globalmentoring.com.mx/api/personas.json')
# print(respuesta)
# cuerpo_respuesta = respuesta.read()
# print(cuerpo_respuesta)

# # Procesar la respuesta
# json_respuesta = json.loads(cuerpo_respuesta.decode("utf-8"))
# print(json_respuesta)

# # Imprimir solo los nombres de las personas
# # JSON se convierte a listas y diccionarios en python
# for persona in json_respuesta["personas"]:
#   print(f"Persona: {persona['nombre']}, Edad: {persona["edad"]}")

# # Accedemos a las variables independientes

# print(f"Total de personas: {json_respuesta["total"]}")
# print(f"Mensaje de la respuesta: {json_respuesta["mensaje"]}")


respuesta = urllib.request.urlopen('https://globalmentoring.com.mx/api/clima.json')

cuerpo_respuesta = respuesta.read()
json_respuesta = json.loads(cuerpo_respuesta.decode("utf-8"))

clima = json_respuesta["clima"]
descripcion = clima[0]["descripcion"]

principal = json_respuesta["principal"]
temp_min = principal["temp_min"]
temp_max = principal["temp_max"]

print(f"descripcion del clima: {descripcion}, temperatura minima: {temp_min}, temperatura maxima: {temp_max}")