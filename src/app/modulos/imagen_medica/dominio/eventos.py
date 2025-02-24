from __future__ import annotations
from dataclasses import dataclass, field
from app.seedwork.dominio.eventos import (EventoDominio)
from datetime import datetime
import uuid

@dataclass
class ImagenMedicaCreada(EventoDominio):
    id: uuid.UUID = None
    url_image: str = None