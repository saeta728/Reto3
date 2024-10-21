from app import db
from app.models.servicios_gen import ServiciosGen

class ServiciosGenService:
    """Servicio para gestionar operaciones CRUD sobre los servicios generales."""

    @staticmethod
    def create_servicio_gen(nombre_servicio_gen):
        """Crear un nuevo servicio general."""
        nuevo_servicio_gen = ServiciosGen(nombre_servicio_gen=nombre_servicio_gen)
        db.session.add(nuevo_servicio_gen)
        db.session.commit()
        return nuevo_servicio_gen

    @staticmethod
    def get_all_servicios_gen():
        """Obtener todos los servicios generales."""
        return ServiciosGen.query.all()

    @staticmethod
    def get_servicio_gen_by_id(id_servicio_gen):
        """Obtener un servicio general por su ID."""
        return ServiciosGen.query.get(id_servicio_gen)

    @staticmethod
    def update_servicio_gen(servicio_gen, nombre_servicio_gen=None):
        """Actualizar la información de un servicio general."""
        if nombre_servicio_gen:
            servicio_gen.nombre_servicio_gen = nombre_servicio_gen
        db.session.commit()
        return servicio_gen

    @staticmethod
    def delete_servicio_gen(servicio_gen):
        """Eliminar un servicio general."""
        db.session.delete(servicio_gen)
        db.session.commit()