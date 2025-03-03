""" Fábricas para la creación de objetos del dominio de vuelos

En este archivo usted encontrará las diferentes fábricas para crear
objetos complejos del dominio de vuelos

"""

from app.modulos.anonimizacion.dominio.entidades import Anonimizacion
from app.modulos.anonimizacion.dominio.excepciones import TipoObjetoNoExisteEnDominioAnonimizacionsExcepcion
from app.seedwork.dominio.repositorios import Mapeador, Repositorio
from app.seedwork.dominio.fabricas import Fabrica
from app.seedwork.dominio.entidades import Entidad
from dataclasses import dataclass
from app.seedwork.infraestructura.vistas import Vista
@dataclass
class FabricaAnonimizacion(Fabrica):
    def crear_objeto(self, obj: any, mapeador: Mapeador) -> any:
        if isinstance(obj, Entidad):
            return mapeador.entidad_a_dto(obj)
        else:
            compania: Anonimizacion = mapeador.dto_a_entidad(obj)
            return compania

