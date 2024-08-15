# Proyecto de Microservicios con Docker

Este proyecto consiste en una arquitectura de microservicios utilizando Docker y Docker Compose. Incluye varios servicios como CRUD, Login, API y Gateway, cada uno con su propio contenedor.

## Estructura del Proyecto

- **movies/**: Contiene el servicio CRUD.
- **login/**: Contiene el servicio de autenticación.
- **api_call/**: Contiene el servicio API.
- **gateway/**: Contiene el servicio de Gateway Nginx.

## Servicios

### CRUD (movies)
Servicio para gestionar películas.

- **Tecnología**: Flask
- **Puerto**: 5000

### Login (login)
Servicio para autenticación de usuarios.

- **Tecnología**: FastAPI
- **Puerto**: 8000

### API (api_call)
Servicio para realizar llamadas a una API externa.

- **Tecnología**: Node.js con Express
- **Puerto**: 8080

### Gateway (gateway)
Servicio de Gateway utilizando Nginx para enrutar las solicitudes a los diferentes servicios.

- **Tecnología**: Nginx
- **Puerto**: 80

## Configuración

### Variables de Entorno
Cree un archivo `.env` en la raíz del proyecto y defina las siguientes variables:

```env
SECRET_KEY=your_secret_key
PGSQL_HOST=your_pgsql_host
PGSQL_PORT=your_pgsql_port
PGSQL_USER=your_pgsql_user
PGSQL_PASSWORD=your_pgsql_password
PGSQL_DATABASE=your_pgsql_database
LOGIN_SECRET_KEY=your_login_secret_key
```
### Construcción y Ejecución
1. Construya los contenedores:
```sh
docker-compose build
```

2. Inicie los contenedores:

```sh
docker-compose up
```

## EndPoints

### CRUD

- **GET /api/movies:** Obtener todas las películas.
- **POST /api/movies/add:** Crear una nueva película.
- **UPDATE /api/update/<id>:** Actualiza una película existente
- **DELETE /api/delete/<id>:** Elimina una película

### Login

- **POST /login/token:** Obtener un token de acceso.
- **GET /login/users/profile:** Obtener el perfil del usuario autenticado.

### API

- **GET /products:** Obtener todos los productos.
- **GET /products/:id:** Obtener un producto específico por ID.
- **GET /categories:** Obtener todas las categorías de productos.
- **GET /categories/:category/products:** Obtener productos por categoría.

## Dependencias

### CRUD

- Flask
- Flask-Cors
- psycopg2
- python-decouple

### Login

- FastAPI
- passlib
- python-jose
- python-dotenv

### API

- Express
- Axios

### Gateway

- Nginx

