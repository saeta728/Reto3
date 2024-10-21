from flask import request, jsonify
from flask_restx import Namespace, Resource, fields
from app.services.servicios_esp_service import ServiciosEspService

servicio_esp_ns = Namespace('servicios_esp', description="Operaciones relacionadas con servicios específicos")

# Definir el modelo de servicio específico para la documentación de Swagger
servicio_esp_model = servicio_esp_ns.model('ServicioEsp', {
    'nombre_servicio_esp': fields.String(required=True, description='Nombre del servicio específico')
})

# Modelo de salida para servicios específicos
servicio_esp_response_model = servicio_esp_ns.model('ServicioEspResponse', {
    'id_servicio_esp': fields.Integer(description='ID del servicio específico'),
    'nombre_servicio_esp': fields.String(description='Nombre del servicio específico')
})

@servicio_esp_ns.route('/')
class ServiciosEspList(Resource):
    @servicio_esp_ns.marshal_with(servicio_esp_response_model, as_list=True)
    def get(self):
        """Obtener todos los servicios específicos"""
        servicios = ServiciosEspService.get_all_servicios_esp()
        return servicios

    @servicio_esp_ns.expect(servicio_esp_model)
    @servicio_esp_ns.marshal_with(servicio_esp_response_model, code=201)
    def post(self):
        """Crear un nuevo servicio específico"""
        data = request.get_json()
        nuevo_servicio = ServiciosEspService.create_servicio_esp(nombre_servicio_esp=data['nombre_servicio_esp'])
        return nuevo_servicio, 201

@servicio_esp_ns.route('/<int:id_servicio_esp>')
class ServiciosEspDetail(Resource):
    @servicio_esp_ns.marshal_with(servicio_esp_response_model)
    def get(self, id_servicio_esp):
        """Obtener un servicio específico por su ID"""
        servicio = ServiciosEspService.get_servicio_esp_by_id(id_servicio_esp)
        return servicio

    @servicio_esp_ns.expect(servicio_esp_model)
    @servicio_esp_ns.marshal_with(servicio_esp_response_model)
    def put(self, id_servicio_esp):
        """Actualizar un servicio específico"""
        servicio = ServiciosEspService.get_servicio_esp_by_id(id_servicio_esp)
        data = request.get_json()
        servicio = ServiciosEspService.update_servicio_esp(servicio, nombre_servicio_esp=data.get('nombre_servicio_esp'))
        return servicio

    def delete(self, id_servicio_esp):
        """Eliminar un servicio específico"""
        servicio = ServiciosEspService.get_servicio_esp_by_id(id_servicio_esp)
        ServiciosEspService.delete_servicio_esp(servicio)
        return jsonify({'message': 'Servicio eliminado correctamente'})
