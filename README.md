
# Scalable Minds Project

Este proyecto es un sistema de gestión de imágenes médicas que utiliza Flask como framework backend y PostgreSQL como base de datos. También hace uso de Apache Pulsar como sistema de mensajería.

## 💁️ Estructura del Proyecto

```bash
src/
│── app/
│   ├── api/                # Endpoints de la API
│   │   ├── imagen_medica.py
│   │   ├── proveedores.py
│   │   └── __init__.py
│   ├── config/             # Configuración de la base de datos y otros servicios
│   │   ├── db.py
│   │   ├── uow.py
│   │   └── __init__.py
│   ├── modulos/            # Módulos específicos del dominio
│   │   ├── imagen_medica/
│   │   └── __init__.py
│   ├── seedwork/           # Implementaciones reutilizables
│   │   ├── aplicacion/
│   │   │   ├── comandos.py
│   │   │   ├── dto.py
│   │   │   ├── handlers.py
│   │   │   ├── queries.py
│   │   │   ├── servicios.py
│   │   │   └── __init__.py
│   │   ├── dominio/
│   │   │   ├── entidades.py
│   │   │   ├── eventos.py
│   │   │   ├── excepciones.py
│   │   │   ├── fabricas.py
│   │   │   ├── mixins.py
│   │   │   ├── objetos_valor.py
│   │   │   ├── reglas.py
│   │   │   ├── repositorios.py
│   │   │   ├── servicios.py
│   │   │   └── __init__.py
│   │   ├── infraestructura/
│   │   │   ├── schema/
│   │   │   │   ├── __init__.py
│   │   │   │   ├── uow.py
│   │   │   │   ├── utils.py
│   │   │   │   └── vistas.py
│   │   ├── presentacion/
│   │   │   ├── __init__.py
│   │   │   ├── api.py
│   │   │   └── __init__.py
```

## 🛠️ Tecnologías Utilizadas
- Python 3

- Flask como framework web

- PostgreSQL como base de datos

- Apache Pulsar como sistema de mensajería

- Docker para la orquestación de servicios

## 🚀 Instalación y Ejecución
1️⃣ Prerrequisitos

Asegúrate de tener instalado:

- Docker

- Docker Compose

2️⃣ Ejecutar con Docker

Para levantar los servicios utilizando docker-compose, ejecuta:

```bash
docker-compose up --build
```

Esto iniciará los siguientes servicios:

- PostgreSQL en el puerto 5432

- Apache Pulsar en los puertos 6650 y 8080

- Aplicación de imágenes médicas en el puerto 5001

- Apliación de proveedores en el puerto 5002

- Aplicación de anonimización en el puerto 5003

3️⃣ Verificación de Servicios

Después de iniciar los contenedores, verifica que los servicios están corriendo:
```bash
docker ps
```
También puedes acceder a los logs de la aplicación:
```bash
docker logs imagenes_medicas
```

```bash
docker logs proveedores
```

```bash
docker logs anonimizacion
```

Si necesitas acceder a la base de datos PostgreSQL desde tu máquina, usa:
```bash
psql -h localhost -U postgres -d postgres
```
4️⃣ Pruebas

Para ejecutar las pruebas unitarias del proyecto, usa:
```bash
docker exec -it imagenes_medicas pytest
```

5️⃣Detener los Contenedores
Para detener la ejecución de los servicios, ejecuta:
```bash
docker-compose down
```

6️⃣ Ejecutar endpoints en postman
Para probar los diferentes endpoints construidos en la carpeta raiz acceder al archivo "Desarrollo de Apps no monoliticas.postman_collection.json" y copiar su contenido. Abrir postman y con la opción "import" copiar el contenido del archivo. La documentación de la respuesta de los endpoints se encuentra en https://documenter.getpostman.com/view/30550594/2sAYdeLBWp 

## 🐥 BFF
Para ejecutar el bff
```bash
uvicorn bff_web.main:app --host localhost --port 8003 --reload
```


## 📄 Licencia

Este proyecto está bajo la licencia MIT. Puedes ver más detalles en el archivo LICENSE.
