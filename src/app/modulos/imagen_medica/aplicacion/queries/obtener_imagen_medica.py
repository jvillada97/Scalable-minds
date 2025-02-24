from app.seedwork.aplicacion.queries import Query, QueryHandler, QueryResultado
from app.seedwork.aplicacion.queries import ejecutar_query as query
from app.modulos.imagen_medica.infraestructura.repositorios import RepositorioImagenMedicas
from dataclasses import dataclass
from .base import ReservaQueryBaseHandler
from app.modulos.imagen_medica.aplicacion.mapeadores import MapeadorImagenMedica
import uuid

@dataclass
class ObtenerReserva(Query):
    id: str

class ObtenerReservaHandler(ReservaQueryBaseHandler):

    def handle(self, query: ObtenerReserva) -> QueryResultado:
        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioImagenMedicas.__class__)
        reserva =  self.fabrica_imagen_medica.crear_objeto(repositorio.obtener_por_id(query.id), MapeadorImagenMedica())
        return QueryResultado(resultado=reserva)

@query.register(ObtenerReserva)
def ejecutar_query_obtener_reserva(query: ObtenerReserva):
    handler = ObtenerReservaHandler()
    return handler.handle(query)