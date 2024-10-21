from app import db

class Insumos(db.Model):
    __tablename__ = 'insumos'
    id_insumo = db.Column(db.Integer, primary_key=True, autoincrement=True)
    insumos = db.Column(db.String(100), nullable=False)

    def __init__(self, insumos):
        """
        Constructor de la clase Insumos.

        Args:
            insumos (str): Nombre del insumo.
        """
        self.insumos = insumos
