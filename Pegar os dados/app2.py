from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/receber-dados', methods=['POST'])
def receber_dados():
    # Obtém os dados do corpo da requisição
    dados_recebidos = request.json
    print("Dados Recebidos:", dados_recebidos)

    # Processa os dados (aqui você pode adicionar o código para processar ou armazenar os dados)
    # ...

    # Retorna uma resposta
    return jsonify({"mensagem": "Dados recebidos com sucesso"}), 200

if __name__ == '__main__':
    app.run(debug=True, port=5000)
