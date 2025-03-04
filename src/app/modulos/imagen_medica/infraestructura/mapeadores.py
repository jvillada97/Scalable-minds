""" Mapeadores para la capa de infrastructura del dominio de vuelos

En este archivo usted encontrará los diferentes mapeadores
encargados de la transformación entre formatos de dominio y DTOs

"""

from app.seedwork.dominio.repositorios import Mapeador
from app.modulos.imagen_medica.dominio.entidades import ImagenMedica
from app.modulos.imagen_medica.infraestructura.dto import ImagenMedica as ImagenMedicaDTO
from app.modulos.imagen_medica.dominio.eventos import EventoImagenMedica, ImagenMedicaCreada
from app.seedwork.infraestructura.utils import unix_time_millis

class MapeadorReserva(Mapeador):
    _FORMATO_FECHA = '%Y-%m-%dT%H:%M:%SZ'   

    def obtener_tipo(self) -> type:
        return ImagenMedica.__class__

    def entidad_a_dto(self, entidad: ImagenMedica) -> ImagenMedicaDTO:
        
        reserva_dto = ImagenMedicaDTO()
        reserva_dto.url_imagen = entidad.url_imagen
        return reserva_dto

    def dto_a_entidad(self, dto: ImagenMedicaDTO) -> ImagenMedica:
        reserva = ImagenMedica(dto.url_imagen)   
        
        return reserva
    
class MapadeadorEventosImagenMedica(Mapeador):

    # Versiones aceptadas
    versions = ('v1',)

    LATEST_VERSION = versions[0]

    def __init__(self):
        self.router = {
            ImagenMedicaCreada: self._entidad_a_reserva_creada,
        }

    def obtener_tipo(self) -> type:
        return EventoImagenMedica.__class__

    def es_version_valida(self, version):
        for v in self.versions:
            if v == version:
                return True
        return False

    def _entidad_a_reserva_creada(self, entidad: ImagenMedicaCreada, version=LATEST_VERSION):
        def v1(evento):
            from .schema.v1.eventos import ImagenMedicaCreadaPayload, EventoImagenMedicaCreada

            payload = ImagenMedicaCreadaPayload(
                id=str(evento.id), 
                url_imagen=str(evento.url_imagen),                 
                fecha_creacion=int(unix_time_millis(evento.fecha_creacion))
            )
            evento_integracion = EventoImagenMedicaCreada(id=str(evento.id))
            evento_integracion.id = str(evento.id)
            evento_integracion.time = int(unix_time_millis(evento.fecha_creacion))
            evento_integracion.specversion = str(version)
            evento_integracion.type = 'ImagenMedicaCreada'
            evento_integracion.datacontenttype = 'AVRO'
            evento_integracion.service_name = 'app'
            evento_integracion.data = payload

            return evento_integracion
                    
        if not self.es_version_valida(version):
            raise Exception(f'No se sabe procesar la version {version}')

        if version == 'v1':
             return v1(entidad)   
         
    def entidad_a_dto(self, entidad: EventoImagenMedica) -> dict:
        # Implementa la lógica para convertir una entidad a DTO
        return {
            'id': str(entidad.id),
            'url_imagen': str(entidad.url_imagen),           
        }

    def dto_a_entidad(self, dto: dict) -> EventoImagenMedica:
        # Implementa la lógica para convertir un DTO a entidad
        return EventoImagenMedica(
            id=dto['id'],
            url_imagen=dto['url_imagen'],
          
        )