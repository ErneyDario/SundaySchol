from conexionDB.conexion import *

def addPerson():
    cursor.execute("INSERT INTO staff(Identificacion, Nombres, Apellidos, Direccion, Telefono, FechaNacimiento) VALUES ('1065570490', ' Matilde lina', 'Vides Jimenez', 'Carrera 12 11 23', '3182345678','23/04/2001')")
    conexion.commit()
    return("El Registro fue exitoso")

def addUsers():
    cursor.execute ("INSERT INTO user(idPerson, user_Name, password) values('1065570488', 'Mati','12345678')")
    conexion.commit()
    return("Usuario Registrado")

def addRol():
    cursor.execute ("INSERT INTO rol(idPerson, user_Name, password) values('1065570488', 'Mati','12345678')")
    conexion.commit()
    return("Usuario Registrado")
