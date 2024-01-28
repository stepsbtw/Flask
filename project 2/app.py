from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Alunos registrados
alunos_lista = [] # quando desligar o server, a variavel some.

@app.route("/") # default get
def index():
    return render_template("index.html")

@app.route("/registrados")
def registrados():
    return render_template("registrado.html", alunos=alunos_lista)

@app.route("/registro", methods=["POST"])
def registro():
    nome = request.form.get("nome") # nao usamos os args, é um post!
    ensino = request.form.get("ensino")
    if not nome or not ensino:
        return render_template("failure.html")
    alunos_lista.append(f"{nome} do {ensino}")
    return redirect("/registrados")