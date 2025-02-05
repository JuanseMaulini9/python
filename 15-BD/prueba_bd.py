import psycopg2

conexion = psycopg2.connect(user="postgres", password="admin", host="127.0.0.1", port="5432", database="test_db")

# LEER
# try:
#   with conexion:
#     with conexion.cursor() as cursor:
#       sentencia = "SELECT * FROM persona WHERE id_persona IN %s"
#       # llaves_primarias = ((1,2,3),)
#       entrada = input("Proporciona los ids a buscar (separados por comas):")
#       llaves_primarias = (tuple(entrada.split(",")),)
#       cursor.execute(sentencia, llaves_primarias)
#       registros = cursor.fetchall()
#       for registro in registros:
#         print(registro)
# except Exception as e:
#   print(f"Ocurrio un error: {e}")
# finally:
#   conexion.close()

# INSERTAR
# try:
#   with conexion:
#     with conexion.cursor() as cursor:
#       sentencia = "INSERT INTO persona(nombre, apellido, email) VALUES(%s, %s, %s)"
#       valores = (("Sanji", "Vinsmoke", "sanji@mail.com"), ("Nami", "", "nami@mail.com"), ("Usopp", "", "usopp@mail.com"))
#       cursor.executemany(sentencia, valores)
#       # conexion.commit()
#       registros_insertados = cursor.rowcount
#       print(f"Registros insertados: {registros_insertados}")
# except Exception as e:
#   print(f"Ocurrio un error: {e}")
# finally:
#   conexion.close()

# EDITAR
# try:
#   with conexion:
#     with conexion.cursor() as cursor:
#       sentencia = "UPDATE persona SET nombre = %s, apellido = %s, email = %s WHERE id_persona = %s"
#       valores = (("Franky", "", "suuuuuuper@mail.com", 1), ("Robin", "Nico", "robin@mail.com", 2))
#       cursor.executemany(sentencia, valores)
#       registros_actualizados = cursor.rowcount
#       print(f"Registros actualizados: {registros_actualizados}")
# except Exception as e:
#   print(f"Ocurrio un error: {e}")
# finally:
#   conexion.close()

# DELETE 
try:
  with conexion:
    with conexion.cursor() as cursor:
      sentencia = "DELETE FROM persona WHERE id_persona IN %s"
      entrada = input("Proporciona los id persona a eliminar (separados por coma): ")
      valores = (tuple(entrada.split(",")), )
      cursor.execute(sentencia, valores)
      registros_borrados = cursor.rowcount
      print(f"Registros borrados: {registros_borrados}")
except Exception as e:
  print(f"Ocurrio un error: {e}")
finally:
  conexion.close()