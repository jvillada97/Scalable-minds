""" Fábricas para la creación de objetos en la capa de infrastructura del dominio de vuelos

En este archivo usted encontrará las diferentes fábricas para crear
objetos complejos en la capa de infraestructura del dominio de vuelos

"""

from dataclasses import dataclass, field
from app.seedwork.dominio.fabricas import Fabrica
from app.seedwork.dominio.repositorios import Repositorio
from app.modulos.imagen_medica.dominio.repositorios import  RepositorioImagenMedicas
from app.modulos.imagen_medica.infraestructura.repositorios import RepositorioImagenMedicasSQLite
from app.modulos.imagen_medica.infraestructura.excepciones import ExcepcionFabrica
from app.modulos.imagen_medica.dominio.entidades import ImagenMedica
from app.seedwork.infraestructura.vistas import Vista

@dataclass
class FabricaRepositorio(Fabrica):
    
    def crear_objeto(self, obj: type, mapeador: any = None) -> Repositorio:
        if obj == RepositorioImagenMedicas.__class__:
            return RepositorioImagenMedicasSQLite()       
        else:
            raise ExcepcionFabrica()
        
                
@dataclass
class FabricaVista(Fabrica):
    def crear_objeto(self, obj: type, mapeador: any = None) -> Vista:
        if obj == ImagenMedica:
            return RepositorioImagenMedicasSQLite()
        else:
            raise ExcepcionFabrica(f'No existe fábrica para el objeto {obj}')