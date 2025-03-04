"""DTOs para la capa de infraestructura del dominio de imagen médica

En este archivo usted encontrará los DTOs (modelos anémicos) de
la infraestructura del dominio de imagen médica

"""

from app.config.db import db
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, ForeignKey, Integer, Table, DateTime, String

import uuid

Base = db.declarative_base()


class Anonimizacion(db.Model):
    __tablename__ = "anonimizacion"
    id = db.Column(db.String, primary_key=True, default=lambda: str(uuid.uuid4()))
    url_imagen = db.Column(db.String, nullable=False)

class EventosAnonimizacion(db.Model):
    __tablename__ = "eventos_anonimizacion"
    id = db.Column(db.String(40), primary_key=True)
    id_entidad = db.Column(db.String(40), nullable=False)
    fecha_evento = db.Column(db.DateTime, nullable=True)
    version = db.Column(db.String(10), nullable=True)
    tipo_evento = db.Column(db.String(100), nullable=True)
    formato_contenido = db.Column(db.String(10), nullable=True)
    nombre_servicio = db.Column(db.String(40), nullable=True)
    contenido = db.Column(db.Text, nullable=True)
    
class AnonimizacionAnalitica(db.Model):
    __tablename__ = "analitica_anonimizacion"
    fecha_creacion = db.Column(db.Date, primary_key=True)
    total = db.Column(db.Integer, primary_key=True, nullable=False)