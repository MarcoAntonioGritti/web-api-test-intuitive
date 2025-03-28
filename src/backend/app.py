import os
from flask import Flask, jsonify,json
from werkzeug.exceptions import HTTPException
from src.backend.execeptions import CustomErrorException
from flask_cors import CORS

cors = CORS()

def create_app():

    # Criação e configuração simples da aplicação
    app = Flask(__name__)
    cors.init_app(app)

    # registra blueprint
    from src.backend.controller.blueprint import route_bp
    app.register_blueprint(route_bp)


    @app.errorhandler(HTTPException)
    def handle_exception(e):
        """Return JSON instead of HTML for HTTP errors."""
        # Verifica se a exceção é uma CustomErrorException
        if isinstance(e, CustomErrorException):
            # Se for, retorna a mensagem personalizada e o código de status fornecido
            response = jsonify({"message": e.message})
            response.status_code = e.code
        else:
            # Se não for, mantém a resposta padrão
            response = e.get_response()
            # Substitui o corpo com o formato JSON padrão para a exceção
            response.data = json.dumps(
                {
                    "code": e.code,
                    "name": e.name,
                    "description": e.description,
                }
            )
            response.content_type = "application/json"

        return response

    return app