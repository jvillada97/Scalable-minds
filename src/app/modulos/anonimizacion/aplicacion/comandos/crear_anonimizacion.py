from app.seedwork.aplicacion.comandos import Comando
from app.modulos.anonimizacion.aplicacion.dto import AnonimizacionDTO
from app.modulos.anonimizacion.aplicacion.comandos.base import CrearAnonimizacionBaseHandler
from dataclasses import dataclass, field
from app.seedwork.aplicacion.comandos import ejecutar_commando as comando

from app.modulos.anonimizacion.dominio.entidades import Anonimizacion
from app.seedwork.infraestructura.uow import UnidadTrabajoPuerto
from app.modulos.anonimizacion.aplicacion.mapeadores import MapeadorAnonimizacion
from app.modulos.anonimizacion.infraestructura.repositorios import RepositorioAnonimizacions
@dataclass
class CrearAnonimizacion(Comando):
    url_image: str = field(default_factory=str)


class CrearReservaHandler(CrearAnonimizacionBaseHandler):
    
    def handle(self, comando: CrearAnonimizacion):
        reserva_dto = AnonimizacionDTO(
               url_imagen=comando.url_image)

        reserva: Anonimizacion = self.fabrica_anonimizacion.crear_objeto(reserva_dto, MapeadorAnonimizacion())
        print(reserva)
        reserva.crear_propiedad(reserva)

        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioAnonimizacions.__class__)

        UnidadTrabajoPuerto.registrar_batch(repositorio.agregar, reserva)
        UnidadTrabajoPuerto.savepoint()
        UnidadTrabajoPuerto.commit()


@comando.register(CrearAnonimizacion)
def ejecutar_comando_crear_anonimizacion(comando: CrearAnonimizacion):
    handler = CrearReservaHandler()
    handler.handle(comando)
    