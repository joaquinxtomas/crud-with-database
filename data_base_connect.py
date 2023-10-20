import sqlite3

conn = sqlite3.connect('crud_base.db')
cursor = conn.cursor()

cursor.execute('''
               CREATE TABLE IF NOT EXISTS usuarios (
	                id	INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre TEXT,
                    email TEXT
                );
               ''')

conn.commit()

def listar_usuarios():
    cursor.execute("""
                   SELECT * FROM usuarios
                   """)
    users = cursor.fetchall()
    for i in users:
        print(f"""Usuario: {i[0]} - Nombre: {i[1]} - Email: {i[2]}
              """)

def crear_usuario(nombre: str,email: str):
    cursor.execute("""
                    INSERT INTO usuarios(nombre,email)
                    VALUES(?, ?)
                   """, (nombre,email))
    conn.commit()
    print("""
          ---------------------------
          Usuario agregado con exito!
          ---------------------------
          """)

def modificar_usuario(id, nombre, email):
    cursor.execute("""
                   UPDATE usuarios
                   SET nombre = ?, email = ?
                   WHERE id = ?
                   """, (nombre,email, id))
    conn.commit()
    print("""
          -------------------
          Usuario actualizado
          -------------------
          """)

def ver_usuario(id):
    cursor.execute("""
                    SELECT * FROM usuarios
                    WHERE id = ?
                   """, (id,))
    usuario = cursor.fetchone()
    if(usuario):
        print(f"""
              -----------------------------------------
              Mostrando el usuario numero: {usuario[0]}
              nombre: {usuario[1]}, email: {usuario[2]}
              -----------------------------------------
          """)
    else:
        print("USUARIO NO ENCONTRADO")
        
def busqueda_usuario(query):
    cursor.execute("""
        SELECT id, nombre, email FROM usuarios
        WHERE nombre LIKE ? OR email LIKE ?
    """, ('%' + query + '%', '%' + query + '%'))
    resultados = cursor.fetchall()
    if (resultados):
        for i in resultados:
            print(f"Usuario: {i[0]} - Nombre: {i[1]} - Email: {i[2]}\n")
    else:
        print("No se han encontrado resultados.")
    
def eliminar_usuario(id):
    cursor.execute("""
                   DELETE FROM usuarios
                   WHERE id = ?
                   """, (id,))
    conn.commit()
    print("""
          ------------------------------
          Usuario eliminado exitosamente
          ------------------------------
          """)