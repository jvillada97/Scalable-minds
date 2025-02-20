"""Objetos valor del dominio de cliente

En este archivo usted encontrará los objetos valor del dominio de cliente

"""

from app.seedwork.dominio.objetos_valor import ObjetoValor
from dataclasses import dataclass

@dataclass(frozen=True)
class Nombre(ObjetoValor):
    nombres: str
    apellidos: str

@dataclass(frozen=True)
class Email(ObjetoValor):
    address: str
    dominio: str
    es_empresarial: bool


@dataclass(frozen=True)
class Direccion(ObjetoValor):
    ciudad: str
    pais: str
    direccion: str
