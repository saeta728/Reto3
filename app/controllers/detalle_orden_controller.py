from flask import request, jsonify
from flask_restx import Namespace, Resource, fields
from app.services.detalle_orden_service import DetalleOrdenService

detalle_orden_ns = Namespace('detalle_orden', description="Operaciones relacionadas con detalles de órdenes")

# Definir el modelo de detalle de orden para la documentación de Swagger
detalle_orden_model = detalle_orden_ns.model('DetalleOrden', {
    'numero_orden': fields.Integer(required=True, description='Número de la orden asociada'),
    'id_servicio_gen': fields.Integer(required=True, description='ID del servicio general'),
    'id_servicio_esp': fields.Integer(required=True, description='ID del servicio específico'),
    'id_otro_servicio': fields.Integer(description='ID de otro servicio asociado'),
    'id_insumo': fields.Integer(description='ID del insumo asociado'),
    'cantidad': fields.Integer(description='Cantidad del servicio o insumo'),
    'precio': fields.Float(required=True, description='Precio del servicio o insumo')
})

# Modelo de salida para detalles de órdenes
detalle_orden_response_model = detalle_orden_ns.model('DetalleOrdenResponse', {
    'id_detalle': fields.Integer(description='ID del detalle de la orden'),
    'numero_orden': fields.Integer(description='Número de la orden asociada'),
    'id_servicio_gen': fields.Integer(description='ID del servicio general'),
    'id_servicio_esp': fields.Integer(description='ID del servicio específico'),
    'id_otro_servicio': fields.Integer(description='ID de otro servicio asociado'),
    'id_insumo': fields.Integer(description='ID del insumo asociado'),
    'cantidad': fields.Integer(description='Cantidad del servicio o insumo'),
    'precio': fields.Float(description='Precio del servicio o insumo')
})

@detalle_orden_ns.route('/')
class DetalleOrdenList(Resource):
    @detalle_orden_ns.marshal_with(detalle_orden_response_model, as_list=True)
    def get(self):
        """Obtener todos los detalles de órdenes"""
        detalles = DetalleOrdenService.get_all_detalles_orden()
        return detalles

    @detalle_orden_ns.expect(detalle_orden_model)
    @detalle_orden_ns.marshal_with(detalle_orden_response_model, code=201)
    def post(self):
        """Crear un nuevo detalle de orden"""
        data = request.get_json()
        nuevo_detalle = DetalleOrdenService.create_detalle_orden(
            numero_orden=data['numero_orden'],
            id_servicio_gen=data['id_servicio_gen'],
            id_servicio_esp=data['id_servicio_esp'],
            id_otro_servicio=data.get('id_otro_servicio'),
            id_insumo=data.get('id_insumo'),
            cantidad=data.get('cantidad', 1),
            precio=data['precio']
        )
        return nuevo_detalle, 201

@detalle_orden_ns.route('/<int:id_detalle>')
class DetalleOrdenDetail(Resource):
    @detalle_orden_ns.marshal_with(detalle_orden_response_model)
    def get(self, id_detalle):
        """Obtener un detalle de orden por su ID"""
        detalle = DetalleOrdenService.get_detalle_orden_by_id(id_detalle)
        return detalle

    def delete(self, id_detalle):
        """Eliminar un detalle de orden"""
        detalle = DetalleOrdenService.get_detalle_orden_by_id(id_detalle)
        DetalleOrdenService.delete_detalle_orden(detalle)
        return jsonify({'message': 'Detalle de orden eliminado correctamente'})
