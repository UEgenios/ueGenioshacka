import csv
import pandas as pd

file_path = 'utils/indice_populacional_ibge.csv'

# lendo o CSV
arquivo_csv = pd.read_csv(file_path, sep=";", decimal=",", encoding='ANSI')
    
# for linha_atual in arquivo_csv.iterrows():  # Itera diretamente sobre o leitor
#         print(linha_atual)
print(arquivo_csv)
#escrevendo no arquivo precipitacao
# precipitacao = pd.DataFrame()
# rows_list = []
# for i,linha_atual in agrupado.iterrows():
#     print(linha_atual)
#     dict1 = {'cidade': 'Goiânia', 'ano': linha_atual['ano'], 'mes': linha_atual['mes'], 'dia': linha_atual['dia'], 'data': linha_atual['Data'], 'volume': linha_atual['PRECIPITACAO'], 'data_importacao': '2024/11/29'}
#     rows_list.append(dict1)
# precipitacao = precipitacao._append(pd.DataFrame(rows_list), ignore_index=True)
# precipitacao.to_csv("bd/precipitacao.csv", index=False)




