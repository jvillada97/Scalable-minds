""" Mapeadores para la capa de infrastructura del dominio de vuelos

En este archivo usted encontrará los diferentes mapeadores
encargados de la transformación entre formatos de dominio y DTOs

"""

from app.seedwork.dominio.repositorios import Mapeador
from app.modulos.anonimizacion.dominio.objetos_valor import Archivo, TipoArchivo, Etiqueta,Patologia,Modalidad
from app.modulos.anonimizacion.dominio.entidades import Anonimizacion
from app.modulos.anonimizacion.infraestructura.dto import Anonimizacion as AnonimizacionDTO
from app.modulos.anonimizacion.dominio.eventos import AnonimizacionCreada, EventoAnonimizacion

from app.seedwork.infraestructura.utils import unix_time_millis

class MapeadorReserva(Mapeador):
    _FORMATO_FECHA = '%Y-%m-%dT%H:%M:%SZ'   

    def obtener_tipo(self) -> type:
        return Anonimizacion.__class__

    def entidad_a_dto(self, entidad: Anonimizacion) -> AnonimizacionDTO:
        
        reserva_dto = AnonimizacionDTO()
        reserva_dto.url_imagen = entidad.url_imagen
        return reserva_dto

    def dto_a_entidad(self, dto: AnonimizacionDTO) -> Anonimizacion:
        reserva = Anonimizacion(dto.url_imagen)   
        
        return reserva
    
class MapadeadorEventosAnonimizacion(Mapeador):

    # Versiones aceptadas
    versions = ('v1',)

    LATEST_VERSION = versions[0]

    def __init__(self):
        self.router = {
            AnonimizacionCreada: self._entidad_a_reserva_creada,
        }

    def obtener_tipo(self) -> type:
        return EventoAnonimizacion.__class__

    def es_version_valida(self, version):
        for v in self.versions:
            if v == version:
                return True
        return False

    def _entidad_a_reserva_creada(self, entidad: AnonimizacionCreada, version=LATEST_VERSION):
        def v1(evento):
            from .schema.v1.eventos import AnonimizacionCreadaPayload, EventoAnonimizacionCreada

            payload = AnonimizacionCreadaPayload(
                id=str(evento.id), 
                url_imagen=str(evento.url_imagen),                 
                fecha_creacion=int(unix_time_millis(evento.fecha_creacion))
            )
            evento_integracion = EventoAnonimizacionCreada(id=str(evento.id))
            evento_integracion.id = str(evento.id)
            evento_integracion.time = int(unix_time_millis(evento.fecha_creacion))
            evento_integracion.specversion = str(version)
            evento_integracion.type = 'AnonimizacionCreada'
            evento_integracion.datacontenttype = 'AVRO'
            evento_integracion.service_name = 'app'
            evento_integracion.data = payload

            return evento_integracion
                    
        if not self.es_version_valida(version):
            raise Exception(f'No se sabe procesar la version {version}')

        if version == 'v1':
             return v1(entidad)   
         
        