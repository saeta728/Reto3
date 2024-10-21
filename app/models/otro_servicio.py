from app import db

class OtroServicio(db.Model):
    __tablename__ = 'otro_servicio'
    id_otro_servicio = db.Column(db.Integer, primary_key=True, autoincrement=True)
    otro_servicio = db.Column(db.String(100), nullable=False)

    def __init__(self, otro_servicio):
        """
        Constructor de la clase OtroServicio.

        Args:
            otro_servicio (str): Descripción del otro servicio.
        """
        self.otro_servicio = otro_servicio
