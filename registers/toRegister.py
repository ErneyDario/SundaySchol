from conexionDB.conexion import *

def addPerson():
    cursor.execute("INSERT INTO staff(Identificacion, Nombres, Apellidos, Direccion, Telefono, FechaNacimiento) VALUES ('1065570484', 'Andrea Johana', 'Amador Peña', 'Carrera 12 11 23', '3182345678','23/04/2001')")
    conexion.commit()
    return("Registro exitoso")
