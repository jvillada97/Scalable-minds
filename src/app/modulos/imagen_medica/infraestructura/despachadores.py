import pulsar
from pulsar.schema import *

from app.modulos.imagen_medica.infraestructura.schema.v1.eventos import EventoImagenMedicaCreada, ImagenMedicaCreadaPayload
from app.modulos.imagen_medica.infraestructura.schema.v1.comandos import ComandoCrearImagenMedica, ComandoCrearImagenMedicaPayload
from app.seedwork.infraestructura import utils

import datetime

epoch = datetime.datetime.utcfromtimestamp(0)

def unix_time_millis(dt):
    return (dt - epoch).total_seconds() * 1000.0

class Despachador:
    def _publicar_mensaje(self, mensaje, topico, schema):
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        publicador = cliente.create_producer(topico, schema=AvroSchema(EventoImagenMedicaCreada))
        publicador.send(mensaje)
        cliente.close()

    def publicar_evento(self, evento, topico):
        # TODO Debe existir un forma de crear el Payload en Avro con base al tipo del evento
        payload = ImagenMedicaCreadaPayload(
            id=evento.id,
            url_imagen=evento.url_imagen
        )
        evento_integracion = EventoImagenMedicaCreada(data=payload)
        self._publicar_mensaje(evento_integracion, topico, AvroSchema(EventoImagenMedicaCreada))

    def publicar_comando(self, comando, topico):
        # TODO Debe existir un forma de crear el Payload en Avro con base al tipo del comando
        payload = ComandoCrearImagenMedicaPayload(
            id_usuario=str(comando.id_usuario)
        )
        comando_integracion = ComandoCrearImagenMedica(data=payload)
        self._publicar_mensaje(comando_integracion, topico, AvroSchema(ComandoCrearImagenMedica))
