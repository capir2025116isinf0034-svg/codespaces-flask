from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Olá, mundo! Projeto Flask - Dupla Heitor e Kavanny"

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
