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