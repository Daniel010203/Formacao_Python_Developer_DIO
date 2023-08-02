from flask import Flask, jsonify, requests, json

app = Flask(__name__)

@app.route('/<int:id>')
def pessoa(id):
    return jsonify({
        'id':id,
        'nome':'Raphael',
        'profissao':'Desenvolvedor'
        })

# @app.route('/soma/<int:valor1>/<int:valor2>')
# def soma(valor1, valor2):
#     return jsonify('soma': valor1 + valor2)

@app.route('/soma', methods=['POST', 'GET'])
def soma():
    if requests.method == 'POST':
        dados = json.loads(requests.data)
        total = sum(dados['valores'])
    elif requests.method == 'GET':
        total = 10 + 10
    return jsonify({'soma':total})

if __name__=="__main__":
    app.run(debug=True)