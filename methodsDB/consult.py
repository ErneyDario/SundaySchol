
from conexionDB.conexion import *
from mysql.connector import Error

# ----------------------------------------------------------------------------
# Consultar los registros de la tabla staff
# ----------------------------------------------------------------------------
def conStaff():
    try:
        cursor.execute("SELECT * FROM staff")
        staff = cursor.fetchall()
        return (staff)
    except Error as ex:
        return ("Error al realizar la consulta {0}".format(ex))

# ----------------------------------------------------------------------------
# Consultar los registros de la tabla rol
# ----------------------------------------------------------------------------
def conRol():
    try:
        cursor.execute("SELECT * FROM rol")
        rol = cursor.fetchall()
        return (rol)
    except Error as ex:
        return ("Error al realizar la consulta {0}".format(ex))

# ----------------------------------------------------------------------------
# Consultar los registros de la table classroom
# ----------------------------------------------------------------------------
def conClassroom():
    try:
        cursor.execute("SELECT * FROM classroom")
        classroom = cursor.fetchall()
        return (classroom)
    except Error as ex:
        return ("Error al realizar la consulta {0}".format(ex))
        
# ----------------------------------------------------------------------------
# Consultar un registro de la tabla staff y sus referencias
# ----------------------------------------------------------------------------
def conRegStaff(Identificiacion= str):
    try:
        cursor.execute ("""SELECT s.Identificacion, s.Nombres,s.Apellidos, s.Direccion, s.Telefono, u.user_Name, c.nameClass, r.nameRol FROM  staff s 
	join `user` u on s.Identificacion = u.idPerson 
	join classroom_staff cs on cs.idPerson  = cs.idPerson 
	join classroom c on cs.id_classroom = c.ID
	join staff_roles sr on sr.idPerson = s.Identificacion 
	join rol r on r.ID  = sr.idRol 
	where s.Identificacion = %s""", (Identificiacion,))
        regstaff = cursor.fetchall()
        if not regstaff:
            return("No se encontro un registro para el parametro {0}".format(Identificiacion))
        else:
            return (regstaff)
    except Error as ex:
        return ("Error al realizar la consulta {0}".format(ex))
