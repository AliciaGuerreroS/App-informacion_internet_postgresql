from src import create_app
from src.db import db
from src.models.alcance import Alcance
from src.models.departamento import Departamento
from src.models.empresa import Empresa
from src.models.rango_empresa import Rangoempresa
from src.models.rango import Rango


app = create_app()

db.init_app(app)
with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)
