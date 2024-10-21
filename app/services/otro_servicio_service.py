from app import db
from app.models.otro_servicio import OtroServicio

class OtroServicioService:
    """Servicio para gestionar operaciones CRUD sobre otros servicios."""

    @staticmethod
    def create_otro_servicio(otro_servicio):
        """Crear un nuevo otro servicio."""
        nuevo_otro_servicio = OtroServicio(otro_servicio=otro_servicio)
        db.session.add(nuevo_otro_servicio)
        db.session.commit()
        return nuevo_otro_servicio

    @staticmethod
    def get_all_otros_servicios():
        """Obtener todos los otros servicios."""
        return OtroServicio.query.all()

    @staticmethod
    def get_otro_servicio_by_id(id_otro_servicio):
        """Obtener un otro servicio por su ID."""
        return OtroServicio.query.get(id_otro_servicio)

    @staticmethod
    def update_otro_servicio(otro_servicio, nuevo_otro_servicio=None):
        """Actualizar la información de un otro servicio."""
        if nuevo_otro_servicio:
            otro_servicio.otro_servicio = nuevo_otro_servicio
        db.session.commit()
        return otro_servicio

    @staticmethod
    def delete_otro_servicio(otro_servicio):
        """Eliminar un otro servicio."""
        db.session.delete(otro_servicio)
        db.session.commit()