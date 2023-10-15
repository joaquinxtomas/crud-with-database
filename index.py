import data_base_connect as dbc
import functions

while True:
    dec = input("""Bienvenido.\nQué acción deseas realizar?\n
        1 - Crear un usuario
        2 - Modificar un usuario
        3 - Ver un usuario
        4 - Eliminar un usuario
        5 - Salir
      """)
    if dec == "1":
        name = input("Ingrese su nombre: ")
        email = functions.validar_email()
        dbc.crear_usuario(name,email)
    elif dec == "2":
        id = input("Ingrese el id del usuario a modificar: ")
        name = input("Ingrese el nuevo nombre: ")
        email = functions.validar_email()
        dbc.modificar_usuario(id,name,email)
    elif dec == "3":
        id = input("Ingrese el id del usuario a visualizar: ")
        dbc.ver_usuario(id)
    elif dec == "4":
        id = input("Ingrese el id del usuario a eliminar: ")
        dbc.eliminar_usuario(id)
    elif dec == "5":
        break

        
        



