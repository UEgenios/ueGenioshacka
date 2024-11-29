import csv

file_path = r'utils/execorcamentaria_naturezadespesa_202407.csv'

# lendo o CSV
with open(file_path, 'r', encoding='utf-8') as arquivo_csv:
    leitor_csv = csv.reader(arquivo_csv)
    
    for linha_atual in leitor_csv:  # Itera diretamente sobre o leitor
        print(linha_atual) 




