from flask import Blueprint, render_template
from src.models.empresa import Empresa


get = Blueprint('get', __name__)

@get.route("/")
def home():
    todas_empresas = Empresa.query.order_by("id_empresa").all()
    return render_template("inicio.html", todas_empresas=todas_empresas)

