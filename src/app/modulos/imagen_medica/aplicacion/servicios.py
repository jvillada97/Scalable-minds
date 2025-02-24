from app.seedwork.aplicacion.servicios import Servicio
from app.modulos.imagen_medica.dominio.entidades import ImagenMedica
from app.modulos.imagen_medica.dominio.fabricas import FabricaImagenMedica
from app.modulos.imagen_medica.infraestructura.fabricas import FabricaRepositorio
from app.modulos.imagen_medica.infraestructura.repositorios import RepositorioImagenMedicas
from .mapeadores import MapeadorImagenMedica
from werkzeug.utils import secure_filename
import os

from .dto import ImagenMedicaDTO

class ServicioReserva(Servicio):

    def __init__(self):
        self._fabrica_repositorio: FabricaRepositorio = FabricaRepositorio()

    @property
    def fabrica_repositorio(self):
        return self._fabrica_repositorio
    
    @property
    def fabrica_vuelos(self):
        return self._fabrica_repositorio

    def crear_imagen_medica(self, reserva_dto: ImagenMedicaDTO) -> ImagenMedicaDTO:
        # Guardar la imagen en una carpeta
        archivo_imagen = reserva_dto.archivo_imagen
        filename = secure_filename(archivo_imagen.filename)
        save_path = os.path.join('src', 'images', filename)
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        archivo_imagen.save(save_path)

        # Crear la entidad ImagenMedica
        imagenMedica: ImagenMedica = self.fabrica_vuelos.crear_objeto(reserva_dto, MapeadorImagenMedica())
        imagenMedica.url_imagen = save_path  # Guardar la ruta de la imagen en la entidad

        # Guardar la entidad en el repositorio
        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioImagenMedicas.__class__)
        repositorio.agregar(imagenMedica)

        return self.fabrica_vuelos.crear_objeto(imagenMedica, MapeadorImagenMedica())

    def obtener_imagen_medica_por_id(self, id) -> ImagenMedicaDTO:
        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioImagenMedicas.__class__)
        imagen_medica = repositorio.obtener_por_id(id)
        
        # Leer el archivo de imagen desde la URL
        with open(imagen_medica.url_imagen, 'rb') as file:
            imagen_data = file.read()
        
        # Crear el DTO y agregar la imagen
        imagen_medica_dto = self.fabrica_vuelos.crear_objeto(imagen_medica, MapeadorImagenMedica())
        imagen_medica_dto.archivo_imagen = imagen_data
        
        return imagen_medica_dto

