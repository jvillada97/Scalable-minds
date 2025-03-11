from __future__ import annotations
from dataclasses import dataclass, field
from app.seedwork.dominio.eventos import (EventoDominio)
from datetime import datetime
import uuid
class EventoProveedor(EventoDominio):
    ...

    
@dataclass
class ProveedorCreada(EventoProveedor):
    id: uuid.UUID = None
    name: str = None
    
@dataclass
class ProveedorEliminada(EventoDominio):
     name: str = None   