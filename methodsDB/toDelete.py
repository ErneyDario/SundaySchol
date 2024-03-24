from conexionDB.conexion import *
from mysql.connector import Error

#---------------------------------------------------------------------
# Eliminar un registro de Staff
#---------------------------------------------------------------------
def delStaff(Identificacion = str):
    cursor.execute ("SELECT Nombres, Identificacion FROM staff WHERE Identificacion = '1065570480'")
    consulta = cursor.fetchall()
    if consulta != []:
        return("El usuario {0}".format(consulta), "sera Eliminado")        
    else:
        return("El numero de Identificación digitado, no existe en la Base de Datos")
    
#---------------------------------------------------------------------
# Realizar consulta en tabla staff
#---------------------------------------------------------------------
# def searchStaff(parameter = str):
#     cursor.execute("SELECT Nombres, Apellidos, Direccion, Telefono, ")

