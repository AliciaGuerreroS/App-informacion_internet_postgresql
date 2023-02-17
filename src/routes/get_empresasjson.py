from flask import Blueprint, jsonify
from src.models.empresa import Empresa
from flask_marshmallow import Marshmallow
from app import app

ma= Marshmallow(app)

class EmpresaSchema(ma.Schema):
    class Meta:
        fields= ('id_empresa', 'nombre', 'estado', 'id_segmento')
        model= Empresa

empresa_schema= EmpresaSchema()
empresa_schema= EmpresaSchema(many=True)



get_empresas = Blueprint('get', __name__)

@get_empresas.route("/empresas")
def ver_empresas():
    empresas = Empresa.query.all()
    resultado= empresa_schema.dump(empresas)
    return jsonify(resultado)

