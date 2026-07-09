from flask import Blueprint,render_template
from models.fornecedor import Fornecedor
bp_fornecedor=Blueprint("fornecedores",__name__)
@bp_fornecedor.route("/fornecedores")
def fornecedores():
    return render_template("fornecedores.html",fornecedores=Fornecedor.query.all())
