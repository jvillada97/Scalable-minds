""" Fábricas para la creación de objetos en la capa de infrastructura del dominio de vuelos

En este archivo usted encontrará las diferentes fábricas para crear
objetos complejos en la capa de infraestructura del dominio de vuelos

"""

from dataclasses import dataclass, field
from app.seedwork.dominio.fabricas import Fabrica
from app.seedwork.dominio.repositorios import Repositorio
from app.modulos.recursos.dominio.repositorios import  RepositorioRecursos
from .repositorios import RepositorioReservasSQLite
from .excepciones import ExcepcionFabrica

@dataclass
class FabricaRepositorio(Fabrica):
    def crear_objeto(self, obj: type, mapeador: any = None) -> Repositorio:
        if obj == RepositorioRecursos.__class__:
            return RepositorioReservasSQLite()       
        else:
            raise ExcepcionFabrica()