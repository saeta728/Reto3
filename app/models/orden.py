from app import db
from app.models.cliente import Cliente
from app.models.vehiculo import Vehiculo

class Orden(db.Model):
    __tablename__ = 'orden'
    numero_orden = db.Column(db.Integer, primary_key=True, autoincrement=True)
    fecha_orden = db.Column(db.DateTime, default=db.func.current_timestamp(), nullable=False)
    numero_identificacion = db.Column(db.Integer, db.ForeignKey('cliente.numero_identificacion'), nullable=False)
    placa = db.Column(db.String(6), db.ForeignKey('vehiculo.placa'))

    # Relación con Cliente
    cliente = db.relationship('Cliente', backref='ordenes')

    """
    Esta línea establece una relación entre Orden y Cliente, 
    permitiendo que se acceda a las órdenes de un cliente desde 
    el modelo Cliente usando cliente.ordenes.
    """

    # Relación con Vehiculo
    vehiculo = db.relationship('Vehiculo', backref='ordenes')

    """
    Esta línea establece la relación entre Orden y Vehiculo, 
    permitiendo que se acceda a las órdenes de un vehículo 
    desde el modelo Vehiculo.
    """

    def __init__(self, numero_identificacion, placa):
        """
        Constructor de la clase Orden.

        Args:
            numero_identificacion (int): Número de identificación del cliente asociado a la orden.
            placa (str): Placa del vehículo asociado a la orden.
        """
        self.numero_identificacion = numero_identificacion
        self.placa = placa