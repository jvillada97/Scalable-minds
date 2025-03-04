""" Repositorios para el manejo de persistencia de objetos de dominio en la capa de infrastructura del dominio de vuelos

En este archivo usted encontrará las diferentes repositorios para
persistir objetos dominio (agregaciones) en la capa de infraestructura del dominio de vuelos

"""

from app.config.db import db
from app.modulos.proveedor.dominio.repositorios import RepositorioProveedor, RepositorioEventosProveedor
from app.modulos.proveedor.infraestructura.dto import Proveedor, EventosProveedor
from app.modulos.proveedor.dominio.fabricas import FabricaProveedor
from app.modulos.proveedor.infraestructura.dto import Proveedor as ProveedorDTO
from app.modulos.proveedor.infraestructura.mapeadores import MapeadorProveedor, MapadeadorEventosProveedor
from uuid import UUID
import uuid
from pulsar.schema import JsonSchema
from datetime import datetime
class RepositorioProveedorsSQLite(RepositorioProveedor): 

    def __init__(self):
        self._fabrica_imagenes: FabricaProveedor = FabricaProveedor()

    @property
    def fabrica_imagenes(self):
        return self._fabrica_imagenes

    def obtener_por_id(self, id: UUID) -> Proveedor:
        reserva_dto = db.session.query(ProveedorDTO).filter_by(id=str(id)).one()
        return self.fabrica_imagenes.crear_objeto(reserva_dto, MapeadorProveedor())

    def obtener_todos(self) -> list[Proveedor]:
        companias_list = db.session.query(Proveedor).all()
        return companias_list

    def agregar(self, reserva: Proveedor):
        reserva_dto = self.fabrica_imagenes.crear_objeto(reserva, MapeadorProveedor())
        db.session.add(reserva_dto)
        db.session.commit()

    def actualizar(self, reserva: Proveedor):
        # TODO
        raise NotImplementedError

    def eliminar(self, reserva_id: UUID):
        # TODO
        raise NotImplementedError
    
class RepositorioEventosProveedorSQLAlchemy(RepositorioEventosProveedor):

    def __init__(self):
        self._fabrica_vuelos: FabricaProveedor = FabricaProveedor()

    @property
    def fabrica_vuelos(self):
        return self._fabrica_vuelos

    def obtener_por_id(self, id: UUID) -> Proveedor:
        reserva_dto = db.session.query(ProveedorDTO).filter_by(id=str(id)).one()
        return self.fabrica_vuelos.crear_objeto(reserva_dto, MapadeadorEventosProveedor())

    def obtener_todos(self) -> list[Proveedor]:
        raise NotImplementedError

    def agregar(self, evento):
        reserva_evento = self.fabrica_vuelos.crear_objeto(evento, MapadeadorEventosProveedor())
        print(reserva_evento)       
       
        evento_dto = EventosProveedor()
        evento_dto.id = str(uuid.uuid4())  
        evento_dto.id_entidad = str(evento.id)
        evento_dto.fecha_evento = datetime.now()
        evento_dto.tipo_evento = evento.__class__.__name__
        evento_dto.formato_contenido = 'JSON'
        evento_dto.contenido = ''

        db.session.add(evento_dto)
        
    def actualizar(self, reserva: Proveedor):
        raise NotImplementedError

    def eliminar(self, reserva_id: UUID):
        raise NotImplementedError
