from flask import Flask, request, jsonify

app = Flask(__name__)

# Criar um dicionário com os dados iniciais
data = {
    1: {'name': 'John Doe', 'age': 30},
    2: {'name': 'Jane Smith', 'age': 25}
}

# Rota para criar um novo registro
@app.route('/api/create', methods=['POST'])
def create():
    # Obtém os dados do corpo da requisição
    new_data = request.get_json()
    # Gera um novo ID
    new_id = max(data.keys()) + 1
    # Adiciona os dados ao dicionário
    data[new_id] = new_data
    # Retorna o ID gerado como resposta
    return jsonify({'id': new_id})

# Rota para ler um registro
@app.route('/api/read/<int:id>', methods=['GET'])
def read(id):
    # Verifica se o ID existe no dicionário
    if id in data:
        return jsonify(data[id])
    else:
        return jsonify({'error': 'Registro não encontrado'})

# Rota para atualizar um registro
@app.route('/api/update/<int:id>', methods=['PUT'])
def update(id):
    # Obtém os dados do corpo da requisição
    update_data = request.get_json()
    # Verifica se o ID existe no dicionário
    if id in data:
        # Atualiza os dados no dicionário
        data[id].update(update_data)
        return jsonify({'status': 'Registro atualizado'})
    else:
        return jsonify({'error': 'Registro não encontrado'})

# Rota para deletar um registro
@app.route('/api/delete/<int:id>', methods=['DELETE'])
def delete(id):
    # Verifica se o ID existe no dicionário
    if id in data:
        # Deleta o registro do dicionário
        del data[id]
        return jsonify({'status': 'Registro deletado'})
    else:
        return jsonify({'error': 'Registro não encontrado'})

if __name__ == '__main__':
    app.run(debug=True)
