"""DTOs para la capa de infraestructura del dominio de imagen médica

En este archivo usted encontrará los DTOs (modelos anémicos) de
la infraestructura del dominio de imagen médica

"""

from app.config.db import db
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, ForeignKey, Integer, Table, DateTime, String

import uuid

Base = db.declarative_base()


class ImagenMedica(db.Model):
    __tablename__ = "imagen_medica"
    id = db.Column(db.String, primary_key=True, default=lambda: str(uuid.uuid4()))
    url_imagen = db.Column(db.String, nullable=False)

class EventosImagenMedica(db.Model):
    __tablename__ = "eventos_imagen_medica"
    id = db.Column(db.String(40), primary_key=True)
    id_entidad = db.Column(db.String(40), nullable=False)
    fecha_evento = db.Column(db.DateTime, nullable=False)
    version = db.Column(db.String(10), nullable=False)
    tipo_evento = db.Column(db.String(100), nullable=False)
    formato_contenido = db.Column(db.String(10), nullable=False)
    nombre_servicio = db.Column(db.String(40), nullable=False)
    contenido = db.Column(db.Text, nullable=False)
    
class ImagenMedicaAnalitica(db.Model):
    __tablename__ = "analitica_imagen_medicas"
    fecha_creacion = db.Column(db.Date, primary_key=True)
    total = db.Column(db.Integer, primary_key=True, nullable=False)