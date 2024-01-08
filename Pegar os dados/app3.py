from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return 'Home Page'

@app.route('/webhook', methods=['POST', 'GET'])
def webhook():
    if request.method == 'POST':
        data = request.json
        print(data)
        return 'Webhook recebido', 200
    else:
        return 'Webhook aceita apenas método POST', 200


if __name__ == '__main__':
    app.run(debug=True)
