from flask import Blueprint,render_template
from models.cliente import Cliente
bp_cliente=Blueprint("clientes",__name__)
@bp_cliente.route("/clientes")
def clientes():
    return render_template("clientes.html",clientes=Cliente.query.all())
