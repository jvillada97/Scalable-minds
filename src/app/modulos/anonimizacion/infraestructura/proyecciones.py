from app.seedwork.infraestructura.proyecciones import Proyeccion, ProyeccionHandler
from app.seedwork.infraestructura.proyecciones import ejecutar_proyeccion as proyeccion
from app.modulos.anonimizacion.infraestructura.fabricas import FabricaRepositorio
from app.modulos.anonimizacion.infraestructura.repositorios import RepositorioAnonimizacions
from app.modulos.anonimizacion.dominio.entidades import Anonimizacion
from app.modulos.anonimizacion.infraestructura.dto import Anonimizacion as AnonimizacionDTO

from app.seedwork.infraestructura.utils import millis_a_datetime

import datetime
import logging
import traceback
from abc import ABC, abstractmethod
from .dto import AnonimizacionAnalitica

class ProyeccionAnonimizacion(Proyeccion, ABC):
    @abstractmethod
    def ejecutar(self):
        ...

class ProyeccionImagenesTotales(ProyeccionAnonimizacion):
    ADD = 1
    DELETE = 2
    UPDATE = 3

    def __init__(self, fecha_creacion, operacion):
        self.fecha_creacion = millis_a_datetime(fecha_creacion)
        self.operacion = operacion

    def ejecutar(self, db=None):
        if not db:
            logging.error('ERROR: DB del app no puede ser nula')
            return
        # NOTE esta no usa repositorios y de una vez aplica los cambios. Es decir, no todo siempre debe ser un repositorio
        record = db.session.query(AnonimizacionAnalitica).filter_by(fecha_creacion=self.fecha_creacion.date()).one_or_none()

        if record and self.operacion == self.ADD:
            record.total += 1
        elif record and self.operacion == self.DELETE:
            record.total -= 1 
            record.total = max(record.total, 0)
        else:
            db.session.add(AnonimizacionAnalitica(fecha_creacion=self.fecha_creacion.date(), total=1))
        
        db.session.commit()

class ProyeccionImagenesLista(ProyeccionAnonimizacion):
    def __init__(self, id_imagen, url_imagen, fecha_creacion, fecha_actualizacion):
        self.id_imagen = id_imagen
        self.url_imagen = url_imagen
        self.fecha_creacion = millis_a_datetime(fecha_creacion)
        self.fecha_actualizacion = millis_a_datetime(fecha_actualizacion)
    
    def ejecutar(self, db=None):
        if not db:
            logging.error('ERROR: DB del app no puede ser nula')
            return
        
        fabrica_repositorio = FabricaRepositorio()
        repositorio = fabrica_repositorio.crear_objeto(RepositorioAnonimizacions)
        
        # TODO Haga los cambios necesarios para que se consideren los itinerarios, demás entidades y asociaciones
        repositorio.agregar(
            Anonimizacion(
                id=str(self.id_imagen), 
                url_imagen=str(self.url_imagen), 
                fecha_creacion=self.fecha_creacion, 
                fecha_actualizacion=self.fecha_actualizacion))
        
        # TODO ¿Y si la imagen ya existe y debemos actualizarla? Complete el método para hacer merge

        # TODO ¿Tal vez podríamos reutilizar la Unidad de Trabajo?
        db.session.commit()

class ProyeccionAnonimizacionHandler(ProyeccionHandler):
    
    def handle(self, proyeccion: ProyeccionAnonimizacion):

        # TODO El evento de creación no viene con todos los datos de itinerarios, esto tal vez pueda ser una extensión
        # Asi mismo estamos dejando la funcionalidad de persistencia en el mismo método de recepción. Piense que componente
        # podriamos diseñar para alojar esta funcionalidad
        from app.config.db import db

        proyeccion.ejecutar(db=db)
        

@proyeccion.register(ProyeccionImagenesLista)
@proyeccion.register(ProyeccionImagenesTotales)
def ejecutar_proyeccion_imagen_medica(proyeccion, app=None):
    if not app:
        logging.error('ERROR: Contexto del app no puede ser nulo')
        return
    try:
        with app.app_context():
            handler = ProyeccionAnonimizacionHandler()
            handler.handle(proyeccion)
            
    except:
        traceback.print_exc()
        logging.error('ERROR: Persistiendo!')