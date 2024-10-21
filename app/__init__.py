from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_restx import Api
from flask_migrate import Migrate
from .config import Config

# Inicializamos las extensiones globalmente para luego asociarlas a la app en la función create_app
db = SQLAlchemy()  # Para la interacción con la base de datos usando SQLAlchemy
migrate = Migrate()  # Para gestionar las migraciones de la base de datos
bcrypt = Bcrypt()  # Para el hash y verificación de contraseñas de los usuarios
jwt = JWTManager()  # Para la gestión de tokens JWT en la autenticación

def create_app():
    """Función factory para crear la aplicación Flask y configurar sus componentes."""
    
    # Creamos una instancia de la aplicación Flask
    app = Flask(__name__)
    
    # Cargamos la configuración de la aplicación desde el archivo de configuración
    app.config.from_object(Config)

    # Inicializamos las extensiones con la aplicación
    db.init_app(app)  # Inicializar SQLAlchemy con la app
    bcrypt.init_app(app)  # Inicializar Bcrypt con la app
    jwt.init_app(app)  # Inicializar JWTManager con la app
    migrate.init_app(app, db)  # Inicializar Migrate con la app y la base de datos

    # Autorizador JWT para integrar con la documentación Swagger
    authorizations = {
        'Bearer': {
            'type': 'apiKey',  # Tipo apiKey define que el token JWT se envía en el encabezado de la solicitud
            'in': 'header',  # El token JWT se debe enviar en el encabezado de la solicitud HTTP
            'name': 'Authorization',  # Nombre del campo del encabezado HTTP para el token
            'description': 'JWT Bearer token. Ejemplo: "Bearer {token}"'  # Instrucción sobre cómo enviar el token
        }
    }

    # Configuramos la API Flask-RESTX, que nos ayuda a crear endpoints RESTful con documentación Swagger integrada
    api = Api(
        app,  # La aplicación Flask en la que registramos la API
        title='API de registro de servicios',  # Título para la documentación Swagger
        version='1.0',  # Versión de la API
        description='API para gestión de órdenes de servicios',  # Descripción de la API
        authorizations=authorizations,  # Añadimos la configuración de JWT a la API
        security='Bearer'  # Define que los endpoints por defecto usan el esquema de seguridad JWT
    )

    # Registrar los controladores (namespaces) para cada tabla/entidad
    from .controllers.cliente_controller import cliente_ns
    from .controllers.vehiculo_controller import vehiculo_ns
    from .controllers.servicios_gen_controller import servicio_gen_ns
    from .controllers.servicios_esp_controller import servicio_esp_ns
    from .controllers.otro_servicio_controller import otro_servicio_ns
    from .controllers.insumos_controller import insumos_ns
    from .controllers.orden_controller import orden_ns
    from .controllers.detalle_orden_controller import detalle_orden_ns

    # Agregar los namespaces (rutas) al Api
    api.add_namespace(cliente_ns, path='/clientes')  # Rutas para clientes
    api.add_namespace(vehiculo_ns, path='/vehiculos')  # Rutas para vehículos
    api.add_namespace(servicio_gen_ns, path='/servicios_gen')  # Rutas para servicios generales
    api.add_namespace(servicio_esp_ns, path='/servicios_esp')  # Rutas para servicios específicos
    api.add_namespace(otro_servicio_ns, path='/otro_servicio')  # Rutas para otros servicios
    api.add_namespace(insumos_ns, path='/insumos')  # Rutas para insumos
    api.add_namespace(orden_ns, path='/ordenes')  # Rutas para órdenes
    api.add_namespace(detalle_orden_ns, path='/detalle_orden')  # Rutas para detalles de órdenes

    # Retornamos la aplicación ya configurada
    return app

    
    
    
