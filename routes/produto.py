from flask import Blueprint, request, jsonify
from models import Produto
from extensions import db

produto_bp = Blueprint('produto', __name__)

@produto_bp.route('/', methods=['GET'])
def get_produtos():
    produtos = Produto.query.all()
    return jsonify([{"id": p.id, "nome": p.nome, "preco": p.preco} for p in produtos])

@produto_bp.route('/', methods=['POST'])
def create_produto():
    data = request.get_json()
    produto = Produto(nome=data['nome'], preco=data['preco'])
    db.session.add(produto)
    db.session.commit()
    return jsonify({"message": "Produto criado com sucesso!"}), 201
