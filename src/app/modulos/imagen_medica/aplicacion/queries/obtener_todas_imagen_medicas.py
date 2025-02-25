from dataclasses import dataclass
from app.seedwork.aplicacion.queries import Query, QueryHandler, QueryResultado
from app.seedwork.aplicacion.queries import ejecutar_query as query
from app.modulos.imagen_medica.dominio.entidades import ImagenMedica
from app.modulos.imagen_medica.aplicacion.queries.base import ImagenMedicaQueryBaseHandler
from app.modulos.imagen_medica.aplicacion.mapeadores import MapeadorImagenMedica
from app.modulos.imagen_medica.aplicacion.dto import ImagenMedicaDTO

@dataclass
class ObtenerTodasImagenesMedicas(Query):
    ...

class ObtenerTodasImagenesMedicasHandler(ImagenMedicaQueryBaseHandler):

    def handle(self, query) -> QueryResultado:
        propiedades_dto = []
        vista = self._fabrica_vista.crear_objeto(ImagenMedica)
        propiedades = vista.obtener_todos()    

        for propiedad in propiedades:
            dto = ImagenMedicaDTO(
                url_imagen=propiedad.url_imagen
                )
            propiedades_dto.append(dto)    
        
        return QueryResultado(resultado=propiedades_dto)

@query.register(ObtenerTodasImagenesMedicas)
def ejecutar_query_obtener_propiedad(query: ObtenerTodasImagenesMedicas):
    handler = ObtenerTodasImagenesMedicasHandler()
    return handler.handle(query)