''' Este archivo se utiliza para realizar la importacion de las configuraciones globales
    tales como la importacion de la app, las rutas generales del proyecto, definir si el
    servidor corre en modo debug, Registro de la BD, etc.'''

from flask import Flask
from myapp.config import DevConfig
from myapp.tasks.controllers import taskRoute

app = Flask(__name__)
app.register_blueprint(taskRoute) #Registra
#app.debug = True

app.config.from_object(DevConfig)
@app.route('/') #Esta es la ruta más global de nuestro proyecto
def hello_world() -> str:
    return ' Hello world'