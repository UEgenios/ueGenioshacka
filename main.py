import pandas as pd
import plotly.express as px
import streamlit as st
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
st.title("Grafico Teste")
st.sidebar.header('Filtros')
col1,cold2 = st.columns(2)
col3, col4 = st.columns(2)

cidades_denuncias = set(denuncias['cidade'])
cidades_populacao = set(populacao['cidade'])
cidades_precipitacoes = set(precipitacoes['cidade'])
cidades_reservatorios = set(reservatorios['cidade'])

# Interseção de cidades presentes em todos os DataFrames
cidades_comuns = set(cidades_denuncias) | set(cidades_populacao) | set(cidades_precipitacoes) | set(cidades_reservatorios)


# Sidebar para seleção de cidades
cidade_selecionada = st.sidebar.selectbox(
    "Escolha uma cidade para filtrar:",
    sorted(cidades_comuns)
)





