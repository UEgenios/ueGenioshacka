import pandas as pd
import plotly.express as px
import streamlit as st

################### Anotações temporarias ################################
# rodar a pagina, digitar no terminal "streamlit run main.py"
#
#
#
#
##########################################################################

# funçoes auxiliares (cred eduardo)
def calculate_age(born):
    today = date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

def exclui_outliers(DataFrame, col_name):
  intervalo = 3*DataFrame[col_name].std() ## Fator * Desvio padrão
  media = DataFrame[col_name].mean() ## Média
  DataFrame.loc[DataFrame[col_name] < (media - intervalo), col_name] = np.nan
  DataFrame.loc[DataFrame[col_name] > (media + intervalo), col_name] = np.nan


# configs da pagina
st.set_page_config(layout="wide",page_title="Hacka")
col1, col2 = st.columns(2)
col3, col4 = st.columns(2)

st.sidebar.header('Menu')

# Conteúdo principal
col1.title("Grafico Teste")
col1.markdown("Test")

# lendo arquivo CSV
file_path = 'utils/execorcamentaria_naturezadespesa_202407.csv'
df = pd.read_csv(file_path, sep=';', on_bad_lines='skip')

# limpando os dados
df.dropna(how='all', inplace=True)

# nomes das colunas
colunas = df.columns.tolist()

# colunas em um selectbox
coluna_selecionada = col3.selectbox(
    'Escolha uma coluna para plotar:',
    colunas
)

# gráfico com a coluna selecionada
fig = px.histogram(df, x=coluna_selecionada)
col4.plotly_chart(fig)





