from flask import request, jsonify
from flask_restx import Namespace, Resource, fields
from app.services.servicios_gen_service import ServiciosGenService

servicio_gen_ns = Namespace('servicios_gen', description="Operaciones relacionadas con servicios generales")

# Definir el modelo de servicio general para la documentación de Swagger
servicio_gen_model = servicio_gen_ns.model('ServicioGen', {
    'nombre_servicio_gen': fields.String(required=True, description='Nombre del servicio general')
})

# Modelo de salida para servicios generales
servicio_gen_response_model = servicio_gen_ns.model('ServicioGenResponse', {
    'id_servicio_gen': fields.Integer(description='ID del servicio general'),
    'nombre_servicio_gen': fields.String(description='Nombre del servicio general')
})

@servicio_gen_ns.route('/')
class ServiciosGenList(Resource):
    @servicio_gen_ns.marshal_with(servicio_gen_response_model, as_list=True)
    def get(self):
        """Obtener todos los servicios generales"""
        servicios = ServiciosGenService.get_all_servicios_gen()
        return servicios

    @servicio_gen_ns.expect(servicio_gen_model)
    @servicio_gen_ns.marshal_with(servicio_gen_response_model, code=201)
    def post(self):
        """Crear un nuevo servicio general"""
        data = request.get_json()
        nuevo_servicio = ServiciosGenService.create_servicio_gen(nombre_servicio_gen=data['nombre_servicio_gen'])
        return nuevo_servicio, 201

@servicio_gen_ns.route('/<int:id_servicio_gen>')
class ServiciosGenDetail(Resource):
    @servicio_gen_ns.marshal_with(servicio_gen_response_model)
    def get(self, id_servicio_gen):
        """Obtener un servicio general por su ID"""
        servicio = ServiciosGenService.get_servicio_gen_by_id(id_servicio_gen)
        return servicio

    @servicio_gen_ns.expect(servicio_gen_model)
    @servicio_gen_ns.marshal_with(servicio_gen_response_model)
    def put(self, id_servicio_gen):
        """Actualizar un servicio general"""
        servicio = ServiciosGenService.get_servicio_gen_by_id(id_servicio_gen)
        data = request.get_json()
        servicio = ServiciosGenService.update_servicio_gen(servicio, nombre_servicio_gen=data.get('nombre_servicio_gen'))
        return servicio

    def delete(self, id_servicio_gen):
        """Eliminar un servicio general"""
        servicio = ServiciosGenService.get_servicio_gen_by_id(id_servicio_gen)
        ServiciosGenService.delete_servicio_gen(servicio)
        return jsonify({'message': 'Servicio eliminado correctamente'})
