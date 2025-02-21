""" Repositorios para el manejo de persistencia de objetos de dominio en la capa de infrastructura del dominio de vuelos

En este archivo usted encontrará las diferentes repositorios para
persistir objetos dominio (agregaciones) en la capa de infraestructura del dominio de vuelos

"""

from app.config.db import db
from app.modulos.imagen_medica.dominio.repositorios import RepositorioImagenMedicas, RepositorioProveedores
from app.modulos.imagen_medica.dominio.objetos_valor import NombreAero, Odo, Leg, Segmento, Itinerario, CodigoIATA
from app.modulos.imagen_medica.dominio.entidades import ImagenMedica, Diagnostico
from app.modulos.imagen_medica.dominio.fabricas import FabricaImagenMedica
from .dto import ImagenMedica as ImagenMedicaDTO
from .mapeadores import MapeadorReserva
from uuid import UUID

class RepositorioImagenMedicasSQLite(RepositorioImagenMedicas):

    def __init__(self):
        self._fabrica_vuelos: FabricaImagenMedica = FabricaImagenMedica()

    @property
    def fabrica_vuelos(self):
        return self._fabrica_vuelos

    def obtener_por_id(self, id: UUID) -> ImagenMedica:
        reserva_dto = db.session.query(ImagenMedicaDTO).filter_by(id=str(id)).one()
        return self.fabrica_vuelos.crear_objeto(reserva_dto, MapeadorReserva())

    def obtener_todos(self) -> list[ImagenMedica]:
        # TODO
        raise NotImplementedError

    def agregar(self, reserva: ImagenMedica):
        reserva_dto = self.fabrica_vuelos.crear_objeto(reserva, MapeadorReserva())
        db.session.add(reserva_dto)
        db.session.commit()

    def actualizar(self, reserva: ImagenMedica):
        # TODO
        raise NotImplementedError

    def eliminar(self, reserva_id: UUID):
        # TODO
        raise NotImplementedError