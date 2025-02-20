from app.seedwork.aplicacion.servicios import Servicio
from app.modulos.recursos.dominio.entidades import Recurso
from app.modulos.recursos.dominio.fabricas import FabricaVuelos
from app.modulos.recursos.infraestructura.fabricas import FabricaRepositorio
from app.modulos.recursos.infraestructura.repositorios import RepositorioRecursos
from .mapeadores import MapeadorReserva

from .dto import RecursoDTO

class ServicioReserva(Servicio):

    def __init__(self):
        self._fabrica_repositorio: FabricaRepositorio = FabricaRepositorio()
        self._fabrica_vuelos: FabricaVuelos = FabricaVuelos()

    @property
    def fabrica_repositorio(self):
        return self._fabrica_repositorio
    
    @property
    def fabrica_vuelos(self):
        return self._fabrica_vuelos

    def crear_recurso(self, reserva_dto: RecursoDTO) -> RecursoDTO:
        recurso: Recurso = self.fabrica_vuelos.crear_objeto(reserva_dto, MapeadorReserva())

        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioRecursos.__class__)
        repositorio.agregar(recurso)

        return self.fabrica_vuelos.crear_objeto(recurso, MapeadorReserva())

    def obtener_recurso_por_id(self, id) -> RecursoDTO:
        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioRecursos.__class__)
        return repositorio.obtener_por_id(id).__dict__

