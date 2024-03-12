import mysql.connector # importamos las librerias para la conexion
from mysql.connector import Error # Importamos errores de conexion


try:
    conexion=mysql.connector.connect(   
    user='root',
    password='Dev4286@',
    host='localhost',
    port='3306',
    database='sundayschool_db'
    )
except Error as ex:
    print("Error en la conexion a la DB {0}".format(ex))