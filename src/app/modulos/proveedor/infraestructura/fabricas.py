""" Fábricas para la creación de objetos en la capa de infrastructura del dominio de vuelos

En este archivo usted encontrará las diferentes fábricas para crear
objetos complejos en la capa de infraestructura del dominio de vuelos

"""

from dataclasses import dataclass, field
from app.seedwork.dominio.fabricas import Fabrica
from app.seedwork.dominio.repositorios import Repositorio
from app.modulos.proveedor.dominio.repositorios import  RepositorioProveedors
from app.modulos.proveedor.infraestructura.repositorios import RepositorioProveedorsSQLite
from app.modulos.proveedor.infraestructura.excepciones import ExcepcionFabrica
from app.modulos.proveedor.dominio.entidades import Proveedor
from app.seedwork.infraestructura.vistas import Vista

@dataclass
class FabricaRepositorio(Fabrica):
    
    def crear_objeto(self, obj: type, mapeador: any = None) -> Repositorio:
        if obj == RepositorioProveedors.__class__:
            return RepositorioProveedorsSQLite()       
        else:
            raise ExcepcionFabrica()
        
                
@dataclass
class FabricaVista(Fabrica):
    def crear_objeto(self, obj: type, mapeador: any = None) -> Vista:
        if obj == Proveedor:
            return RepositorioProveedorsSQLite()
        else:
            raise ExcepcionFabrica(f'No existe fábrica para el objeto {obj}')