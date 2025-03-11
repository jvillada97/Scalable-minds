from app.seedwork.aplicacion.comandos import ComandoHandler
from app.modulos.proveedor.infraestructura.fabricas import FabricaRepositorio
from app.modulos.proveedor.dominio.fabricas import FabricaProveedor

class CrearProveedorBaseHandler(ComandoHandler):
    def __init__(self):
        self._fabrica_repositorio: FabricaRepositorio = FabricaRepositorio()
        self._fabrica_proveedor: FabricaProveedor = FabricaProveedor()

    @property
    def fabrica_repositorio(self):
        return self._fabrica_repositorio
    
    @property
    def fabrica_proveedor(self):
        return self._fabrica_proveedor    
class EliminarProveedorBaseHandler(ComandoHandler):
    def __init__(self):
        self._fabrica_repositorio: FabricaRepositorio = FabricaRepositorio()
        self._fabrica_proveedor: FabricaProveedor = FabricaProveedor()

    @property
    def fabrica_repositorio(self):
        return self._fabrica_repositorio
    
    @property
    def fabrica_companias(self):
        return self._fabrica_proveedor   
       