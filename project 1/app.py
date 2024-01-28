from flask import Flask, render_template, request

app = Flask(__name__) # turn this file into an web application 

@app.route("/") # listen to get request on "/"
def index():
    nome_ = request.args.get("nome", "world") # trying to get an argument called "NAME" in the request
    return render_template("index.html", nome=nome_) # render_template has various parameters such as name


