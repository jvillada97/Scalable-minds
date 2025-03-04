""" Interfaces para los repositorios del dominio de vuelos

En este archivo usted encontrará las diferentes interfaces para repositorios
del dominio de vuelos

"""

from abc import ABC
from app.seedwork.dominio.repositorios import Repositorio

class RepositorioProveedor(Repositorio, ABC):
    ...


class RepositorioEventosProveedor(Repositorio, ABC):
    ...

