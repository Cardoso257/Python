# models/__init__.py
from flask_sqlalchemy import SQLAlchemy

# Instancia o banco de dados
db = SQLAlchemy()

# Importa o model para que o app reconheça na hora de criar as tabelas
from .operacao import Operacao

__all__ = ["db", "Operacao"]