from flask import Blueprint, request, jsonify,Response
from models import Cliente
from extensions import db
from collections import OrderedDict
import json


cliente_bp = Blueprint('cliente', __name__)

@cliente_bp.route('/', methods=['GET'])
def get_clientes():
    clientes = Cliente.query.order_by(Cliente.nome).all() #consulta a tabela Cliente e ordena pelo campo nome e retorna todos os registros
    response = [
        OrderedDict([       #cria um dicionario ordenado
            ("id", c.id),              #Para cada elemento da lista, o Python atribui o elemento atual à variável c.
            ("nome", c.nome),          #O dicionário é criado com os campos id, nome, endereco, numero, complemento, bairro, cep, cidade e estado.
            ("endereco", c.endereco),
            ("numero", c.numero),
            ("complemento", c.complemento),
            ("bairro", c.bairro),
            ("cep", c.cep),
            ("cidade", c.cidade),
            ("estado", c.estado)
        ])
        for c in clientes
    ]
    return Response(json.dumps(response, ensure_ascii=False), mimetype='application/json') #Transforma a lista em um JSON, e retorna a resposta com o tipo de conteúdo application/json.

@cliente_bp.route('/', methods=['POST'])
def create_cliente():
    data = request.get_json() #Converte o Body da requisição em um dicionário Python.
    cliente = Cliente(
        nome = data['nome'],
        endereco = data['endereco'],
        numero = data['numero'],
        complemento = data['complemento'],
        bairro = data['bairro'],
        cep = data['cep'],
        cidade = data['cidade'],
        estado = data['estado'])
    db.session.add(cliente)  
    db.session.commit()
    return jsonify({"message": "Cliente criado com sucesso!"}),201
                    