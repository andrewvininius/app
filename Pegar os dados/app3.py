from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/')
def home():
    return 'Home Page'

@app.route('/webhook', methods=['POST', 'GET'])
def webhook():
    if request.method == 'POST':
        data = request.json
        print(data)

        # Salvar em um arquivo (anexar a um arquivo existente ou criar um novo).
        with open('depositos.json', 'a') as file:
            file.write(json.dumps(data) + '\n')

        return 'Webhook recebido', 200
    else:
        return 'Webhook aceita apenas método POST', 200

if __name__ == '__main__':
    app.run(debug=True)

#$body = @{chave="valor"} | ConvertTo-Json
#Invoke-WebRequest -Uri http://127.0.0.1:5000/webhook -Method POST -ContentType "application/json" -Body $body -UseBasicParsing
