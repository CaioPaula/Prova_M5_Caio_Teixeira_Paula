from flask import Flask, render_template, jsonify, request, redirect
from tinydb import TinyDB, Query

db = TinyDB("caminhos.json")

server = Flask(__name__)


@server.route("/")
def main():
    return (
        """
        <ul>
            <li><a href="/novo_form">Novo caminho</a></li>
            <li><a href="/pegar_caminho_form">Pegar caminho</a></li>
            <li><a href="/listas_caminhos">Lista de caminhos</a></li>
            <li><a href="/atualizar">Atualiza caminho</a></li>
            <li><a href="/deletar">Deletar caminho</a></li>
        </ul>
"""
)

@server.route('/novo_form')
def rout_form():
    return render_template("novo.html")


@server.route("/novo", methods=["POST"])
def reg_rowt():
    name = str(request.form.get("name"))
    x = float(request.form.get('x'))
    y = float(request.form.get('y'))
    z = float(request.form.get('z'))
    r = float(request.form.get('r'))
    

    db.insert({"name":name, "x":x, "y":y, "z":z, "r":r})

    return redirect("/")

@server.route('/pegar_caminho_form')
def get_routes():
    return render_template("get-route.html")


@server.route('/pegar_caminho', methods=["POST"])
def get_route():
    name = str(request.form.get("name"))
    Route = Query()

    route = db.search(Route.name == name)[0]
    print(route)

    return f' Nome Posicao : {route["name"]}<br>X:{route['x']}<br>Y:{route['y']}<br>Z:{route['z']}<br>R:{route['r']}<br><a href="/">Voltar</a>'



@server.route('/listas_caminhos')
def get_all_routes():
    routes_list_on_db = db.all()
    routes_list = ""

    for route in routes_list_on_db:
        routes_list += (f"<li>Caminho : {route["name"]}<li>")

    return f"<ul>{routes_list}</ul>"



if __name__ == "__main__":
    server.run()