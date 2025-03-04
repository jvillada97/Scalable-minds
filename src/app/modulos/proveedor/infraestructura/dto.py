"""DTOs para la capa de infraestructura del dominio de imagen médica

En este archivo usted encontrará los DTOs (modelos anémicos) de
la infraestructura del dominio de imagen médica

"""

from app.config.db import db
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, ForeignKey, Integer, Table, DateTime, String

import uuid

Base = db.declarative_base()


class Proveedor(db.Model):
    __tablename__ = "proveedor"
    id = db.Column(db.String, primary_key=True, default=lambda: str(uuid.uuid4()))
    name = db.Column(db.String, nullable=False)

class EventosProveedor(db.Model):
    __tablename__ = "eventos_proveedor"
    id = db.Column(db.String(40), primary_key=True)
    id_entidad = db.Column(db.String(40), nullable=False)
    fecha_evento = db.Column(db.DateTime, nullable=False)
    version = db.Column(db.String(10), nullable=True)
    tipo_evento = db.Column(db.String(100), nullable=True)
    formato_contenido = db.Column(db.String(10), nullable=True)
    nombre_servicio = db.Column(db.String(40), nullable=True)
    contenido = db.Column(db.Text, nullable=True)
    
class ProveedorAnalitica(db.Model):
    __tablename__ = "analitica_proveedor"
    fecha_creacion = db.Column(db.Date, primary_key=True)
    total = db.Column(db.Integer, primary_key=True, nullable=False)