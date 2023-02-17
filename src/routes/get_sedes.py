from flask import Blueprint, jsonify
from src.models.departamento import Departamento
from flask_marshmallow import Marshmallow
from app import app

ma= Marshmallow(app)

class DepartamentoSchema(ma.Schema):
    class Meta:
        fields= ('id_departamento', 'nombre')
        model= Departamento

departamento_schema= DepartamentoSchema()
departamento_schema= DepartamentoSchema(many=True)



get_sedes = Blueprint('get', __name__)

@get_sedes.route("/sedes")
def ver_sedes():
    departamento = Departamento.query.all()
    resultado= departamento_schema.dump(departamento)
    return jsonify(resultado)



