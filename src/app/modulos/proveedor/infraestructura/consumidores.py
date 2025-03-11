import pulsar,_pulsar  
from pulsar.schema import *
import uuid
import time
import logging
import traceback

from app.modulos.proveedor.infraestructura.schema.v1.eventos import EventoProveedorCreada
from app.modulos.proveedor.infraestructura.schema.v1.comandos import ComandoCrearProveedor
from app.seedwork.infraestructura import utils

def suscribirse_a_eventos():
    cliente = None
    try:
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumidor = cliente.subscribe('eventos-proveedor', consumer_type=_pulsar.ConsumerType.Shared,subscription_name='app-sub-eventos', schema=AvroSchema(EventoProveedorCreada))

        while True:
            mensaje = consumidor.receive()
            print(f'Evento recibido: {mensaje.value().data}')

            consumidor.acknowledge(mensaje)     

        cliente.close()
    except Exception as e:
        logging.error('ERROR: Suscribiendose al tópico de eventos!')
        logging.error(f'Error: {e}')
        traceback.print_exc()
        if cliente:
            cliente.close()
            
def suscribirse_a_proveedor_eliminada():
    cliente = None
    try:
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumidor = cliente.subscribe('eventos-proveedor-eliminada', consumer_type=_pulsar.ConsumerType.Shared,subscription_name='propiedadesalpes-sub-eventos', schema=AvroSchema(EventoPropiedadEliminada))

        while True:
            mensaje = consumidor.receive()
            datos_mensaje = mensaje.value()
            print(F'INFO: Se recibe evento (ProveedorEliminada) => [{datos_mensaje.data}]')          
            consumidor.acknowledge(mensaje)     
        cliente.close()
    except:
        print('ERROR: Suscribiendose al tópico de eventos!')
        traceback.print_exc()
        if cliente:
            cliente.close()          

def suscribirse_a_comandos():
    cliente = None
    try:
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumidor = cliente.subscribe('comandos-proveedor', consumer_type=_pulsar.ConsumerType.Shared, subscription_name='app-sub-comandos', schema=AvroSchema(ComandoCrearProveedor))

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