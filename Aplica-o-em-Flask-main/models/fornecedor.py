from . import db
from .base import BaseModel
class Fornecedor(BaseModel):
    __tablename__="tabela_fornecedor"
    nome_empresa=db.Column(db.String(100))
    cnpj=db.Column(db.String(20))
    produto_fornecido=db.Column(db.String(100))
