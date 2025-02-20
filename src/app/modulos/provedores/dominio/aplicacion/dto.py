from dataclasses import dataclass, field
from app.seedwork.aplicacion.dto import DTO

@dataclass(frozen=True)
class ProvedorDTO(DTO):
    fecha_salida: str
    fecha_llegada: str
    origen: dict
    destino: dict

