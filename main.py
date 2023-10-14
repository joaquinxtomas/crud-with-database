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
    print("Usuario agregado con exito!")

def ver_usuario(id):
    cursor.execute("""
                    SELECT * FROM usuarios
                    WHERE id = ?
                   """, (id,))
    usuario = cursor.fetchone()
    print(f"""Mostrando el usuario numero: {usuario[0]}\nnombre: {usuario[1]}, email: {usuario[2]}
          """)
    
def eliminar_usuario(id):
    cursor.execute("""
                   DELETE FROM usuarios
                   WHERE id = ?
                   """, (id,))
    conn.commit()
    print("Usuario eliminado exitosamente.")
    
crear_usuario("jorge", "jorge@gmail.com")
ver_usuario(2)
    