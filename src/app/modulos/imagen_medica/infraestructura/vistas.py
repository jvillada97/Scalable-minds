from app.seedwork.infraestructura.vistas import Vista
from app.modulos.imagen_medica.dominio.entidades import ImagenMedica
from app.config.db import db
from .dto import ImagenMedica as ImagenMedicaDTO

class VistaImagenMedica(Vista):
    def obtener_por(id=None, url_imagen=None, **kwargs) -> [ImagenMedica]:
        params = dict()

        if id:
            params['id'] = str(id)
        
        if url_imagen:
            params['url_imagen'] = str(url_imagen)        
            
        return db.session.query(ImagenMedicaDTO).filter_by(**params)
