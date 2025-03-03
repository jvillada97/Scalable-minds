from app.seedwork.aplicacion.comandos import Comando
from app.modulos.proveedor.aplicacion.dto import ProveedorDTO
from app.modulos.proveedor.aplicacion.comandos.base import CrearProveedorBaseHandler
from dataclasses import dataclass, field
from app.seedwork.aplicacion.comandos import ejecutar_commando as comando

from app.modulos.proveedor.dominio.entidades import Proveedor
from app.seedwork.infraestructura.uow import UnidadTrabajoPuerto
from app.modulos.proveedor.aplicacion.mapeadores import MapeadorProveedor
from app.modulos.proveedor.infraestructura.repositorios import RepositorioProveedors, RepositorioEventosProveedors
@dataclass
class CrearProveedor(Comando):
    name: str = field(default_factory=str)


class CrearReservaHandler(CrearProveedorBaseHandler):
    
    def handle(self, comando: CrearProveedor):
        reserva_dto = ProveedorDTO(
               name=comando.name)

        reserva: Proveedor = self.fabrica_proveedor.crear_objeto(reserva_dto, MapeadorProveedor())
        print(reserva)
        reserva.crear_propiedad(reserva)

        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioProveedors.__class__)
        repositorio_eventos = self.fabrica_repositorio.crear_objeto(RepositorioEventosProveedors)
        
        UnidadTrabajoPuerto.registrar_batch(repositorio.agregar, reserva, repositorio_eventos_func=repositorio_eventos.agregar)
        UnidadTrabajoPuerto.savepoint()
        UnidadTrabajoPuerto.commit()


@comando.register(CrearProveedor)
def ejecutar_comando_crear_proveedor(comando: CrearProveedor):
    handler = CrearReservaHandler()
    handler.handle(comando)
    