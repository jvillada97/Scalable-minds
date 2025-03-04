
import strawberry
from .esquemas import *

@strawberry.type
class Query:
    imagenes: typing.List[ImagenMedica] = strawberry.field(resolver=obtener_image)