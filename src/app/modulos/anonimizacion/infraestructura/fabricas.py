""" Fábricas para la creación de objetos en la capa de infrastructura del dominio de vuelos

En este archivo usted encontrará las diferentes fábricas para crear
objetos complejos en la capa de infraestructura del dominio de vuelos

"""

from dataclasses import dataclass, field
from app.seedwork.dominio.fabricas import Fabrica
from app.seedwork.dominio.repositorios import Repositorio
from app.modulos.anonimizacion.dominio.repositorios import  RepositorioAnonimizacions, RepositorioEventosAnonimizacions
from app.modulos.anonimizacion.infraestructura.repositorios import RepositorioAnonimizacionsSQLite, RepositorioEventosAnonimizacionSQLAlchemy
from app.modulos.anonimizacion.infraestructura.excepciones import ExcepcionFabrica
from app.modulos.anonimizacion.dominio.entidades import Anonimizacion
from app.seedwork.infraestructura.vistas import Vista

@dataclass
class FabricaRepositorio(Fabrica):    
        
    def crear_objeto(self, obj: type, mapeador: any = None) -> Repositorio:
        if obj == RepositorioAnonimizacions:
            return RepositorioAnonimizacionsSQLite()
        elif obj == RepositorioEventosAnonimizacions:
            return RepositorioEventosAnonimizacionSQLAlchemy()
        else:
            raise ExcepcionFabrica(mensaje=f'No existe una implementación para el repositorio con el tipo {obj}')           
@dataclass
class FabricaVista(Fabrica):
    def crear_objeto(self, obj: type, mapeador: any = None) -> Vista:
        if obj == Anonimizacion:
            return RepositorioAnonimizacionsSQLite()
        else:
            raise ExcepcionFabrica(f'No existe fábrica para el objeto {obj}')