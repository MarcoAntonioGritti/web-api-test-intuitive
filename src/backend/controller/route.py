from http import HTTPStatus
from flask import request, jsonify
from src.backend.utils import read_csv
from .blueprint import route_bp
from flask_cors import cross_origin

@route_bp.route('/consultar', methods=['GET'])
@cross_origin() 
def consultar():
    data_param = request.args.get('Data_Registro_ANS')

    df = read_csv()

    # Removendo espaços extras nos valores da coluna Data_Registro_ANS
    if 'Data_Registro_ANS' in df.columns:
        df['Data_Registro_ANS'] = df['Data_Registro_ANS'].str.strip()

    # Filtrar os dados com base no parâmetro "data" (se fornecido)
    if data_param:
        df_filtered = df[df['Data_Registro_ANS'] == data_param]
    else:
        df_filtered = df

    # Verificar se há resultados
    if not df_filtered.empty:
        result = df_filtered.to_dict(orient='records')
        return jsonify(result), HTTPStatus.OK
    else:
        return jsonify({"message": "Nenhum dado encontrado."}), HTTPStatus.NOT_FOUND
