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
<<<<<<< HEAD
=======

cidades_denuncias = set(denuncias['cidade'])
cidades_populacao = set(populacao['cidade'])
cidades_precipitacoes = set(precipitacoes['cidade'])
cidades_reservatorios = set(reservatorios['cidade'])

# Interseção de cidades presentes em todos os DataFrames
cidades_comuns = set(cidades_denuncias) | set(cidades_populacao) | set(cidades_precipitacoes) | set(cidades_reservatorios)
>>>>>>> 95507bec00b04ea5a100904814730559cd9e8657

# Verificar as cidades em cada planilha
cidades_denuncias, denuncias_vazia = verificar_cidades(denuncias, 'cidade', 'Denúncias')
cidades_populacao, populacao_vazia = verificar_cidades(populacao, 'cidade', 'População')
cidades_precipitacoes, precipitacoes_vazia = verificar_cidades(precipitacoes, 'cidade', 'Precipitações')
cidades_reservatorios, reservatorios_vazia = verificar_cidades(reservatorios, 'cidade', 'Reservatórios')

cidades_denuncias = set(denuncias['cidade'])
cidades_populacao = set(populacao['cidade'])
cidades_precipitacoes = set(precipitacoes['cidade'])
cidades_reservatorios = set(reservatorios['cidade'])

# Interseção de cidades presentes em todos os DataFrames
cidades_comuns = cidades_denuncias & cidades_populacao & cidades_precipitacoes & cidades_reservatorios

# Sidebar para seleção de cidades
cidade_selecionada = st.sidebar.selectbox(
    "Escolha uma cidade para filtrar:",
    sorted(cidades_comuns)
)

<<<<<<< HEAD

# lendo arquivo CSV
file_path = 'utils/execorcamentaria_naturezadespesa_202407.csv'
df = pd.read_csv(file_path, sep=';', on_bad_lines='skip')

# limpando os dados
df.dropna(how='all', inplace=True)

# nomes das colunas
colunas = df.columns.tolist()

# colunas em um selectbox
coluna_selecionada = st.sidebar.selectbox(
    'Escolha uma coluna para plotar:',
    colunas
)

# gráfico com a coluna selecionada
fig = px.histogram(df, x=coluna_selecionada)
col3.plotly_chart(fig)

=======
# Sidebar para seleção de cidades
cidade_selecionada = st.sidebar.selectbox(
    "Escolha uma cidade para filtrar:",
    sorted(cidades_comuns)
)

>>>>>>> 95507bec00b04ea5a100904814730559cd9e8657




