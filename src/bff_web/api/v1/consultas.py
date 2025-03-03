
import strawberry
from .esquemas import *

@strawberry.type
class Query:
    reservas: typing.List[ImagenMedica] = strawberry.field(resolver=obtener_imagenes)