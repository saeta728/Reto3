from flask import request, jsonify
from flask_restx import Namespace, Resource, fields
from app.services.orden_service import OrdenService

orden_ns = Namespace('ordenes', description="Operaciones relacionadas con órdenes")

# Definir el modelo de orden para la documentación de Swagger
orden_model = orden_ns.model('Orden', {
    'numero_identificacion': fields.Integer(required=True, description='Número de identificación del cliente'),
    'placa': fields.String(required=True, description='Placa del vehículo asociado')
})

# Modelo de salida para órdenes
orden_response_model = orden_ns.model('OrdenResponse', {
    'numero_orden': fields.Integer(description='Número de la orden'),
    'fecha_orden': fields.String(description='Fecha de la orden'),
    'numero_identificacion': fields.Integer(description='Número de identificación del cliente'),
    'placa': fields.String(description='Placa del vehículo asociado')
})

@orden_ns.route('/')
class OrdenList(Resource):
    @orden_ns.marshal_with(orden_response_model, as_list=True)
    def get(self):
        """Obtener todas las órdenes"""
        ordenes = OrdenService.get_all_ordenes()
        return ordenes

    @orden_ns.expect(orden_model)
    @orden_ns.marshal_with(orden_response_model, code=201)
    def post(self):
        """Crear una nueva orden"""
        data = request.get_json()
        nueva_orden = OrdenService.create_orden(
            numero_identificacion=data['numero_identificacion'],
            placa=data['placa']
        )
        return nueva_orden, 201

@orden_ns.route('/<int:numero_orden>')
class OrdenDetail(Resource):
    @orden_ns.marshal_with(orden_response_model)
    def get(self, numero_orden):
        """Obtener una orden por su número"""
        orden = OrdenService.get_orden_by_id(numero_orden)
        return orden

    def delete(self, numero_orden):
        """Eliminar una orden"""
        orden = OrdenService.get_orden_by_id(numero_orden)
        OrdenService.delete_orden(orden)
        return jsonify({'message': 'Orden eliminada correctamente'})
