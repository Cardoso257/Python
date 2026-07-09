from flask import Flask,render_template
from models import db
from controllers.cliente_controller import bp_cliente
from controllers.fornecedor_controller import bp_fornecedor
from models.cliente import Cliente
from models.fornecedor import Fornecedor
def create_app():
    app=Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///lanchonete.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False
    db.init_app(app)
    @app.route("/")
    def home(): return render_template("index.html")
    app.register_blueprint(bp_cliente)
    app.register_blueprint(bp_fornecedor)
    with app.app_context(): db.create_all()
    return app
app=create_app()
if __name__=="__main__": app.run(debug=True)
