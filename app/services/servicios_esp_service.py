from app import db
from app.models.servicios_esp import ServiciosEsp

class ServiciosEspService:
    """Servicio para gestionar operaciones CRUD sobre los servicios específicos."""

    @staticmethod
    def create_servicio_esp(nombre_servicio_esp):
        """Crear un nuevo servicio específico."""
        nuevo_servicio_esp = ServiciosEsp(nombre_servicio_esp=nombre_servicio_esp)
        db.session.add(nuevo_servicio_esp)
        db.session.commit()
        return nuevo_servicio_esp

    @staticmethod
    def get_all_servicios_esp():
        """Obtener todos los servicios específicos."""
        return ServiciosEsp.query.all()

    @staticmethod
    def get_servicio_esp_by_id(id_servicio_esp):
        """Obtener un servicio específico por su ID."""
        return ServiciosEsp.query.get(id_servicio_esp)

    @staticmethod
    def update_servicio_esp(servicio_esp, nombre_servicio_esp=None):
        """Actualizar la información de un servicio específico."""
        if nombre_servicio_esp:
            servicio_esp.nombre_servicio_esp = nombre_servicio_esp
        db.session.commit()
        return servicio_esp

    @staticmethod
    def delete_servicio_esp(servicio_esp):
        """Eliminar un servicio específico."""
        db.session.delete(servicio_esp)
        db.session.commit()