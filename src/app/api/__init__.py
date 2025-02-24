import os
from flask import Flask, render_template, request, url_for, redirect, jsonify
from flask_swagger import swagger

# Identifica el directorio base
basedir = os.path.abspath(os.path.dirname(__file__))

def registrar_handlers():
    import app.modulos.imagen_medica.aplicacion
    
def importar_modelos_alchemy():
    import app.modulos.imagen_medica.infraestructura.dto
    
def comenzar_consumidor():
    """
    Este es un código de ejemplo. Aunque esto sea funcional puede ser un poco peligroso tener 
    threads corriendo por si solos. Mi sugerencia es en estos casos usar un verdadero manejador
    de procesos y threads como Celery.
    """

    import threading
    import app.modulos.imagen_medica.infraestructura.consumidores as imagen_medica

    # Suscripción a eventos
    threading.Thread(target=imagen_medica.suscribirse_a_eventos).start()

    # Suscripción a comandos
    threading.Thread(target=imagen_medica.suscribirse_a_comandos).start()
            
def create_app(configuracion=None):
    # Init la aplicacion de Flask
    app = Flask(__name__, instance_relative_config=True)

    # Configuracion de BD
    app.config['SQLALCHEMY_DATABASE_URI'] =\
            'sqlite:///' + os.path.join(basedir, 'database.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

     # Inicializa la DB
    from app.config.db import init_db
    init_db(app)

    from app.config.db import db

    importar_modelos_alchemy()
    registrar_handlers()

    with app.app_context():
        db.create_all()
        comenzar_consumidor()
     # Importa Blueprints
    from . import imagen_medica

    # Registro de Blueprints
    app.register_blueprint(imagen_medica.bp)

    @app.route("/spec")
    def spec():
        swag = swagger(app)
        swag['info']['version'] = "1.0"
        swag['info']['title'] = "My API"
        return jsonify(swag)

    @app.route("/health")
    def health():
        return {"status": "up"}

    return app
