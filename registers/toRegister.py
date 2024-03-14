from conexionDB.conexion import *
from mysql.connector import Error

#------------------------------------------------------------------------------------------------------------------------
#    Funcion para agregar registros al Staff
#------------------------------------------------------------------------------------------------------------------------
def addPerson(Identificacion =str,
    Nombres = str,
    Apellidos = str,
    Direccion = str,
    Telefono = str,
    FechaNacimiento = str,
    ): 
    try:
        valoresStaff = (Identificacion, Nombres, Apellidos, Direccion, Telefono, FechaNacimiento)
        cursor.execute ("""INSERT INTO staff(Identificacion, Nombres, Apellidos, Direccion, Telefono, FechaNacimiento) 
                    VALUES (%s, %s, %s, %s, %s, %s)""",valoresStaff)
        conexion.commit()
        return("¡Registro Exitoso!")
    except Error as ex:
        return("Error al agregar el registro {0}".format(ex))
    
#-----------------------------------------------------------------------------------------------------------------------
#    Funcion para crear usuarios
#-----------------------------------------------------------------------------------------------------------------------
def addUsers(
        Identificacion =str,
        UserName = str,
        Password = str
        ):
    try:
        valoresUser = (Identificacion, UserName, Password)
        cursor.execute("""INSERT INTO user (idPerson, user_Name, contraseña) 
                       VALUES (%s, %s, %s)""",valoresUser)
        conexion.commit()
        return("Usuario Registrado")
    except Error as ex:
        return("Error al agregar el registro {0}".format(ex))
    
#-----------------------------------------------------------------------------------------------------------------------
    # Fucion Para Agregar Clases
#-----------------------------------------------------------------------------------------------------------------------
def addClassrom(
        nameClass = str, 
        ageRange = str
        ):
    try:
        valoresClass = (nameClass, ageRange)
        cursor.execute ("""INSERT INTO classroom (nameClass, ageRange)
                        VALUES (%s, %s)""", valoresClass)
        conexion.commit()
        return ("Clase Agregada con Exito")
    except Error as ex: 
        return ("Error al agregar el registro {0}".format(ex))

#------------------------------------------------------------------------------------------------------------------------
    # Funcion para Agregar Roles
#------------------------------------------------------------------------------------------------------------------------
  
def addRol(nameRol = str):
    try:
        cursor.execute ("INSERT INTO rol(nameRol) VALUES(%s)",(nameRol,))
        conexion.commit()
        return("El rol ha sido Creado con Exito")
    except Error as ex:
        return("Error al agregar el registro {0}".format(ex))


