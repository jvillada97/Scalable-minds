import pulsar
from pulsar.schema import *

from app.modulos.anonimizacion.infraestructura.schema.v1.eventos import EventoAnonimizacionCreada, AnonimizacionCreadaPayload
from app.modulos.anonimizacion.infraestructura.schema.v1.comandos import ComandoCrearAnonimizacion, ComandoCrearAnonimizacionPayload
from app.seedwork.infraestructura import utils

import datetime

epoch = datetime.datetime.utcfromtimestamp(0)

def unix_time_millis(dt):
    return (dt - epoch).total_seconds() * 1000.0

class Despachador:
    def _publicar_mensaje(self, mensaje, topico, schema):
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        publicador = cliente.create_producer(topico, schema=AvroSchema(EventoAnonimizacionCreada))
        publicador.send(mensaje)
        cliente.close()

    def publicar_evento(self, evento, topico):
        # TODO Debe existir un forma de crear el Payload en Avro con base al tipo del evento
        payload = AnonimizacionCreadaPayload(
            id=evento.id,
            url_imagen=evento.url_imagen
        )
        evento_integracion = EventoAnonimizacionCreada(data=payload)
        self._publicar_mensaje(evento_integracion, topico, AvroSchema(EventoAnonimizacionCreada))

    def publicar_comando(self, comando, topico):
        # TODO Debe existir un forma de crear el Payload en Avro con base al tipo del comando
        payload = ComandoCrearAnonimizacionPayload(
            id_usuario=str(comando.id_usuario)
        )
        comando_integracion = ComandoCrearAnonimizacion(data=payload)
        self._publicar_mensaje(comando_integracion, topico, AvroSchema(ComandoCrearAnonimizacion))
