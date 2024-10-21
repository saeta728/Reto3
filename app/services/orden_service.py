from app import db
from app.models.orden import Orden

class OrdenService:
    """Servicio para gestionar operaciones CRUD sobre las órdenes."""

    @staticmethod
    def create_orden(numero_identificacion, placa):
        """Crear una nueva orden."""
        nueva_orden = Orden(
            numero_identificacion=numero_identificacion,
            placa=placa
        )
        db.session.add(nueva_orden)
        db.session.commit()
        return nueva_orden

    @staticmethod
    def get_all_ordenes():
        """Obtener todas las órdenes."""
        return Orden.query.all()

    @staticmethod
    def get_orden_by_id(numero_orden):
        """Obtener una orden por su número."""
        return Orden.query.get(numero_orden)

    @staticmethod
    def delete_orden(orden):
        """Eliminar una orden."""
        db.session.delete(orden)
        db.session.commit()