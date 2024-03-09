#Importamos librerias
from fastapi import FastAPI
from registers import *
from registers.toRegister import *
#Instaciamos nuestra app
app = FastAPI() 

#------------------------------------------
# creamos un nuevo registro
#------------------------------------------
@app.post("/addstaff")
def addstaff():
    return addPerson()
    








