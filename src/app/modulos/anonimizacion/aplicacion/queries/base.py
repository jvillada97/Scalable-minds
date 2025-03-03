from app.seedwork.aplicacion.queries import QueryHandler
from app.modulos.anonimizacion.infraestructura.fabricas import FabricaVista
from app.modulos.anonimizacion.dominio.fabricas import FabricaAnonimizacion

class AnonimizacionQueryBaseHandler(QueryHandler):
    def __init__(self):
        self._fabrica_vista: FabricaVista = FabricaVista()
        self._fabrica_anonimizacion: FabricaAnonimizacion = FabricaAnonimizacion()

    @property
    def fabrica_repositorio(self):
        return self._fabrica_vista
    
    @property
    def fabrica_anonimizacion(self):
        return self._fabrica_anonimizacion    