#Importamos librerias
from fastapi import FastAPI
from registers import *
from registers.toRegister import *
#Instaciamos nuestra app
app = FastAPI() 

@app.post("/addstaff")
def addPerson():
    cursor.execute("INSERT INTO staff(Identificacion, Nombres, Apellidos, Direccion, Telefono, FechaNacimiento) VALUES ('1065570485', 'Carolina Andrea', 'Amador Peña', 'Carrera 12 11 23', '3182345678','23/04/2001')")
    conexion.commit()
    return("Registro exitoso")







