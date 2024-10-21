from app import db

class ServiciosGen(db.Model):
    __tablename__ = 'servicios_gen'
    id_servicio_gen = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre_servicio_gen = db.Column(db.String(150), nullable=False)

    def __init__(self, nombre_servicio_gen):
        """
        Constructor de la clase ServiciosGen.

        Args:
            nombre_servicio_gen (str): Nombre del servicio general.
        """
        self.nombre_servicio_gen = nombre_servicio_gen