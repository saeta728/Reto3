from app import db


class Cliente(db.Model):
    __tablename__ = 'cliente'
    numero_identificacion = db.Column(db.Integer, primary_key=True)
    nombre_razon_social = db.Column(db.String(255), nullable=False)
    telefono1 = db.Column(db.BigInteger, nullable=False)
    telefono2 = db.Column(db.BigInteger)
    direccion = db.Column(db.String(150))
    correo = db.Column(db.String(100))

    def __init__(self, numero_identificacion, nombre_razon_social, telefono1, telefono2=None, direccion=None, correo=None):
        """
        Constructor de la clase Cliente.

        Args:
            numero_identificacion (int): Número de identificación del cliente.
            nombre_razon_social (str): Nombre o razón social del cliente.
            telefono1 (int): Primer número de teléfono del cliente.
            telefono2 (int, opcional): Segundo número de teléfono del cliente.
            direccion (str, opcional): Dirección del cliente.
            correo (str, opcional): Correo electrónico del cliente.
        """
        self.numero_identificacion = numero_identificacion
        self.nombre_razon_social = nombre_razon_social
        self.telefono1 = telefono1
        self.telefono2 = telefono2
        self.direccion = direccion
        self.correo = correo

        """
        Se agregan los constructores a cada modelo para que al momento de crear instancias de estos objetos en la API, 
        se puedan inicializar con los valores necesarios. 
        Esto permite que las entidades sean fácilmente manejables cuando se interactúa con la base de datos 
        mediante las operaciones CRUD.
        """