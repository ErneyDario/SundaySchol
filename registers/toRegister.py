from conexionDB.conexion import *

cursor = conexion.cursor

def addPerson():    
    cursor.execute ("""INSERT INTO staff(Identificacion, Nombres, Apellidos, Direccion, Telefono, FechaNacimiento) 
                   VALUES (%s, %s, %s, %s, %s, %s,)""")
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
