import pandas as pd

file_path = 'utils/indice_populacional_ibge.csv'

# lendo o CSV
arquivo_csv = pd.read_csv(file_path, sep=",", decimal=".", encoding='ANSI')

print(arquivo_csv)
#escrevendo no arquivo precipitacao
populacao = pd.DataFrame()
rows_list = []
for i,linha_atual in arquivo_csv.iterrows():
    dict1 = {'cidade': linha_atual['Município'], 'ano': '2022', 'quantidade': linha_atual['Populacao2022'], 'data_importacao': '2024/11/29'}
    rows_list.append(dict1)
populacao = populacao._append(pd.DataFrame(rows_list), ignore_index=True)
populacao.to_csv("bd/populacao.csv", index=False)




