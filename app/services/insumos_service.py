from app import db
from app.models.insumos import Insumos

class InsumosService:
    """Servicio para gestionar operaciones CRUD sobre los insumos."""

    @staticmethod
    def create_insumo(insumos):
        """Crear un nuevo insumo."""
        nuevo_insumo = Insumos(insumos=insumos)
        db.session.add(nuevo_insumo)
        db.session.commit()
        return nuevo_insumo

    @staticmethod
    def get_all_insumos():
        """Obtener todos los insumos."""
        return Insumos.query.all()

    @staticmethod
    def get_insumo_by_id(id_insumo):
        """Obtener un insumo por su ID."""
        return Insumos.query.get(id_insumo)

    @staticmethod
    def update_insumo(insumo, nuevo_insumo=None):
        """Actualizar la información de un insumo."""
        if nuevo_insumo:
            insumo.insumos = nuevo_insumo
        db.session.commit()
        return insumo

    @staticmethod
    def delete_insumo(insumo):
        """Eliminar un insumo."""
        db.session.delete(insumo)
        db.session.commit()