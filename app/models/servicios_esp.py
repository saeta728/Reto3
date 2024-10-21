from app import db

class ServiciosEsp(db.Model):
    __tablename__ = 'servicios_esp'
    id_servicio_esp = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre_servicio_esp = db.Column(db.String(255), nullable=False)

    def __init__(self, nombre_servicio_esp):
        """
        Constructor de la clase ServiciosEsp.

        Args:
            nombre_servicio_esp (str): Nombre del servicio específico.
        """
        self.nombre_servicio_esp = nombre_servicio_esp
