from app import db
from app.models.vehiculo import Vehiculo

class VehiculoService:
    """Servicio para gestionar operaciones CRUD sobre los vehículos."""

    @staticmethod
    def create_vehiculo(placa, marca, modelo, referencia, descripcion=None, fecha_ingreso=None, fecha_pos_egreso=None):
        """Crear un nuevo vehículo."""
        nuevo_vehiculo = Vehiculo(
            placa=placa,
            marca=marca,
            modelo=modelo,
            referencia=referencia,
            descripcion=descripcion,
            fecha_ingreso=fecha_ingreso,
            fecha_pos_egreso=fecha_pos_egreso
        )
        db.session.add(nuevo_vehiculo)
        db.session.commit()
        return nuevo_vehiculo

    @staticmethod
    def get_all_vehiculos():
        """Obtener todos los vehículos."""
        return Vehiculo.query.all()

    @staticmethod
    def get_vehiculo_by_placa(placa):
        """Obtener un vehículo por su placa."""
        return Vehiculo.query.get(placa)

    @staticmethod
    def update_vehiculo(vehiculo, marca=None, modelo=None, referencia=None, descripcion=None, fecha_ingreso=None, fecha_pos_egreso=None):
        """Actualizar la información de un vehículo."""
        if marca:
            vehiculo.marca = marca
        if modelo:
            vehiculo.modelo = modelo
        if referencia:
            vehiculo.referencia = referencia
        if descripcion:
            vehiculo.descripcion = descripcion
        if fecha_ingreso:
            vehiculo.fecha_ingreso = fecha_ingreso
        if fecha_pos_egreso:
            vehiculo.fecha_pos_egreso = fecha_pos_egreso
        db.session.commit()
        return vehiculo

    @staticmethod
    def delete_vehiculo(vehiculo):
        """Eliminar un vehículo."""
        db.session.delete(vehiculo)
        db.session.commit()