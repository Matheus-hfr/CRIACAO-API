from flask import Blueprint, request, jsonify
from models import ItemPedido, Pedido, Produto
from extensions import db

item_pedido_bp = Blueprint('item_pedido', __name__)

@item_pedido_bp.route('/', methods=['GET'])
def get_itens_pedido():
    itens = ItemPedido.query.all()
    return jsonify([
        {
            "id": item.id,
            "pedido_id": item.pedido_id,
            "produto_id": item.produto_id,
            "produto_nome": item.produto.nome,
            "quantidade": item.quantidade
        } for item in itens
    ])

@item_pedido_bp.route('/', methods=['POST'])
def create_item_pedido():
    data = request.get_json()
    pedido = Pedido.query.get(data['pedido_id'])
    produto = Produto.query.get(data['produto_id'])
    
    if not pedido:
        return jsonify({"error": "Pedido não encontrado!"}), 404
    if not produto:
        return jsonify({"error": "Produto não encontrado!"}), 404
    
    item_pedido = ItemPedido(
        pedido_id=data['pedido_id'],
        produto_id=data['produto_id'],
        quantidade=data['quantidade']
    )
    db.session.add(item_pedido)
    db.session.commit()
    return jsonify({"message": "Item do pedido criado com sucesso!"}), 201
