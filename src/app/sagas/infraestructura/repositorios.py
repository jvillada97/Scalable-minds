import traceback
from config.db import db
from .dto import Saga_Log
import uuid
 
class RepositorioSagaLogPostgresSQL():         
 
    def agregar(self, evento: str):
        saga_log_dto = Saga_Log(id=uuid.uuid4().hex, evento=evento)
        db.session.add(saga_log_dto)
        db.session.commit()