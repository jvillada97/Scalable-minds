"""Objetos valor del dominio de cliente

En este archivo usted encontrará los objetos valor del dominio de cliente

"""

from app.seedwork.dominio.objetos_valor import ObjetoValor
from dataclasses import dataclass

@dataclass(frozen=True)
class TipoArchivo(ObjetoValor):
    nombres: str
    extension: str

@dataclass(frozen=True)
class Archivo(ObjetoValor):
    identificador: str
    dominio: str

@dataclass(frozen=True)
class Etiqueta(ObjetoValor):
    identificador: str
    dominio: str
    
@dataclass(frozen=True)
class Patologia(ObjetoValor):
    nombre: str
    dominio: str
    
@dataclass(frozen=True)
class Modalidad(ObjetoValor):
    identificador: str
    dominio: str