#Importamos librerias
from fastapi import FastAPI
from registers import *
from registers.toRegister import *
from conexionDB.conexion import *

#Instaciamos nuestra app
app = FastAPI() 

#------------------------------------------
# creamos un nuevo registro
#------------------------------------------

@app.get("/")
def conexionDB():
    return probandoConexion()








