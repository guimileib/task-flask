from flask import Flask 

app = Flask(__name__)
# Criando rota -> receber e devolver informações
@app.route("/")
def hello_world():
    return "Hello World!"

@app.route("/about")
def about():
    return "Página sobre"

if __name__ == "__main__":
    app.run(debug=True) 
