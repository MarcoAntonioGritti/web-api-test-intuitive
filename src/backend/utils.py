import pandas as pd
import os

def read_csv():
    # Caminho relativo para o arquivo CSV na pasta 'data'
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # Vai para o diretório raiz do projeto
    csv_path = os.path.join(base_dir, 'backend','data','Relatorio_cadop.csv')  # Caminho para o arquivo CSV
    # Leia o arquivo CSV com pandas
    df = pd.read_csv(csv_path, sep=';', engine='python')
    return df