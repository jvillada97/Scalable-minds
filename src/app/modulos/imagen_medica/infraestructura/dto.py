"""DTOs para la capa de infraestructura del dominio de imagen médica

En este archivo usted encontrará los DTOs (modelos anémicos) de
la infraestructura del dominio de imagen médica

"""

from app.config.db import db
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, ForeignKey, Integer, Table, DateTime, String

import uuid

Base = db.declarative_base()

# Tabla intermedia para tener la relación de muchos a muchos entre la tabla imagen_medica y diagnostico
imagenes_diagnosticos = db.Table(
    "imagenes_diagnosticos",
    db.Model.metadata,
    db.Column("imagen_id", db.String, db.ForeignKey("imagen_medica.id")),
    db.Column("diagnostico_id", db.String, db.ForeignKey("diagnosticos.id"))
)

class ImagenMedica(db.Model):
    __tablename__ = "imagen_medica"
    id = db.Column(db.String, primary_key=True, default=lambda: str(uuid.uuid4()))
    fecha_creacion = db.Column(db.DateTime, nullable=False)
    tipo_imagen = db.Column(db.String, nullable=False)
    url_imagen = db.Column(db.String, nullable=False)
    diagnosticos = db.relationship('Diagnostico', secondary=imagenes_diagnosticos, backref='imagenes_medicas')

class Diagnostico(db.Model):
    __tablename__ = "diagnosticos"
    id = db.Column(db.String, primary_key=True, default=lambda: str(uuid.uuid4()))
    fecha_diagnostico = db.Column(db.DateTime, nullable=False)
    descripcion = db.Column(db.String, nullable=False)
    imagenes_medicas = db.relationship('ImagenMedica', secondary=imagenes_diagnosticos, backref='diagnosticos')