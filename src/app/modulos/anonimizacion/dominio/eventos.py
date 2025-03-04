from __future__ import annotations
from dataclasses import dataclass, field
from app.seedwork.dominio.eventos import (EventoDominio)
from datetime import datetime
import uuid

class EventoAnonimizacion(EventoDominio):
    ...
@dataclass
class AnonimizacionCreada(EventoAnonimizacion):
    id: uuid.UUID = None
    url_imagen: str = None