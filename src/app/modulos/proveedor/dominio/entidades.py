"""Entidades del dominio de cliente

En este archivo usted encontrará las entidades del dominio de cliente

"""

from datetime import datetime
from app.seedwork.dominio.entidades import Entidad, AgregacionRaiz
from dataclasses import dataclass, field
from app.modulos.proveedor.dominio.objetos_valor import TipoArchivo, Archivo, Etiqueta, Patologia, Modalidad


from .eventos import ProveedorCreada

@dataclass
class Proveedor(AgregacionRaiz):
    name: str = ""
    # tipoArchivo: TipoArchivo = field(default_factory=TipoArchivo)
    # archivo: Archivo = field(default_factory=Archivo)
    # diagnostico: Diagnostico = field(default_factory=Diagnostico)
    def crear_propiedad(self, propiedad: "Proveedor"):
        self.name = propiedad.name,  

        self.agregar_evento(ProveedorCreada(id=self.id, name=self.name, fecha_creacion=datetime.now() )
    )
