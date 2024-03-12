from conexionDB.conexion import *

def addPerson(Identificacion =str,
    Nombres = str,
    Apellidos = str,
    Direccion = str,
    Telefono = str,
    FechaNacimiento = str): 
    valores = (Identificacion, Nombres, Apellidos, Direccion, Telefono, FechaNacimiento)
    cursor.execute("""INSERT INTO staff(Identificacion, Nombres, Apellidos, Direccion, Telefono, FechaNacimiento) 
                    VALUES (%s, %s, %s, %s, %s, %s)""",valores)
    conexion.commit()
    return("¡Registro Exitoso!")


# def addUsers():
#     cursor.execute ("INSERT INTO user(idPerson, user_Name, password) values('1065570488', 'Mati','12345678')")
#     conexion.commit()
#     return("Usuario Registrado")

# def addRol():
#     cursor.execute ("INSERT INTO rol(idPerson, user_Name, password) values('1065570488', 'Mati','12345678')")
#     conexion.commit()
#     return("Usuario Registrado")
