from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>Hello World!</h1>'


@app.route('/usuario', methods=['GET'])
def buscar_usuario():
    usuario = {'usuario': "Ruby",
               "idade": 16,
               "telefono": "(19) 999956567"
    }
    return usuario

@app.route('/produto', methods=['POST'])
def cadastrar_produto():
    dados = request.get_json()

    if not(dados):
        return jsonify({"erro": "Dados inválidos"}), 400

    print(f'Novo produto: {dados}')

    return jsonify(
        {
            "message": "Produto salvo com sucesso!",
            "produto_cadastrado": dados
        }
    ), 201

@app.route('/produto', methods=['PUT'])
def atualizar_produtos():
    produto = {
        "id": 1,
        "nome": "Caneta azul",
        "preco": 1.5,
        "descricao": "Caneta esferográfica",
        "marca": "Bic"
    }

    dados = request.get_json()

    if not dados:
        return jsonify({"erro": "Dados inváidos"}), 400

    if dados['id'] == produto['id']:
        produto = dados

        print(f'Novo produto: {produto}')

        return jsonify({'message': 'Produto salvo!'}), 201
    else:
        return jsonify({'message': 'Produto não encontrado!'}), 404


if __name__ == '__main__':
 app.run(debug=True)