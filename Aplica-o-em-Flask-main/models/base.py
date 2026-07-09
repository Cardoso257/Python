from . import db
from datetime import datetime
class BaseModel(db.Model):
    __abstract__=True
    id=db.Column(db.Integer,primary_key=True)
    data_criacao=db.Column(db.DateTime,default=datetime.utcnow)
    data_atualizacao=db.Column(db.DateTime,default=datetime.utcnow,onupdate=datetime.utcnow)
