from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)


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
    
    # salvando os registros em um csv
    file = open("registrado.csv", "a") # "a" -> append uma linha
    writer = csv.writer(file)
    writer.writerow((request.form.get("nome"), request.form.get("ensino")))
    file.close()

    return redirect("/registrados")