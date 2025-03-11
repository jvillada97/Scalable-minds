from dataclasses import dataclass, field
from app.seedwork.aplicacion.comandos import Comando
from app.modulos.proveedor.aplicacion.comandos.base import EliminarProveedorBaseHandler
from app.modulos.proveedor.infraestructura.repositorios import RepositorioProveedor, RepositorioEventosProveedor
from app.modulos.proveedor.dominio.entidades import Proveedor
from app.modulos.proveedor.aplicacion.mapeadores import MapeadorProveedor
from app.modulos.proveedor.aplicacion.dto import ProveedorDTO
from app.seedwork.infraestructura.uow import UnidadTrabajoPuerto
from app.seedwork.aplicacion.comandos import ejecutar_commando as comando

@dataclass
class EliminarProveedor(Comando):
    name: str

class EliminarProveedorHandler(EliminarProveedorBaseHandler):
    def handle(self, comando: EliminarProveedor):      
        propiedad_dto = ProveedorDTO(name=comando.name)
        propiedad : Proveedor = self.fabrica_companias.crear_objeto(propiedad_dto, MapeadorProveedor())
        propiedad.eliminar_propiedad(propiedad)
        repositorio = self._fabrica_repositorio.crear_objeto(RepositorioProveedor.__class__)
        UnidadTrabajoPuerto.registrar_batch(repositorio.eliminar, propiedad)
        UnidadTrabajoPuerto.commit()


@comando.register(EliminarProveedor)
def ejecutar_comando_Eliminar_compania(comando: EliminarProveedor):
    handler = EliminarProveedorHandler()
    handler.handle(comando)