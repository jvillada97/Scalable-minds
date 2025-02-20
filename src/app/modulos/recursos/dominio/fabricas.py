""" Fábricas para la creación de objetos del dominio de vuelos

En este archivo usted encontrará las diferentes fábricas para crear
objetos complejos del dominio de vuelos

"""

from .entidades import Recurso
from .reglas import MinimoUnItinerario, RutaValida
from .excepciones import TipoObjetoNoExisteEnDominioRecursosExcepcion
from app.seedwork.dominio.repositorios import Mapeador, Repositorio
from app.seedwork.dominio.fabricas import Fabrica
from app.seedwork.dominio.entidades import Entidad
from dataclasses import dataclass

@dataclass
class FabricaVuelos(Fabrica):
     def crear_objeto(self, obj: any, mapeador: Mapeador) -> any:
        if isinstance(obj, Entidad):
            return mapeador.entidad_a_dto(obj)
        else:
            recurso: Recurso = mapeador.dto_a_entidad(obj)          
            return recurso

