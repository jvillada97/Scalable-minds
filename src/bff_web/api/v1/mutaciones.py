import strawberry
import typing

from strawberry.types import Info
from bff_web import utils
from bff_web.despachadores import Despachador

from .esquemas import *

@strawberry.type
class Mutation:

    @strawberry.mutation
    async def cargar_imagen_medica(self, archivo_imagen: str, info: Info) -> ImagenMedicaRespuesta:
        save_path = f"src/images/logo.png"
        payload = dict(
            archivo_imagen=save_path
        )
        comando = dict(
            id = str(uuid.uuid4()),
            time=utils.time_millis(),
            specversion = "v1",
            type = "ComandoReserva",
            ingestion=utils.time_millis(),
            datacontenttype="AVRO",
            service_name = "BFF Web",
            data = payload
        )
        despachador = Despachador()
        info.context["background_tasks"].add_task(despachador.publicar_mensaje, comando, "comandos-imagen-medica", "public/default/comandos-imagen-medica")
        
        return ImagenMedicaRespuesta(mensaje="Cargando imagen correctamente", codigo=203)