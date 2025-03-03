import pulsar,_pulsar  
from pulsar.schema import *
import uuid
import time
import logging
import traceback

from app.modulos.imagen_medica.infraestructura.schema.v1.eventos import EventoImagenMedicaCreada
from app.modulos.imagen_medica.infraestructura.schema.v1.comandos import ComandoCrearImagenMedica
from app.seedwork.infraestructura import utils
from app.seedwork.infraestructura.proyecciones import ejecutar_proyeccion
from app.modulos.imagen_medica.infraestructura.proyecciones import ProyeccionImagenesLista, ProyeccionImagenesTotales


def suscribirse_a_eventos(app=None):
    cliente = None
    try:
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumidor = cliente.subscribe('eventos-imagen-medica', consumer_type=_pulsar.ConsumerType.Shared,subscription_name='app-sub-eventos', schema=AvroSchema(EventoImagenMedicaCreada))

        while True:
            mensaje = consumidor.receive()
            datos = mensaje.value().data

            print(f'Evento recibido: {mensaje.value().data}')
            ejecutar_proyeccion(ProyeccionImagenesTotales(datos.fecha_creacion, ProyeccionImagenesTotales.ADD), app=app)
            ejecutar_proyeccion(ProyeccionImagenesLista(datos.id_imagen, datos.url_imagen, datos.fecha_creacion, datos.fecha_creacion), app=app)
            
            consumidor.acknowledge(mensaje)     

        cliente.close()
    except Exception as e:
        logging.error('ERROR: Suscribiendose al tópico de eventos!')
        logging.error(f'Error: {e}')
        traceback.print_exc()
        if cliente:
            cliente.close()

def suscribirse_a_comandos():
    cliente = None
    try:
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumidor = cliente.subscribe('comandos-imagen-medica', consumer_type=_pulsar.ConsumerType.Shared, subscription_name='app-sub-comandos', schema=AvroSchema(ComandoCrearImagenMedica))

        while True:
            mensaje = consumidor.receive()
            print(f'Comando recibido: {mensaje.value().data}')

            consumidor.acknowledge(mensaje)     
            
        cliente.close()
    except Exception as e:
        logging.error('ERROR: Suscribiendose al tópico de comandos!')
        logging.error(f'Error: {e}')
        traceback.print_exc()
        if cliente:
            cliente.close()