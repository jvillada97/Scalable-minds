""" Mapeadores para la capa de infrastructura del dominio de vuelos

En este archivo usted encontrará los diferentes mapeadores
encargados de la transformación entre formatos de dominio y DTOs

"""

from app.seedwork.dominio.repositorios import Mapeador
from app.modulos.proveedor.dominio.entidades import Proveedor
from app.modulos.proveedor.infraestructura.dto import Proveedor as ProveedorDTO
from app.modulos.proveedor.dominio.eventos import ProveedorCreada, EventoProveedor
from app.seedwork.infraestructura.utils import unix_time_millis

class MapeadorProveedor(Mapeador):
    _FORMATO_FECHA = '%Y-%m-%dT%H:%M:%SZ'   

    def obtener_tipo(self) -> type:
        return Proveedor.__class__

    def entidad_a_dto(self, entidad: Proveedor) -> ProveedorDTO:
        
        proveedor_dto = ProveedorDTO()
        proveedor_dto.url_imagen = entidad.url_imagen
        return proveedor_dto

    def dto_a_entidad(self, dto: ProveedorDTO) -> Proveedor:
        proveedor = Proveedor(dto.url_imagen)   
        
        return proveedor
class MapadeadorEventosProveedor(Mapeador):

    # Versiones aceptadas
    versions = ('v1',)

    LATEST_VERSION = versions[0]

    def __init__(self):
        self.router = {
            ProveedorCreada: self._entidad_a_reserva_creada,
        }

    def obtener_tipo(self) -> type:
        return EventoProveedor.__class__

    def es_version_valida(self, version):
        for v in self.versions:
            if v == version:
                return True
        return False

    def _entidad_a_reserva_creada(self, entidad: ProveedorCreada, version=LATEST_VERSION):
        def v1(evento):
            from .schema.v1.eventos import ProveedorCreadaPayload, EventoProveedorCreada

            payload = ProveedorCreadaPayload(
                id=str(evento.id), 
                name=str(evento.name),                 
                fecha_creacion=int(unix_time_millis(evento.fecha_creacion))
            )
            evento_integracion = EventoProveedorCreada(id=str(evento.id))
            evento_integracion.id = str(evento.id)
            evento_integracion.time = int(unix_time_millis(evento.fecha_creacion))
            evento_integracion.specversion = str(version)
            evento_integracion.type = 'ProveedorCreada'
            evento_integracion.datacontenttype = 'AVRO'
            evento_integracion.service_name = 'app'
            evento_integracion.data = payload

            return evento_integracion
                    
        if not self.es_version_valida(version):
            raise Exception(f'No se sabe procesar la version {version}')

        if version == 'v1':
             return v1(entidad)   
         
        