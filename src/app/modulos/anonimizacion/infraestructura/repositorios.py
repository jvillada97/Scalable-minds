""" Repositorios para el manejo de persistencia de objetos de dominio en la capa de infrastructura del dominio de vuelos

En este archivo usted encontrará las diferentes repositorios para
persistir objetos dominio (agregaciones) en la capa de infraestructura del dominio de vuelos

"""

from app.config.db import db
from app.modulos.anonimizacion.dominio.repositorios import RepositorioAnonimizacions, RepositorioEventosAnonimizacions
from app.modulos.anonimizacion.infraestructura.dto import Anonimizacion, EventosAnonimizacion
from app.modulos.anonimizacion.dominio.fabricas import FabricaAnonimizacion
from app.modulos.anonimizacion.infraestructura.dto import Anonimizacion as AnonimizacionDTO
from app.modulos.anonimizacion.infraestructura.mapeadores import MapeadorReserva, MapadeadorEventosAnonimizacion
from uuid import UUID

class RepositorioAnonimizacionsSQLite(RepositorioAnonimizacions):

    def __init__(self):
        self._fabrica_imagenes: FabricaAnonimizacion = FabricaAnonimizacion()

    @property
    def fabrica_imagenes(self):
        return self._fabrica_imagenes

    def obtener_por_id(self, id: UUID) -> Anonimizacion:
        reserva_dto = db.session.query(AnonimizacionDTO).filter_by(id=str(id)).one()
        return self.fabrica_imagenes.crear_objeto(reserva_dto, MapeadorReserva())

    def obtener_todos(self) -> list[Anonimizacion]:
        companias_list = db.session.query(Anonimizacion).all()
        return companias_list

    def agregar(self, reserva: Anonimizacion):
        reserva_dto = self.fabrica_imagenes.crear_objeto(reserva, MapeadorReserva())
        db.session.add(reserva_dto)
        db.session.commit()

    def actualizar(self, reserva: Anonimizacion):
        # TODO
        raise NotImplementedError

    def eliminar(self, reserva_id: UUID):
        # TODO
        raise NotImplementedError
class RepositorioEventosAnonimizacionSQLAlchemy(RepositorioEventosAnonimizacions):

    def __init__(self):
        self._fabrica_vuelos: FabricaAnonimizacion = FabricaAnonimizacion()

    @property
    def fabrica_vuelos(self):
        return self._fabrica_vuelos

    def obtener_por_id(self, id: UUID) -> Anonimizacion:
        reserva_dto = db.session.query(AnonimizacionDTO).filter_by(id=str(id)).one()
        return self.fabrica_vuelos.crear_objeto(reserva_dto, MapadeadorEventosAnonimizacion())

    def obtener_todos(self) -> list[Anonimizacion]:
        raise NotImplementedError

    def agregar(self, evento):
        reserva_evento = self.fabrica_vuelos.crear_objeto(evento, MapadeadorEventosAnonimizacion())

        parser_payload = JsonSchema(reserva_evento.data.__class__)
        json_str = parser_payload.encode(reserva_evento.data)

        evento_dto = EventosAnonimizacion()
        evento_dto.id = str(evento.id)
        evento_dto.id_entidad = str(evento.id_reserva)
        evento_dto.fecha_evento = evento.fecha_creacion
        evento_dto.version = str(reserva_evento.specversion)
        evento_dto.tipo_evento = evento.__class__.__name__
        evento_dto.formato_contenido = 'JSON'
        evento_dto.nombre_servicio = str(reserva_evento.service_name)
        evento_dto.contenido = json_str

        db.session.add(evento_dto)

    def actualizar(self, reserva: Anonimizacion):
        raise NotImplementedError

    def eliminar(self, reserva_id: UUID):
        raise NotImplementedError
