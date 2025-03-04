"""Entidades del dominio de cliente

En este archivo usted encontrará las entidades del dominio de cliente

"""

from datetime import datetime
from app.seedwork.dominio.entidades import Entidad, AgregacionRaiz
from dataclasses import dataclass, field
from app.modulos.anonimizacion.dominio.objetos_valor import TipoArchivo, Archivo, Etiqueta, Patologia, Modalidad


from .eventos import AnonimizacionCreada


@dataclass
class Diagnostico(Entidad):
    etiqueta: Etiqueta = field(default_factory=Etiqueta)
    modalidad: Modalidad = field(default_factory=Modalidad)
    patologia: Patologia = field(default_factory=Patologia)

@dataclass
class Anonimizacion(AgregacionRaiz):
    url_imagen: str = ""   
    def crear_propiedad(self, propiedad: "Anonimizacion"):
        self.url_imagen = propiedad.url_imagen,  

        self.agregar_evento(AnonimizacionCreada(id= self.id, url_imagen=self.url_imagen)
    )
