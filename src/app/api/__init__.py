import os
from flask import Flask, render_template, request, url_for, redirect, jsonify
from flask_swagger import swagger

# Identifica el directorio base
basedir = os.path.abspath(os.path.dirname(__file__))

# Constantes
DB_USER = os.environ["POSTGRES_USER"]
DB_PASSWORD = os.environ["POSTGRES_PASSWORD"]
DB_HOST = os.environ["POSTGRES_HOST"]
DB_PORT = os.environ["POSTGRES_PORT"]
DB_NAME =  os.environ["POSTGRES_DB"]
def registrar_handlers():
    import app.modulos.imagen_medica.aplicacion
    import app.modulos.proveedor.aplicacion
    import app.modulos.anonimizacion.aplicacion
    
    
def importar_modelos_alchemy():
    import app.modulos.imagen_medica.infraestructura.dto
    import app.modulos.proveedor.infraestructura.dto
    import app.modulos.anonimizacion.infraestructura.dto
    
def comenzar_consumidor():
    """
    Este es un código de ejemplo. Aunque esto sea funcional puede ser un poco peligroso tener 
    threads corriendo por si solos. Mi sugerencia es en estos casos usar un verdadero manejador
    de procesos y threads como Celery.
    """

    import threading
    import app.modulos.imagen_medica.infraestructura.consumidores as imagen_medica
    import app.modulos.proveedor.infraestructura.consumidores as provedor
    import app.modulos.anonimizacion.infraestructura.consumidores as anonimizacion
    # Suscripción a eventos
    threading.Thread(target=imagen_medica.suscribirse_a_eventos).start()
    threading.Thread(target=provedor.suscribirse_a_eventos).start()
    threading.Thread(target=anonimizacion.suscribirse_a_eventos).start()

    # Suscripción a comandos
    threading.Thread(target=imagen_medica.suscribirse_a_comandos).start()
    threading.Thread(target=provedor.suscribirse_a_comandos).start()
    threading.Thread(target=anonimizacion.suscribirse_a_comandos).start()
            
def create_app(configuracion=None):
    # Init la aplicacion de Flask
    app = Flask(__name__, instance_relative_config=True)

    # Configuracion de BD
    app.config["SQLALCHEMY_DATABASE_URI"] = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.secret_key = '9d58f98f-3ae8-4149-a09f-3a8c2012e32c'
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
    from . import provedor
    from . import anonimizacion

    # Registro de Blueprints
    app.register_blueprint(imagen_medica.bp)
    app.register_blueprint(provedor.bp)
    app.register_blueprint(anonimizacion.bp)

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
