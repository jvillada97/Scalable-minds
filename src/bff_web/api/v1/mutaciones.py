import strawberry
import typing
import uuid
from strawberry.types import Info
from bff_web import utils
from bff_web.despachadores import Despachador
from .esquemas import ImagenMedicaRespuesta

# Definir un tipo escalar para manejar archivos binarios en GraphQL
FileScalar = strawberry.scalar(
    bytes, description="Tipo escalar para manejar archivos en GraphQL"
)

# Definir esquema GraphQL con Strawberry
@strawberry.type
class Mutation:
    @strawberry.mutation
    async def subir_imagen_medica(self, archivo: FileScalar) -> ImagenMedicaRespuesta:
        """Mutación para subir una imagen médica a almacenamiento y devolver la URL"""
        try:
            file_id = str(uuid.uuid4())  # Generar un ID único para el archivo
            file_location = f"/uploads/{file_id}.jpg"

            with open(file_location, "wb") as buffer:
                buffer.write(archivo)  # `archivo` ya es `bytes`

            return ImagenMedicaRespuesta(mensaje=f"Imagen guardada en {file_location}", codigo=201)
        except Exception as e:
            return ImagenMedicaRespuesta(mensaje=f"Error al subir imagen: {str(e)}", codigo=500)
