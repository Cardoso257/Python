from . import db
from .base import BaseModel
class Cliente(BaseModel):
    __tablename__="tabela_cliente"
    nome=db.Column(db.String(100))
    telefone=db.Column(db.String(20))
    pontos_fidelidade=db.Column(db.Integer,default=0)
