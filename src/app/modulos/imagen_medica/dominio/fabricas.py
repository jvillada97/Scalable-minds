""" Fábricas para la creación de objetos del dominio de vuelos

En este archivo usted encontrará las diferentes fábricas para crear
objetos complejos del dominio de vuelos

"""

from app.modulos.imagen_medica.dominio.entidades import ImagenMedica
from app.modulos.imagen_medica.dominio.excepciones import TipoObjetoNoExisteEnDominioImagenMedicasExcepcion
from app.seedwork.dominio.repositorios import Mapeador, Repositorio
from app.seedwork.dominio.fabricas import Fabrica
from app.seedwork.dominio.entidades import Entidad
from dataclasses import dataclass
from app.seedwork.infraestructura.vistas import Vista
@dataclass
class FabricaImagenMedica(Fabrica):
    def crear_objeto(self, obj: any, mapeador: Mapeador) -> any:
        if isinstance(obj, Entidad):
            return mapeador.entidad_a_dto(obj)
        else:
            compania: ImagenMedica = mapeador.dto_a_entidad(obj)
            return compania

