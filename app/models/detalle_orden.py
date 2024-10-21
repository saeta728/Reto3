from app import db
from app.models.orden import Orden
from app.models.servicios_gen import ServiciosGen
from app.models.servicios_esp import ServiciosEsp
from app.models.otro_servicio import OtroServicio
from app.models.insumos import Insumos

class DetalleOrden(db.Model):
    __tablename__ = 'detalle_orden'
    id_detalle = db.Column(db.Integer, primary_key=True, autoincrement=True)
    numero_orden = db.Column(db.Integer, db.ForeignKey('orden.numero_orden'))
    id_servicio_gen = db.Column(db.Integer, db.ForeignKey('servicios_gen.id_servicio_gen'))
    id_servicio_esp = db.Column(db.Integer, db.ForeignKey('servicios_esp.id_servicio_esp'))
    id_otro_servicio = db.Column(db.Integer, db.ForeignKey('otro_servicio.id_otro_servicio'), nullable=True)
    id_insumo = db.Column(db.Integer, db.ForeignKey('insumos.id_insumo'), nullable=True)
    cantidad = db.Column(db.Integer, default=1)
    precio = db.Column(db.Numeric(10, 2), nullable=False)

    # Relación con Orden, Relaciona con el modelo Orden, lo que permite acceder a los detalles de una orden desde el modelo Orden.
    orden = db.relationship('Orden', backref='detalles')

    # Relación con ServiciosGen, permite acceder a los detalles que tienen un servicio general asociado.
    servicio_gen = db.relationship('ServiciosGen', backref='detalles')

    # Relación con ServiciosEsp, permite acceder a los detalles que tienen un servicio específico asociado.
    servicio_esp = db.relationship('ServiciosEsp', backref='detalles')

    # Relación con OtroServicio, permite acceder a los detalles que tienen otro servicio asociado.
    otro_servicio = db.relationship('OtroServicio', backref='detalles')

    # Relación con Insumos, permite acceder a los detalles que tienen insumos asociados.
    insumo = db.relationship('Insumos', backref='detalles')

    def __init__(self, numero_orden, id_servicio_gen, id_servicio_esp, id_otro_servicio=None, id_insumo=None, cantidad=1, precio=0.0):
        """
        Constructor de la clase DetalleOrden.

        Args:
            numero_orden (int): Número de la orden asociada.
            id_servicio_gen (int): ID del servicio general asociado.
            id_servicio_esp (int): ID del servicio específico asociado.
            id_otro_servicio (int, opcional): ID de otro servicio asociado.
            id_insumo (int, opcional): ID del insumo asociado.
            cantidad (int, opcional): Cantidad de servicios/insumos. Valor por defecto es 1.
            precio (float): Precio del servicio o insumo.
        """
        self.numero_orden = numero_orden
        self.id_servicio_gen = id_servicio_gen
        self.id_servicio_esp = id_servicio_esp
        self.id_otro_servicio = id_otro_servicio
        self.id_insumo = id_insumo
        self.cantidad = cantidad
        self.precio = precio
