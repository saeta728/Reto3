from app import db
from app.models.detalle_orden import DetalleOrden

class DetalleOrdenService:
    """Servicio para gestionar operaciones CRUD sobre los detalles de las órdenes."""

    @staticmethod
    def create_detalle_orden(numero_orden, id_servicio_gen, id_servicio_esp, id_otro_servicio=None, id_insumo=None, cantidad=1, precio=0.0):
        """Crear un nuevo detalle de orden."""
        nuevo_detalle = DetalleOrden(
            numero_orden=numero_orden,
            id_servicio_gen=id_servicio_gen,
            id_servicio_esp=id_servicio_esp,
            id_otro_servicio=id_otro_servicio,
            id_insumo=id_insumo,
            cantidad=cantidad,
            precio=precio
        )
        db.session.add(nuevo_detalle)
        db.session.commit()
        return nuevo_detalle

    @staticmethod
    def get_all_detalles_orden():
        """Obtener todos los detalles de órdenes."""
        return DetalleOrden.query.all()

    @staticmethod
    def get_detalle_orden_by_id(id_detalle):
        """Obtener un detalle de orden por su ID."""
        return DetalleOrden.query.get(id_detalle)

    @staticmethod
    def delete_detalle_orden(detalle_orden):
        """Eliminar un detalle de orden."""
        db.session.delete(detalle_orden)
        db.session.commit()