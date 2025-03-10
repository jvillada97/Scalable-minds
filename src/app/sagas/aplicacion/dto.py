from dataclasses import field
from seedwork.aplicacion.dto import DTO
import uuid


class ProveedorDTO(DTO):
    name: str = field(default_factory=str)   

