#Importamos librerias
from fastapi import FastAPI
from methodsDB.toRegister import *
from methodsDB.toDelete import *
from conexionDB.conexion import *
from methodsDB.consult import *

#Instaciamos nuestra app
app = FastAPI() 


#---------------------------------------------------------------------------------------------------
# creamos un nuevo registro Staff y creamos el usuario
#---------------------------------------------------------------------------------------------------
@app.post("/SundaySchool/Staff")
def post_addStaff(Identificacion: str, Nombres: str, Apellidos: str, Direccion: str, Telefono: str,
                   FechaNacimiento: str, UserName: str, Password: str):
    addPerson (Identificacion, Nombres, Apellidos, Direccion, Telefono, FechaNacimiento)
    return addUsers(Identificacion, UserName, Password)

#---------------------------------------------------------------------------------------------------
# creamos un nuevo salon de Clases
#---------------------------------------------------------------------------------------------------

@app.post("/SundaySchool/Classroom")
def post_addClassroom(nameClass = str, initialAge = str, finalAge = str):
    return addClassrom(nameClass, initialAge, finalAge)

#---------------------------------------------------------------------------------------------------
# creamos un nuevo rol
#---------------------------------------------------------------------------------------------------

@app.post("/SundaySchool/Rol")
def post_addRol(nameRol = str):
    return addRol(nameRol)

#----------------------------------------------------------------------------------------------------
# Consultamos la tabla staff
# ---------------------------------------------------------------------------------------------------
@app.get("/SundaySchool/consultar/Staff")
def getConStaff():
    return(conStaff())

#----------------------------------------------------------------------------------------------------
# Consultamos la tabla Rol
# ---------------------------------------------------------------------------------------------------
@app.get("/SundaySchool/consultar/rol")
def getConRol():
    return(conRol())

#----------------------------------------------------------------------------------------------------
# Consultamos la tabla classRoom    
# ---------------------------------------------------------------------------------------------------
@app.get("/SundaySchool/consultar/classRoom")
def getConClassroom():
    return(conClassroom())

#----------------------------------------------------------------------------------------------------
# Consultamos los datos de una persona registrada
# ---------------------------------------------------------------------------------------------------
@app.get("/SundaySchool/consultar/conRegStaff")
def getConRegStaff(Identificiacion = str):
    return (conRegStaff(Identificiacion))




