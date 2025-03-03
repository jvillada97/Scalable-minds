from app.config.db import db
from app.seedwork.dominio.eventos import EventoDominio
from app.seedwork.infraestructura.uow import UnidadTrabajo, Batch
from pydispatch import dispatcher
import logging
import traceback
from datetime import datetime

class ExcepcionUoW(Exception):
    ...

class UnidadTrabajoSQLAlchemy(UnidadTrabajo):

    def __init__(self):
        self._batches: list[Batch] = list()
        self._savepoints: list[tuple[str, datetime]] = list()

    def __enter__(self) -> UnidadTrabajo:
        return super().__enter__()

    def __exit__(self, *args):
        self.rollback()

    def _limpiar_batches(self):
        self._batches = list()

    @property
    def savepoints(self) -> list:
        return self._savepoints

    @property
    def batches(self) -> list[Batch]:
        return self._batches             

    def commit(self):
        for batch in self.batches:
            lock = batch.lock
            batch.operacion(*batch.args, **batch.kwargs)
                
        db.session.commit() # Commits the transaction

        super().commit()

    def rollback(self, savepoint=None):
        if savepoint:
            db.session.execute(f"ROLLBACK TO SAVEPOINT {savepoint};")
        else:
            db.session.rollback()
        
        super().rollback()
    
    def savepoint(self):
        savepoint_name = f"sp_{len(self._savepoints) + 1}"
        db.session.execute(f"SAVEPOINT {savepoint_name};")
        self._savepoints.append((savepoint_name, datetime.now()))
        return savepoint_name

class UnidadTrabajoPulsar(UnidadTrabajo):

    def __init__(self):
        self._batches: list[Batch] = list()

    def __enter__(self) -> UnidadTrabajo:
        return super().__enter__()

    def __exit__(self, *args):
        self.rollback()

    def _limpiar_batches(self):
        self._batches = list()

    @property
    def savepoints(self) -> list:
        return []

    @property
    def batches(self) -> list[Batch]:
        return self._batches             

    def commit(self):
        index = 0
        try:
            for evento in self._obtener_eventos():
                dispatcher.send(signal=f'{type(evento).__name__}Integracion', evento=evento)
                index += 1
        except:
            logging.error('ERROR: Suscribiendose al tópico de eventos!')
            traceback.print_exc()
            self.rollback(index=index)
        self._limpiar_batches()

    def rollback(self, index=None):
        eventos = self._obtener_eventos()
        if index is not None:
            eventos_a_compensar = eventos[:index]
        else:
            eventos_a_compensar = eventos

        for evento in eventos_a_compensar:
            evento_compensacion = self._crear_evento_compensacion(evento)
            if evento_compensacion:
                dispatcher.send(signal=f'{type(evento_compensacion).__name__}Compensacion', evento=evento_compensacion)

        self._limpiar_batches()
        super().rollback()
        
    def _crear_evento_compensacion(self, evento):
        # Implementa la lógica para crear un evento de compensación basado en el evento original
        # Esto puede variar dependiendo de la lógica de negocio específica
        # Aquí hay un ejemplo básico:
        if isinstance(evento, EventoDominio):
            evento_compensacion = EventoDominio(
                id=evento.id,
                fecha_evento=datetime.now()
            )
            return evento_compensacion
        return None
    
    def savepoint(self):
        # NOTE No hay punto de implementar este método debido a la naturaleza de Event Sourcing
        ...