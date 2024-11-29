import csv
import pandas as pd

file_path = 'utils/INMET_CO_GO_A002_GOIANIA_01-01-2024_A_31-10-2024.csv'

# lendo o CSV
arquivo_csv = pd.read_csv(file_path, sep=";", decimal=",", encoding='ANSI')
agrupado = arquivo_csv.groupby("Data")["PRECIPITACAO"].sum().reset_index()
agrupado['Data'] = pd.to_datetime(agrupado['Data'], format='%Y/%m/%d')
# print(arquivo_csv.dtypes)
agrupado["mes"] = agrupado["Data"].dt.month
agrupado["ano"] = pd.to_numeric(agrupado["Data"].dt.year)
agrupado["dia"] = pd.to_numeric(agrupado["Data"].dt.day)
    
# for linha_atual in arquivo_csv.iterrows():  # Itera diretamente sobre o leitor
#         print(linha_atual)
print(agrupado)
#escrevendo no arquivo precipitacao
precipitacao = pd.DataFrame()
rows_list = []
for i,linha_atual in agrupado.iterrows():
    print(linha_atual)
    dict1 = {'cidade': 'Goiânia', 'ano': linha_atual['ano'], 'mes': linha_atual['mes'], 'dia': linha_atual['dia'], 'data': linha_atual['Data'], 'volume': linha_atual['PRECIPITACAO'], 'data_importacao': '2024/11/29'}
    rows_list.append(dict1)
precipitacao = precipitacao._append(pd.DataFrame(rows_list), ignore_index=True)
precipitacao.to_csv("bd/precipitacao.csv", index=False)




