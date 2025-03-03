from app.seedwork.aplicacion.servicios import Servicio
from app.modulos.proveedor.dominio.entidades import Proveedor
from app.modulos.proveedor.dominio.fabricas import FabricaProveedor
from app.modulos.proveedor.infraestructura.fabricas import FabricaRepositorio
from app.modulos.proveedor.infraestructura.repositorios import RepositorioProveedors
from app.modulos.proveedor.aplicacion.mapeadores import MapeadorProveedor


from .dto import ProveedorDTO

class ServicioProveedor(Servicio):

    def __init__(self):
        self._fabrica_repositorio: FabricaRepositorio = FabricaRepositorio()

    @property
    def fabrica_repositorio(self):
        return self._fabrica_repositorio
    
    @property
    def fabrica_vuelos(self):
        return self._fabrica_repositorio

    def crear_proveedor(self, reserva_dto: ProveedorDTO) -> ProveedorDTO:
        # Guardar la imagen en una carpeta
       

        # Crear la entidad Proveedor
        imagenMedica: Proveedor = self.fabrica_vuelos.crear_objeto(reserva_dto, MapeadorProveedor())       

        # Guardar la entidad en el repositorio
        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioProveedors.__class__)
        repositorio.agregar(imagenMedica)

        return self.fabrica_vuelos.crear_objeto(imagenMedica, MapeadorProveedor())

    def obtener_proveedor_por_id(self, id) -> ProveedorDTO:
        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioProveedors.__class__)
        proveedor = repositorio.obtener_por_id(id)
        
        # Leer el archivo de imagen desde la URL
        with open(proveedor.url_imagen, 'rb') as file:
            imagen_data = file.read()
        
        # Crear el DTO y agregar la imagen
        proveedor_dto = self.fabrica_vuelos.crear_objeto(proveedor, MapeadorProveedor())      
        
        return proveedor_dto

