from flask import Flask
from .config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from src.models.alcance import Alcance
from src.models.departamento import Departamento
from src.models.empresa import Empresa
from src.models.rango import Rango
from src.models.rango_empresa import Rangoempresa
from src.models.sede import Sede

from src.routes.get import get
from src.routes.get_empresasDeparjson import get_empresasede
from src.routes.get_empresasjson import get_empresas
from src.routes.get_sedes import get_sedes



def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db = SQLAlchemy(app)
    migrate = Migrate(app, db)

    app.register_blueprint(get)
    app.register_blueprint(get_sedes)
    app.register_blueprint(get_empresas)
    app.register_blueprint(get_empresasede)
    return app