from app import db

class Vehiculo(db.Model):
    __tablename__ = 'vehiculo'
    placa = db.Column(db.String(6), primary_key=True)
    marca = db.Column(db.String(20), nullable=False)
    modelo = db.Column(db.Integer, nullable=False)
    referencia = db.Column(db.String(50), nullable=False)
    descripcion = db.Column(db.String(255))
    fecha_ingreso = db.Column(db.Date, default=db.func.current_date())
    fecha_pos_egreso = db.Column(db.Date)

    def __init__(self, placa, marca, modelo, referencia, descripcion=None, fecha_ingreso=None, fecha_pos_egreso=None):
        """
        Constructor de la clase Vehiculo.

        Args:
            placa (str): Placa del vehículo.
            marca (str): Marca del vehículo.
            modelo (int): Modelo del vehículo.
            referencia (str): Referencia del vehículo.
            descripcion (str, opcional): Descripción del vehículo.
            fecha_ingreso (date, opcional): Fecha de ingreso del vehículo.
            fecha_pos_egreso (date, opcional): Fecha de posible egreso del vehículo.
        """
        self.placa = placa
        self.marca = marca
        self.modelo = modelo
        self.referencia = referencia
        self.descripcion = descripcion
        self.fecha_ingreso = fecha_ingreso
        self.fecha_pos_egreso = fecha_pos_egreso