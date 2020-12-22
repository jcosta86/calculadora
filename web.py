from flask import Flask

from calculadora.calculator import addition, subtaction, division, multiplication

app = Flask(__name__)


@app.route('/')  # Rota principal
def index():
    h1 = '<h1>Calculadora olist</h1>'
    ol = '''
            <ol> 
                <li><a href='/soma'>Somar</a></li>
                <li><a href='/divide'>Dividir</a></li>
                <li><a href='/multiplica'>Multiplicar</a></li>
                <li><a href='/subtrai'>Subtrair</a></li>
            </ol>
          '''
    return f'{h1} {ol}'


@app.route('/soma')
def soma():
    num_1 = 3.0
    num_2 = 5.0
    resultado = addition(num_1, num_2)
    h1 = '<h1>Soma olisters</h1>'
    h3 = f'<h3> A soma de 3+5 é: {resultado}</h3>'
    voltar = "<a href='/'>Voltar</a>"
    return f'{h1} {h3}<br/> {voltar}'


@app.route('/subtrai')
def subtrai():
    num_1 = 3.0
    num_2 = 5.0
    resultado = subtaction(num_1, num_2)
    h1 = '<h1>Soma olisters</h1>'
    h3 = f'<h3> A diferença de 3-5 é: {resultado}</h3>'
    voltar = "<a href='/'>Voltar</a>"
    return f'{h1} {h3}<br/> {voltar}'


@app.route('/divide')
def divide():
    num_1 = 3.0
    num_2 = 5.0
    resultado = division(num_1, num_2)
    h1 = '<h1>Soma olisters</h1>'
    h3 = f'<h3> A divisão de 3/5 é: {resultado}</h3>'
    voltar = "<a href='/'>Voltar</a>"
    return f'{h1} {h3}<br/> {voltar}'


@app.route('/multiplica')
def multiplica():
    num_1 = 3.0
    num_2 = 5.0
    resultado = multiplication(num_1, num_2)
    h1 = '<h1>Soma olisters</h1>'
    h3 = f'<h3> A multiplicação de 3x5 é: {resultado}</h3>'
    voltar = "<a href='/'>Voltar</a>"
    return f'{h1} {h3}<br/> {voltar}'


app.run(debug=True)
