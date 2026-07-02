from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///escola.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)


class Aluno(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    telefone = db.Column(db.String(20), nullable=False) 


with app.app_context():
    db.create_all()


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        nome = request.form['nome']
        telefone = request.form['telefone']
        
  
        novo_aluno = Aluno(nome=nome, telefone=telefone)
        db.session.add(novo_aluno)
        db.session.commit() 
        
        return redirect(url_for('index'))
    
   
    alunos = Aluno.query.order_by(Aluno.id.desc()).all()
    
 
    total_alunos = Aluno.query.count()
    
    return render_template('index.html', alunos=alunos, total_alunos=total_alunos)


@app.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    aluno = Aluno.query.get_or_404(id)
    
    if request.method == 'POST':
      
        aluno.nome = request.form['nome']
        aluno.telefone = request.form['telefone']
        db.session.commit()
        return redirect(url_for('index'))
        
    return render_template('editar.html', aluno=aluno)


@app.route('/deletar/<int:id>')
def deletar(id):
    aluno = Aluno.query.get_or_404(id)
    
  
    db.session.delete(aluno)
    db.session.commit()
    
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)