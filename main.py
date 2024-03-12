#Importamos librerias
from fastapi import FastAPI
from registers import *
from registers.toRegister import *
from conexionDB.conexion import *

#Instaciamos nuestra app
app = FastAPI() 


#------------------------------------------
# creamos un nuevo registro
# #------------------------------------------
@app.post("/Staff")
def addStaff(Identificacion: str, Nombres: str, Apellidos: str, Direccion: str, Telefono: str, FechaNacimiento: str):
    return addPerson(Identificacion, Nombres, Apellidos, Direccion, Telefono, FechaNacimiento)

@app.get("/staff")
def get_staff():
    cursor.execute("SELECT * FROM staff")
    staff = cursor.fetchall()
    return(staff)






