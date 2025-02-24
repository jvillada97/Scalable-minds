from dataclasses import dataclass
from app.seedwork.aplicacion.queries import Query, QueryHandler, QueryResultado
from app.seedwork.aplicacion.queries import ejecutar_query as query
from app.modulos.imagen_medica.dominio.entidades import ImagenMedica
from app.modulos.imagen_medica.aplicacion.dto import ImagenMedicaDTO
from app.modulos.imagen_medica.aplicacion.queries.base import ImagenMedicaQueryBaseHandler


@dataclass
class ObtenerTodasImagenesMedicas(Query):
    ...

class ObtenerTodasImagenesMedicasHandler(ImagenMedicaQueryBaseHandler):

    FORMATO_FECHA = '%Y-%m-%dT%H:%M:%SZ'

    def handle(self, query) -> QueryResultado:
        propiedades_dto = []
        vista = self.fabrica_vista.crear_objeto(ImagenMedica)
        propiedades = vista.obtener_todos()
        print("=================== ObtenerTodasPropiedadesHandler =========================")
        print(propiedades)

        for propiedad in propiedades:
            dto = ImagenMedicaDTO(
                id=propiedad.id,
                url_imagen=propiedad.url_imagen
                )
            propiedades_dto.append(dto)

        print("=================== ObtenerTodasPropiedadesHandler =========================")
        print(propiedades_dto)
        
        return QueryResultado(resultado=propiedades_dto)

@query.register(ObtenerTodasImagenesMedicas)
def ejecutar_query_obtener_propiedad(query: ObtenerTodasImagenesMedicas):
    handler = ObtenerTodasImagenesMedicasHandler()
    return handler.handle(query)