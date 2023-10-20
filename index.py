import data_base_connect as dbc
import functions

while True:
    dec = input("""Bienvenido.\nQué acción deseas realizar?\n
        1 - Crear un usuario
        2 - Modificar un usuario
        3 - Ver un usuario
        4 - Listar todos los usuarios
        5 - Buscar un usuario por su nombre o email
        6 - Eliminar un usuario
        7 - Salir
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
        dbc.listar_usuarios()
    elif dec == "5":
        query = input("Ingrese el nombre o el email de la persona: ")
        if(len(query) > 0):
            dbc.busqueda_usuario(query)
        else:
            print("No ha colocado la cantidad minima de caracteres de busqueda.")
    elif dec == "6":
        id = input("Ingrese el id del usuario a eliminar: ")
        dbc.eliminar_usuario(id)
    elif dec == "7":
        break

        
        



