from flask import Blueprint

clients_page = Blueprint(
    "client", __name__, static_folder= "client_static", template_folder="client_templates"
)

@clients_page.route("/client")
def client():
    return '<h1>Hello! Welcome to our clients page1</h1>'
