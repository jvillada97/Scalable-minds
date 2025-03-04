""" Repositorios para el manejo de persistencia de objetos de dominio en la capa de infrastructura del dominio de vuelos

En este archivo usted encontrará las diferentes repositorios para
persistir objetos dominio (agregaciones) en la capa de infraestructura del dominio de vuelos

"""

from app.config.db import db
from app.modulos.imagen_medica.dominio.repositorios import RepositorioImagenMedicas, RepositorioEventosImagenMedicas
from app.modulos.imagen_medica.infraestructura.dto import ImagenMedica, EventosImagenMedica
from app.modulos.imagen_medica.dominio.fabricas import FabricaImagenMedica
from app.modulos.imagen_medica.infraestructura.dto import ImagenMedica as ImagenMedicaDTO
from app.modulos.imagen_medica.infraestructura.mapeadores import MapeadorReserva, MapadeadorEventosImagenMedica
from uuid import UUID
import uuid
from datetime import datetime
from pulsar.schema import JsonSchema
class RepositorioImagenMedicasSQLite(RepositorioImagenMedicas):

    def __init__(self):
        self._fabrica_imagenes: FabricaImagenMedica = FabricaImagenMedica()

    @property
    def fabrica_imagenes(self):
        return self._fabrica_imagenes

    def obtener_por_id(self, id: UUID) -> ImagenMedica:
        reserva_dto = db.session.query(ImagenMedicaDTO).filter_by(id=str(id)).one()
        return self.fabrica_imagenes.crear_objeto(reserva_dto, MapeadorReserva())

    def obtener_todos(self) -> list[ImagenMedica]:
        companias_list = db.session.query(ImagenMedica).all()
        return companias_list

    def agregar(self, reserva: ImagenMedica):
        reserva_dto = self.fabrica_imagenes.crear_objeto(reserva, MapeadorReserva())
        db.session.add(reserva_dto)
        db.session.commit()

    def actualizar(self, reserva: ImagenMedica):
        # TODO
        raise NotImplementedError

    def eliminar(self, reserva_id: UUID):
        # TODO
        raise NotImplementedError

class RepositorioEventosImagenMedicaSQLAlchemy(RepositorioEventosImagenMedicas):

    def __init__(self):
        self._fabrica_vuelos: FabricaImagenMedica = FabricaImagenMedica()

    @property
    def fabrica_vuelos(self):
        return self._fabrica_vuelos

    def obtener_por_id(self, id: UUID) -> ImagenMedica:
        reserva_dto = db.session.query(ImagenMedicaDTO).filter_by(id=str(id)).one()
        return self.fabrica_vuelos.crear_objeto(reserva_dto, MapadeadorEventosImagenMedica())

    def obtener_todos(self) -> list[ImagenMedica]:
        raise NotImplementedError

    def agregar(self, evento):
        reserva_evento = self.fabrica_vuelos.crear_objeto(evento, MapadeadorEventosImagenMedica())
        
        evento_dto = EventosImagenMedica()
        evento_dto.id = str(uuid.uuid4())  
        evento_dto.id_entidad = str(evento.id)
        evento_dto.fecha_evento = datetime.now()
        evento_dto.tipo_evento = evento.__class__.__name__
        evento_dto.formato_contenido = 'JSON'
        evento_dto.contenido = '' 
        
        db.session.add(evento_dto)

    def actualizar(self, reserva: ImagenMedica):
        raise NotImplementedError

    def eliminar(self, reserva_id: UUID):
        raise NotImplementedError
