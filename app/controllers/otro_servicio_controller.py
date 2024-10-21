from flask import request, jsonify
from flask_restx import Namespace, Resource, fields
from app.services.otro_servicio_service import OtroServicioService

otro_servicio_ns = Namespace('otro_servicio', description="Operaciones relacionadas con otros servicios")

# Definir el modelo de otro servicio para la documentación de Swagger
otro_servicio_model = otro_servicio_ns.model('OtroServicio', {
    'otro_servicio': fields.String(required=True, description='Nombre del otro servicio')
})

# Modelo de salida para otros servicios
otro_servicio_response_model = otro_servicio_ns.model('OtroServicioResponse', {
    'id_otro_servicio': fields.Integer(description='ID del otro servicio'),
    'otro_servicio': fields.String(description='Nombre del otro servicio')
})

@otro_servicio_ns.route('/')
class OtroServicioList(Resource):
    @otro_servicio_ns.marshal_with(otro_servicio_response_model, as_list=True)
    def get(self):
        """Obtener todos los otros servicios"""
        servicios = OtroServicioService.get_all_otros_servicios()
        return servicios

    @otro_servicio_ns.expect(otro_servicio_model)
    @otro_servicio_ns.marshal_with(otro_servicio_response_model, code=201)
    def post(self):
        """Crear un nuevo otro servicio"""
        data = request.get_json()
        nuevo_servicio = OtroServicioService.create_otro_servicio(otro_servicio=data['otro_servicio'])
        return nuevo_servicio, 201

@otro_servicio_ns.route('/<int:id_otro_servicio>')
class OtroServicioDetail(Resource):
    @otro_servicio_ns.marshal_with(otro_servicio_response_model)
    def get(self, id_otro_servicio):
        """Obtener un otro servicio por su ID"""
        servicio = OtroServicioService.get_otro_servicio_by_id(id_otro_servicio)
        return servicio

    @otro_servicio_ns.expect(otro_servicio_model)
    @otro_servicio_ns.marshal_with(otro_servicio_response_model)
    def put(self, id_otro_servicio):
        """Actualizar un otro servicio"""
        servicio = OtroServicioService.get_otro_servicio_by_id(id_otro_servicio)
        data = request.get_json()
        servicio = OtroServicioService.update_otro_servicio(servicio, nuevo_otro_servicio=data.get('otro_servicio'))
        return servicio

    def delete(self, id_otro_servicio):
        """Eliminar un otro servicio"""
        servicio = OtroServicioService.get_otro_servicio_by_id(id_otro_servicio)
        OtroServicioService.delete_otro_servicio(servicio)
        return jsonify({'message': 'Otro servicio eliminado correctamente'})
