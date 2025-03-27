from http import HTTPStatus
from flask import request, jsonify
from src.backend.utils import read_csv
from .blueprint import route_bp

@route_bp.route('/consultar', methods=['GET'])
def consultar():
    # Parâmetro de consulta enviado pelo front-end (por exemplo, um parâmetro "data")
    data_param = request.args.get('DATA')

    # Ler o arquivo CSV
    df = read_csv()

    # Filtrar os dados com base no parâmetro "data" (se fornecido)
    if data_param:
        # Filtrando por data
        df_filtered = df[df['DATA'] == data_param]
    else:
        df_filtered = df

    # Verificar se há resultados
    if not df_filtered.empty:
        # Converter o DataFrame filtrado para uma lista de dicionários
        result = df_filtered.to_dict(orient='records')
        return jsonify(result), HTTPStatus.OK
    else:
        return jsonify({"message": "Nenhum dado encontrado."}), HTTPStatus.NOT_FOUND