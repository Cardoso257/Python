from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # Dados para os exercícios 1 e 2
    nome_usuario = "Carlos"
    idade_usuario = 25
    
    # Dados para o exercício 3 (Dicionário)
    usuario_dic = {"nome": "Ana", "email": "ana@email.com"}
    
    # Dados para o exercício 4 (Lista de alunos)
    lista_alunos = [
        {"nome": "Bruno"},
        {"nome": "Beatriz"},
        {"nome": "Daniel"}
    ]
    
    # Dados para o exercício 5 (Condicional de Nota)
    nota_aluno = 8.5  # Mude aqui para testar o "Reprovado" depois!

    return render_template(
        'index.html', 
        nome=nome_usuario, 
        idade=idade_usuario,
        usuario=usuario_dic,
        alunos=lista_alunos,
        nota=nota_aluno
    )

if __name__ == '__main__':
    app.run(debug=True)