import csv
import random
from datetime import datetime, timedelta

# Dados de cidades e reservatórios em Goiás
reservatorios_goias = [
    {"cidade": "Goiânia", "reservatorio": "Meia Ponte", "volume": 4100},
    {"cidade": "Anápolis", "reservatorio": "Capivari", "volume": 2200},
    {"cidade": "Rio Verde", "reservatorio": "Verdão", "volume": 1500},
    {"cidade": "Itumbiara", "reservatorio": "Itumbiara", "volume": 17000},
    {"cidade": "Catalão", "reservatorio": "Batalha", "volume": 1200},
    {"cidade": "Formosa", "reservatorio": "Descoberto", "volume": 1100},
    {"cidade": "Senador Canedo", "reservatorio": "Samambaia", "volume": 800},
    {"cidade": "Jataí", "reservatorio": "Paranaíba", "volume": 1400},
    {"cidade": "Luziânia", "reservatorio": "Corumbá IV", "volume": 3400},
    {"cidade": "Águas Lindas de Goiás", "reservatorio": "Brasília", "volume": 2900},
]

# Função para gerar uma data aleatória
def gerar_data_aleatoria(ano_inicio, ano_fim):
    inicio = datetime(ano_inicio, 1, 1)
    fim = datetime(ano_fim, 12, 31)
    delta = fim - inicio
    return inicio + timedelta(days=random.randint(0, delta.days))

# Gerar 1000 linhas de dados
linhas = []
for _ in range(1000):
    reservatorio = random.choice(reservatorios_goias)
    cidade = reservatorio["cidade"]
    nome = reservatorio["reservatorio"]
    volume = reservatorio["volume"]
    data = gerar_data_aleatoria(2017, 2024)
    ano = data.year
    mes = data.month
    dia = data.day
    data_formatada = data.strftime("%Y-%m-%d")
    nivel = round(random.uniform(0, 100), 2)  # Nível do reservatório (0-100%)
    data_importacao = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    linhas.append([cidade, ano, mes, dia, data_formatada, nivel, volume, nome, data_importacao])

# Nome do arquivo CSV
arquivo_csv = "reservatorios_goias.csv"

# Escrever os dados no arquivo CSV
with open(arquivo_csv, mode="w", encoding="utf-8", newline="") as arquivo:
    escritor = csv.writer(arquivo)
    escritor.writerow(["cidade", "ano", "mes", "dia", "data", "nivel", "volume", "nome", "data_importacao"])
    escritor.writerows(linhas)

print(f"Arquivo '{arquivo_csv}' gerado com sucesso!")
