from dataclasses import dataclass, field
from app.seedwork.aplicacion.dto import DTO
    
@dataclass(frozen=True)
class ProveedorDTO(DTO):
    name: str = field(default_factory=str)