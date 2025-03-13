from flask import Flask
from extensions import db
from flask_migrate import Migrate


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db' # Configura a URL do banco de dados.
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Desativa o rastreamento de modificações.
app.config['JSON_SORT_KEYS'] = False  # Desativa a ordenação dos campos JSON.

db.init_app(app)  # Inicializa o banco de dados.
migrate = Migrate(app, db)  # Inicializa a migração.

from routes.cliente import cliente_bp                    #IMPORTAÇÃO DAS ROTAS 
from routes.produto import produto_bp                    #IMPORTAÇÃO DAS ROTAS
from routes.pedido import pedido_bp
from routes.item_pedido import item_pedido_bp

app.register_blueprint(cliente_bp,url_prefix='/clientes')         #Blueprint é usado para organizar o codigo em modulos independentes,é registrada no app com um prefixo.
app.register_blueprint(produto_bp,url_prefix='/produtos')
app.register_blueprint(pedido_bp,url_prefix='/pedidos')
app.register_blueprint(item_pedido_bp,url_prefix='/itens_pedido')

if __name__ == '__main__':
    app.run(debug=True)