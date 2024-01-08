
#pip install mysql-connector-python

import mysql.connector
from flask import Flask, request, jsonify

app = Flask(__name__)

db_config = {
    'host': 'localhost',
    'user': 'seu_usuario',
    'passwd': 'sua_senha',
    'database': 'nome_do_seu_banco'
}

def init_db():
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS dados (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nome VARCHAR(255),
            email VARCHAR(255),
            deposito FLOAT
        )
    ''')
    conn.commit()
    cursor.close()
    conn.close()

@app.route('/receber-dados', methods=['POST'])
def receber_dados():
    dados_recebidos = request.json

    # Inserir dados no banco de dados MySQL
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO dados (nome, email, deposito) VALUES (%s, %s, %s)
    ''', (dados_recebidos['nome'], dados_recebidos['email'], dados_recebidos['deposito']))
    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({"mensagem": "Dados inseridos com sucesso"}), 200

if __name__ == '__main__':
    init_db()  # Inicializar o banco de dados
    app.run(debug=True, port=5000)
