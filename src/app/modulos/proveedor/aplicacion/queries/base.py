from app.seedwork.aplicacion.queries import QueryHandler
from app.modulos.proveedor.infraestructura.fabricas import FabricaVista
from app.modulos.proveedor.dominio.fabricas import FabricaProveedor

class ProveedorQueryBaseHandler(QueryHandler):
    def __init__(self):
        self._fabrica_vista: FabricaVista = FabricaVista()
        self._fabrica_proveedor: FabricaProveedor = FabricaProveedor()

    @property
    def fabrica_repositorio(self):
        return self._fabrica_vista
    
    @property
    def fabrica_proveedor(self):
        return self._fabrica_proveedor    