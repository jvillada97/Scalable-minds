from dataclasses import dataclass
from app.seedwork.aplicacion.queries import Query, QueryHandler, QueryResultado
from app.seedwork.aplicacion.queries import ejecutar_query as query
from app.modulos.anonimizacion.dominio.entidades import Anonimizacion
from app.modulos.anonimizacion.aplicacion.queries.base import AnonimizacionQueryBaseHandler
from app.modulos.anonimizacion.aplicacion.mapeadores import MapeadorAnonimizacion
from app.modulos.anonimizacion.aplicacion.dto import AnonimizacionDTO

@dataclass
class ObtenerTodasAnonimizaciones(Query):
    ...

class ObtenerTodasAnonimizacionesHandler(AnonimizacionQueryBaseHandler):

    def handle(self, query) -> QueryResultado:
        propiedades_dto = []
        vista = self._fabrica_vista.crear_objeto(Anonimizacion)
        propiedades = vista.obtener_todos()    

        for propiedad in propiedades:
            dto = AnonimizacionDTO(
                url_imagen=propiedad.url_imagen
                )
            propiedades_dto.append(dto)    
        
        return QueryResultado(resultado=propiedades_dto)

@query.register(ObtenerTodasAnonimizaciones)
def ejecutar_query_obtener_propiedad(query: ObtenerTodasAnonimizaciones):
    handler = ObtenerTodasAnonimizacionesHandler()
    return handler.handle(query)