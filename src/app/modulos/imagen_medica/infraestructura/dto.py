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

