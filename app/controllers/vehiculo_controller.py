from flask import request, jsonify
from flask_restx import Namespace, Resource, fields
from app.services.vehiculo_service import VehiculoService

vehiculo_ns = Namespace('vehiculos', description="Operaciones relacionadas con vehículos")

# Definir el modelo de vehículo para la documentación de Swagger
vehiculo_model = vehiculo_ns.model('Vehiculo', {
    'placa': fields.String(required=True, description='Placa del vehículo'),
    'marca': fields.String(required=True, description='Marca del vehículo'),
    'modelo': fields.Integer(required=True, description='Modelo del vehículo'),
    'referencia': fields.String(required=True, description='Referencia del vehículo'),
    'descripcion': fields.String(description='Descripción del vehículo'),
    'fecha_ingreso': fields.String(description='Fecha de ingreso del vehículo'),
    'fecha_pos_egreso': fields.String(description='Fecha de posible egreso del vehículo')
})

# Modelo de salida para vehículos
vehiculo_response_model = vehiculo_ns.model('VehiculoResponse', {
    'placa': fields.String(description='Placa del vehículo'),
    'marca': fields.String(description='Marca del vehículo'),
    'modelo': fields.Integer(description='Modelo del vehículo'),
    'referencia': fields.String(description='Referencia del vehículo'),
    'descripcion': fields.String(description='Descripción del vehículo'),
    'fecha_ingreso': fields.String(description='Fecha de ingreso del vehículo'),
    'fecha_pos_egreso': fields.String(description='Fecha de posible egreso del vehículo')
})

@vehiculo_ns.route('/')
class VehiculoList(Resource):
    @vehiculo_ns.marshal_with(vehiculo_response_model, as_list=True)
    def get(self):
        """Obtener todos los vehículos"""
        vehiculos = VehiculoService.get_all_vehiculos()
        return vehiculos

    @vehiculo_ns.expect(vehiculo_model)
    @vehiculo_ns.marshal_with(vehiculo_response_model, code=201)
    def post(self):
        """Crear un nuevo vehículo"""
        data = request.get_json()
        nuevo_vehiculo = VehiculoService.create_vehiculo(
            placa=data['placa'],
            marca=data['marca'],
            modelo=data['modelo'],
            referencia=data['referencia'],
            descripcion=data.get('descripcion'),
            fecha_ingreso=data.get('fecha_ingreso'),
            fecha_pos_egreso=data.get('fecha_pos_egreso')
        )
        return nuevo_vehiculo, 201

@vehiculo_ns.route('/<string:placa>')
class VehiculoDetail(Resource):
    @vehiculo_ns.marshal_with(vehiculo_response_model)
    def get(self, placa):
        """Obtener un vehículo por su placa"""
        vehiculo = VehiculoService.get_vehiculo_by_placa(placa)
        return vehiculo

    @vehiculo_ns.expect(vehiculo_model)
    @vehiculo_ns.marshal_with(vehiculo_response_model)
    def put(self, placa):
        """Actualizar un vehículo"""
        vehiculo = VehiculoService.get_vehiculo_by_placa(placa)
        data = request.get_json()
        vehiculo = VehiculoService.update_vehiculo(
            vehiculo,
            marca=data.get('marca'),
            modelo=data.get('modelo'),
            referencia=data.get('referencia'),
            descripcion=data.get('descripcion'),
            fecha_ingreso=data.get('fecha_ingreso'),
            fecha_pos_egreso=data.get('fecha_pos_egreso')
        )
        return vehiculo

    def delete(self, placa):
        """Eliminar un vehículo"""
        vehiculo = VehiculoService.get_vehiculo_by_placa(placa)
        VehiculoService.delete_vehiculo(vehiculo)
        return jsonify({'message': 'Vehículo eliminado correctamente'})
