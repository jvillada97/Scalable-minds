from config.db import db
Base = db.declarative_base()
from datetime import datetime
from sqlalchemy.dialects.postgresql import UUID

class Saga_Log(db.Model):
     __tablename__ = "saga_log"
     id = db.Column(db.String, primary_key=True, nullable=False)
     source = db.Column(db.String, nullable=True)
     status = db.Column(db.String, nullable=True)
     id = db.Column(UUID(as_uuid=True), primary_key=True)
     evento = db.Column(db.String, nullable=False)
     fecha_evento = db.Column(db.DateTime, default=datetime.utcnow)    