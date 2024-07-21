from flask import Flask
from app.controllers.lancamento_controller import app as lancamento_app
from app.controllers.consolidado_controller import app as consolidado_app

app = Flask(__name__)
app.register_blueprint(lancamento_app)
app.register_blueprint(consolidado_app)

if __name__ == '__main__':
    app.run(debug=True)
