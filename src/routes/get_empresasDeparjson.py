from flask import Blueprint, jsonify
from src.models.sede import Sede
from flask_marshmallow import Marshmallow
from app import app

ma= Marshmallow(app)

class SedeSchema(ma.Schema):
    class Meta:
        fields= ('id_sede', 'id_empresa', 'id_departamento')
        model= Sede

sede_schema= SedeSchema()
sede_schema= SedeSchema(many=True)



get_empresasede = Blueprint('get', __name__)

@get_empresasede.route("/empresa_departamento")
def ver_empresa_departamento():
    sedes = Sede.query.all()
    resultado= sede_schema.dump(sedes)
    return jsonify(resultado)


