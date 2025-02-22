"""Entidades del dominio de cliente

En este archivo usted encontrará las entidades del dominio de cliente

"""

from datetime import datetime
from app.seedwork.dominio.entidades import Entidad
from dataclasses import dataclass, field

from .objetos_valor import TipoArchivo, Archivo, Etiqueta, Patologia, Modalidad


    
@dataclass
class Diagnostico(Entidad):
    etiqueta: Etiqueta = field(default_factory=Etiqueta)
    modalidad: Modalidad = field(default_factory=Modalidad)
    patologia: Patologia = field(default_factory=Patologia)
    
@dataclass
class ImagenMedica(Entidad):
    tipoArchivo: TipoArchivo = field(default_factory=TipoArchivo)
    archivo: Archivo = field(default_factory=Archivo)
    diagnostico: Diagnostico = field(default_factory=Diagnostico)