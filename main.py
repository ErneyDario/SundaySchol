#Importamos librerias
from fastapi import FastAPI
from registers import *
from registers.toRegister import *
from conexionDB.conexion import *

#Instaciamos nuestra app
app = FastAPI() 


#---------------------------------------------------------------------------------------------------
# creamos un nuevo registro Staff y creamos el usuario
#---------------------------------------------------------------------------------------------------
@app.post("/SundaySchool/Staff")
def post_addStaff(Identificacion: str, Nombres: str, Apellidos: str, Direccion: str, Telefono: str,
                   FechaNacimiento: str, UserName: str, Password: str):
    addPerson (Identificacion, Nombres, Apellidos, Direccion, Telefono, FechaNacimiento)
    addUsers(Identificacion, UserName, Password)
    return 

#---------------------------------------------------------------------------------------------------
# creamos un nuevo salon
#---------------------------------------------------------------------------------------------------

@app.post("/SundaySchool/Classroom")
def post_addClassroom(nameClass= str, ageRange = str):
    return addClassrom(nameClass, ageRange)

#---------------------------------------------------------------------------------------------------
# creamos un nuevo rol
#---------------------------------------------------------------------------------------------------

@app.post("/SundaySchool/Rol")
def post_addRol(nameRol = str):
    return addRol(nameRol)






