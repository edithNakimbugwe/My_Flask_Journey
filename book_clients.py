# clients.py
from flask import Blueprint, jsonify

clients = Blueprint(
    "clients", __name__, static_folder="client_static", template_folder="client_templates"
)

clients_list = [
    {"id": 1, "name": "Edith Nak", "email": "edithnak@gmail.com"},
    {"id": 2, "name": "Shaniqua De", "email": "shaniquade@gmail.com"},
]

@clients.route('/', methods=['GET'])
def handle_clients():
    return jsonify(clients_list)

@clients.route('/<int:id>', methods=['GET'])
def client_detail(id):
    for client in clients_list:
        if client['id'] == id:
            return jsonify(client)
    return jsonify({"error": "Client not found"})

