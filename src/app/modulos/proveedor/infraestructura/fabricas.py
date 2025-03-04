from dataclasses import dataclass
from app.seedwork.dominio.fabricas import Fabrica
from app.seedwork.dominio.repositorios import Repositorio
from app.modulos.proveedor.dominio.repositorios import RepositorioProveedor, RepositorioEventosProveedor
from app.modulos.proveedor.infraestructura.repositorios import RepositorioProveedorsSQLite, RepositorioEventosProveedorSQLAlchemy
from app.modulos.proveedor.infraestructura.excepciones import ExcepcionFabrica
from app.modulos.proveedor.dominio.entidades import Proveedor
from app.seedwork.infraestructura.vistas import Vista

@dataclass
class FabricaRepositorio(Fabrica):
    def crear_objeto(self, obj: type, mapeador: any = None) -> Repositorio:
        if obj == RepositorioProveedor:
            return RepositorioProveedorsSQLite()
        elif obj == RepositorioEventosProveedor:
            return RepositorioEventosProveedorSQLAlchemy()
        else:
            raise ExcepcionFabrica(mensaje=f'No existe una implementación para el repositorio con el tipo {obj}')
        
@dataclass
class FabricaVista(Fabrica):
    def crear_objeto(self, obj: type, mapeador: any = None) -> Vista:
        if obj == Proveedor:
            return RepositorioProveedorsSQLite()
        else:
            raise ExcepcionFabrica(mensaje=f'No existe fábrica para el objeto {obj}')