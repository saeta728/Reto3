from app import db
from app.models.cliente import Cliente

class ClienteService:
    """Servicio para gestionar operaciones CRUD sobre los clientes."""

    @staticmethod
    def create_cliente(numero_identificacion, nombre_razon_social, telefono1, telefono2=None, direccion=None, correo=None):
        """Crear un nuevo cliente."""
        nuevo_cliente = Cliente(
            numero_identificacion=numero_identificacion,
            nombre_razon_social=nombre_razon_social,
            telefono1=telefono1,
            telefono2=telefono2,
            direccion=direccion,
            correo=correo
        )
        db.session.add(nuevo_cliente)
        db.session.commit()
        return nuevo_cliente

    @staticmethod
    def get_all_clientes():
        """Obtener todos los clientes."""
        return Cliente.query.all()

    @staticmethod
    def get_cliente_by_id(numero_identificacion):
        """Obtener un cliente por su número de identificación."""
        return Cliente.query.get(numero_identificacion)

    @staticmethod
    def update_cliente(cliente, nombre_razon_social=None, telefono1=None, telefono2=None, direccion=None, correo=None):
        """Actualizar la información de un cliente."""
        if nombre_razon_social:
            cliente.nombre_razon_social = nombre_razon_social
        if telefono1:
            cliente.telefono1 = telefono1
        if telefono2:
            cliente.telefono2 = telefono2
        if direccion:
            cliente.direccion = direccion
        if correo:
            cliente.correo = correo
        db.session.commit()
        return cliente

    @staticmethod
    def delete_cliente(cliente):
        """Eliminar un cliente."""
        db.session.delete(cliente)
        db.session.commit()