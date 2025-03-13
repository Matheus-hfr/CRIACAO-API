from flask import Blueprint, request, jsonify
from models import Pedido, Cliente
from extensions import db

pedido_bp = Blueprint('pedido', __name__)

@pedido_bp.route('/', methods=['GET'])
def get_pedidos():
    pedidos = Pedido.query.all()
    return jsonify([{"id": p.id, "cliente_id": p.cliente_id, "cliente_nome": p.cliente.nome} for p in pedidos])

@pedido_bp.route('/', methods=['POST'])
def create_pedido():
    data = request.get_json()
    cliente = Cliente.query.get(data['cliente_id'])
    if not cliente:
        return jsonify({"error": "Cliente não encontrado!"}), 404
    pedido = Pedido(cliente_id=data['cliente_id'])
    db.session.add(pedido)
    db.session.commit()
    return jsonify({"message": "Pedido criado com sucesso!"}), 201
