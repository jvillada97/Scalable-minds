"""Entidades del dominio de cliente

En este archivo usted encontrará las entidades del dominio de cliente

"""

from datetime import datetime
from app.seedwork.dominio.entidades import Entidad
from dataclasses import dataclass, field

from .objetos_valor import Nombre, Email, Direccion

@dataclass
class Provedor(Entidad):
    nombre: Nombre = field(default_factory=Nombre)
    email: Email = field(default_factory=Email)
    direccion: Direccion = field(default_factory=Direccion)
