print("*** Agenda contactos ***")

agenda = {
  "Luffy": {
      "telefono": "2345456",
      "email": "luffy@mail.com",
      "direccion": "villa Foosha"
  },
  "Zoro": {
      "telefono": "2431324",
      "email": "zoro@mail.com",
      "direccion": "wano"
  },
  "Nami": {
      "telefono": "4325656",
      "email": "nami@mail.com",
      "direccion": "Arlong park"
  }
}

print(f"""Informacion del contacto de Nami:
    Telefono: {agenda["Nami"]["telefono"]}
    Email: {agenda["Nami"]["email"]}
    Direccion: {agenda["Nami"]["direccion"]}
    """)

agenda["Ussop"] = {
  "telefono": "3423423",
  "email": "ussop@mail.com",
  "direccion": "villa syrup"
}

print(agenda)

agenda.pop("Nami")
print(agenda)

print("\nContactos en la agenda")

for nombre, detalles in agenda.items():
  print(f"""Nombre: {nombre}
        Telefono: {detalles.get("telefono")}
        Email: {detalles.get("email")}
        Direccion: {detalles.get("direccion")}
        """)