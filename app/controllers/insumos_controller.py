from flask import request, jsonify
from flask_restx import Namespace, Resource, fields
from app.services.insumos_service import InsumosService

insumos_ns = Namespace('insumos', description="Operaciones relacionadas con insumos")

# Definir el modelo de insumo para la documentación de Swagger
insumo_model = insumos_ns.model('Insumo', {
    'insumos': fields.String(required=True, description='Nombre del insumo')
})

# Modelo de salida para insumos
insumo_response_model = insumos_ns.model('InsumoResponse', {
    'id_insumo': fields.Integer(description='ID del insumo'),
    'insumos': fields.String(description='Nombre del insumo')
})

@insumos_ns.route('/')
class InsumosList(Resource):
    @insumos_ns.marshal_with(insumo_response_model, as_list=True)
    def get(self):
        """Obtener todos los insumos"""
        insumos = InsumosService.get_all_insumos()
        return insumos

    @insumos_ns.expect(insumo_model)
    @insumos_ns.marshal_with(insumo_response_model, code=201)
    def post(self):
        """Crear un nuevo insumo"""
        data = request.get_json()
        nuevo_insumo = InsumosService.create_insumo(insumos=data['insumos'])
        return nuevo_insumo, 201

@insumos_ns.route('/<int:id_insumo>')
class InsumosDetail(Resource):
    @insumos_ns.marshal_with(insumo_response_model)
    def get(self, id_insumo):
        """Obtener un insumo por su ID"""
        insumo = InsumosService.get_insumo_by_id(id_insumo)
        return insumo

    @insumos_ns.expect(insumo_model)
    @insumos_ns.marshal_with(insumo_response_model)
    def put(self, id_insumo):
        """Actualizar un insumo"""
        insumo = InsumosService.get_insumo_by_id(id_insumo)
        data = request.get_json()
        insumo = InsumosService.update_insumo(insumo, nuevo_insumo=data.get('insumos'))
        return insumo

    def delete(self, id_insumo):
        """Eliminar un insumo"""
        insumo = InsumosService.get_insumo_by_id(id_insumo)
        InsumosService.delete_insumo(insumo)
        return jsonify({'message': 'Insumo eliminado correctamente'})
