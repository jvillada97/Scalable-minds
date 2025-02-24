from __future__ import annotations
from dataclasses import dataclass, field
from app.seedwork.dominio.eventos import (EventoDominio)
from datetime import datetime

@dataclass
class ImagenMedicaCreada(EventoDominio):
    id_reserva: uuid.UUID = None
    url_image: datetime = None