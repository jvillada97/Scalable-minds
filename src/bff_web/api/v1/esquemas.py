from __future__ import annotations  # Habilitar anotaciones avanzadas
import os
import typing
import requests
import strawberry

# Configuración del host del BFF
SALUDTECH_BFF_HOST = os.getenv("SALUDTECH_BFF_ADDRESS", "localhost")
IMAGES_API_URL = f"http://{SALUDTECH_BFF_HOST}:5000/imagenes_medicas"

FORMATO_FECHA = '%Y-%m-%dT%H:%M:%SZ'


def obtener_imagenes(root) -> list[ImagenMedica]:
    """Consulta la API del BFF para obtener imágenes médicas."""
    try:
        response = requests.get(IMAGES_API_URL, timeout=5)
        response.raise_for_status()
        imagenes = response.json()
        return [ImagenMedica(**imagen) for imagen in imagenes]
    except requests.exceptions.RequestException as e:
        print(f"Error obteniendo imágenes: {e}")
        return []


@strawberry.type
class ImagenMedica:
    id: str
    url_imagen: str
    tipo_archivo: str
    fecha_creacion: str

    @strawberry.field
    def descargar_imagen(self) -> str:
        """Devuelve la URL de descarga de la imagen."""
        return f"{IMAGES_API_URL}/{self.id}/descargar"


@strawberry.type
class ImagenMedicaRespuesta:
    mensaje: str
    codigo: int
    imagen: typing.Optional[ImagenMedica] = None
