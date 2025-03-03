from fastapi import APIRouter
from strawberry.fastapi import GraphQLRouter
import strawberry

from .consultas import Query
from .mutaciones import Mutation

router = APIRouter()

# Crear el esquema de Strawberry
schema = strawberry.Schema(query=Query, mutation=Mutation)

# Crear GraphQLRouter sin 'lifespan'
graphql_router = GraphQLRouter(schema)

# Agregar GraphQL a las rutas de FastAPI de forma manual
router.add_route("/graphql", graphql_router, methods=["GET", "POST"])
