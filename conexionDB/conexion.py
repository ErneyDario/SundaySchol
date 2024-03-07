import mysql.connector # importamos las librerias para la conexion

#Instanciamos la coneccion en la variable conexion
conexion = mysql.connector.connect (
    user='root',
    password='Dev4286@',
    host='localhost',
    port='3306',
    database='sundayschool_db'
)
cursor = conexion.cursor()
print(conexion)



