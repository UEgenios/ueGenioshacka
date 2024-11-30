from datetime import datetime

import pandas as pd
import plotly.express as px
import streamlit as st
from sklearn.linear_model import LinearRegression
import util
from importacao_precipitacao import precipitacao
from util import carrega_denuncia, carrega_populacao, carrega_precipitacao, carrega_reservatorios,verificar_cidades

################### Anotações temporarias ################################
# rodar a pagina, digitar no terminal "streamlit run main.py"
#
#
#
#
##########################################################################
denuncias = carrega_denuncia()
populacao = carrega_populacao()
precipitacoes = carrega_precipitacao()
reservatorios = carrega_reservatorios()



# configs da pagina
st.set_page_config(layout="wide",page_title="Hacka")
st.title("Previsão")
st.sidebar.header('Filtros')
col1,cold2 = st.columns(2)
col3, col4 = st.columns(2)

cidades_denuncias = set(denuncias['cidade'])
cidades_populacao = set(populacao['cidade'])
cidades_precipitacoes = set(precipitacoes['cidade'])
cidades_reservatorios = set(reservatorios['cidade'])

# cidades presentes em todos os DataFrames
cidades_comuns = set(set(cidades_denuncias) | set(cidades_populacao) | set(cidades_precipitacoes) | set(cidades_reservatorios))


# seleção de cidades
cidade_selecionada = st.sidebar.selectbox(
    "Escolha uma cidade para filtrar:",
    sorted(cidades_comuns)
)

####### Graficos #######
data_atual = datetime.today()
ano_input = st.sidebar.text_input('Digite o Ano (ex: 2024):', value=str(data_atual.year))
mes_input = st.sidebar.text_input('Digite o Mês (1-12):', value=str(data_atual.month))

try:
    ano_input = int(ano_input)  # Converte para inteiro
except ValueError:
    st.sidebar.error("O ano deve ser um número inteiro.")
    ano_input = None
try:
    mes_input = int(mes_input)  # Converte para inteiro
except ValueError:
    st.sidebar.error("O mês deve ser um número inteiro entre 1 e 12.")
    mes_input = None

# Exibir erro se o ano ou mês não forem válidos
if not validacao_ano:
    st.sidebar.error("O ano ou mês deve ser no futuro!")
# Mostrar a variável que armazena os filtros
if validacao_ano and validacao_mes:
    st.write(f"Filtro aplicado: Ano = {filtro_ano_mes['ano']}, Mês = {filtro_ano_mes['mes']}")

    # Filtrar dados com base no ano e mês digitados
    if filtro_ano_mes['ano'] and filtro_ano_mes['mes']:
        # Filtro por ano e mês
        df_filtrado = df_futuro[(df_futuro['ano'] == filtro_ano_mes['ano']) & (df_futuro['mes'] == filtro_ano_mes['mes'])]
    elif filtro_ano_mes['ano']:
        # Filtro por ano
        df_filtrado = df_futuro[df_futuro['ano'] == filtro_ano_mes['ano']]
    elif filtro_ano_mes['mes']:
        # Filtro por mês (aplica para todos os anos disponíveis)
        df_filtrado = df_futuro[df_futuro['mes'] == filtro_ano_mes['mes']]
    else:
        # Caso não haja filtro, mostrar todos os dados futuros
        df_filtrado = df_futuro

# Armazenar os valores do ano e mês em uma variável para uso posterior
filtro_ano_mes = {'ano': ano_input, 'mes': mes_input}

# Mostrar a variável que armazena os filtros
st.write(f"Filtro aplicado: Ano = {filtro_ano_mes['ano']}, Mês = {filtro_ano_mes['mes']}")



# Exibir os dados filtrados
st.write("Dados filtrados:")
