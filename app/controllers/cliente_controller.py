from flask import request, jsonify
from flask_restx import Namespace, Resource, fields
from app.services.cliente_service import ClienteService

cliente_ns = Namespace('clientes', description="Operaciones relacionadas con clientes")

# Definir el modelo de cliente para la documentación de Swagger
cliente_model = cliente_ns.model('Cliente', {
    'numero_identificacion': fields.Integer(required=True, description='Número de identificación del cliente'),
    'nombre_razon_social': fields.String(required=True, description='Nombre o razón social del cliente'),
    'telefono1': fields.Integer(required=True, description='Primer teléfono del cliente'),
    'telefono2': fields.Integer(description='Segundo teléfono del cliente'),
    'direccion': fields.String(description='Dirección del cliente'),
    'correo': fields.String(description='Correo electrónico del cliente')
})

# Modelo de salida para clientes
cliente_response_model = cliente_ns.model('ClienteResponse', {
    'numero_identificacion': fields.Integer(description='Número de identificación del cliente'),
    'nombre_razon_social': fields.String(description='Nombre o razón social del cliente'),
    'telefono1': fields.Integer(description='Primer teléfono del cliente'),
    'telefono2': fields.Integer(description='Segundo teléfono del cliente'),
    'direccion': fields.String(description='Dirección del cliente'),
    'correo': fields.String(description='Correo electrónico del cliente')
})

@cliente_ns.route('/')
class ClienteList(Resource):
    @cliente_ns.marshal_with(cliente_response_model, as_list=True)
    def get(self):
        """Obtener todos los clientes"""
        clientes = ClienteService.get_all_clientes()
        return clientes

    @cliente_ns.expect(cliente_model)
    @cliente_ns.marshal_with(cliente_response_model, code=201)
    def post(self):
        """Crear un nuevo cliente"""
        data = request.get_json()
        nuevo_cliente = ClienteService.create_cliente(
            numero_identificacion=data['numero_identificacion'],
            nombre_razon_social=data['nombre_razon_social'],
            telefono1=data['telefono1'],
            telefono2=data.get('telefono2'),
            direccion=data.get('direccion'),
            correo=data.get('correo')
        )
        return nuevo_cliente, 201

@cliente_ns.route('/<int:numero_identificacion>')
class ClienteDetail(Resource):
    @cliente_ns.marshal_with(cliente_response_model)
    def get(self, numero_identificacion):
        """Obtener un cliente por su número de identificación"""
        cliente = ClienteService.get_cliente_by_id(numero_identificacion)
        return cliente

    @cliente_ns.expect(cliente_model)
    @cliente_ns.marshal_with(cliente_response_model)
    def put(self, numero_identificacion):
        """Actualizar un cliente"""
        cliente = ClienteService.get_cliente_by_id(numero_identificacion)
        data = request.get_json()
        cliente = ClienteService.update_cliente(
            cliente,
            nombre_razon_social=data.get('nombre_razon_social'),
            telefono1=data.get('telefono1'),
            telefono2=data.get('telefono2'),
            direccion=data.get('direccion'),
            correo=data.get('correo')
        )
        return cliente

    def delete(self, numero_identificacion):
        """Eliminar un cliente"""
        cliente = ClienteService.get_cliente_by_id(numero_identificacion)
        ClienteService.delete_cliente(cliente)
        return jsonify({'message': 'Cliente eliminado correctamente'})


