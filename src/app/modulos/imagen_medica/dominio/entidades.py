"""Entidades del dominio de cliente

En este archivo usted encontrará las entidades del dominio de cliente

"""

from datetime import datetime
from app.seedwork.dominio.entidades import Entidad, AgregacionRaiz
from dataclasses import dataclass, field
from app.modulos.imagen_medica.dominio.objetos_valor import TipoArchivo, Archivo, Etiqueta, Patologia, Modalidad


from .eventos import ImagenMedicaCreada


@dataclass
class Diagnostico(Entidad):
    etiqueta: Etiqueta = field(default_factory=Etiqueta)
    modalidad: Modalidad = field(default_factory=Modalidad)
    patologia: Patologia = field(default_factory=Patologia)

@dataclass
class ImagenMedica(AgregacionRaiz):
    url_imagen: str = ""
    # tipoArchivo: TipoArchivo = field(default_factory=TipoArchivo)
    # archivo: Archivo = field(default_factory=Archivo)
    # diagnostico: Diagnostico = field(default_factory=Diagnostico)
    def crear_propiedad(self, propiedad: "ImagenMedica"):
        self.url_imagen = propiedad.url_imagen,   
        self.id = propiedad.id

        self.agregar_evento(ImagenMedicaCreada(
            url_imagen = str(self.url_imagen),  
            id=str(self.id) 
        )
    )
