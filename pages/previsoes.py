import pandas as pd
import streamlit as st
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.metrics import f1_score, mean_squared_error, precision_score, recall_score, roc_auc_score, r2_score
from sklearn.model_selection import train_test_split
from util import carrega_denuncia, carrega_populacao, carrega_precipitacao, carrega_reservatorios


st.title("Previsões")

denuncias = carrega_denuncia()
populacao = carrega_populacao()
precipitacoes = carrega_precipitacao()
reservatorios = carrega_reservatorios()


# configs da pagina

st.sidebar.header('Filtros')
col1,cold2 = st.columns(2)
col3, col4 = st.columns(2)

####### filtros #######
## Cidades ##
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
## Mes ou ano futuros ##
#data_atual = datetime.today()
#ano_input = st.sidebar.text_input('Digite o Ano (ex: 2024):', value=str(data_atual.year))
#mes_input = st.sidebar.text_input('Digite o Mês (1-12):', value=str(data_atual.month))

#try:
#    ano_input = int(ano_input)  # Converte para inteiro
#except ValueError:
#    st.sidebar.error("O ano deve ser um número inteiro.")
 #   ano_input = None
#try:
#    mes_input = int(mes_input)  # Converte para inteiro
#except ValueError:
#    st.sidebar.error("O mês deve ser um número inteiro entre 1 e 12.")
#    mes_input = None
# Armazenar os valores do ano e mês
#filtro_ano_mes = {'ano': ano_input, 'mes': mes_input}

####### Informações #######

dados_completos = pd.merge(reservatorios, precipitacoes, on=['cidade'], how='inner')
dados_completos = pd.merge(dados_completos, populacao, on=['cidade'], how='inner')
dados_filtrados = dados_completos[(dados_completos['cidade'] == cidade_selecionada)]

if dados_filtrados.shape[0] == 0:
    st.warning(f"Não há dados disponíveis para a cidade '{cidade_selecionada}'.")
else:
    X = dados_filtrados[['volume_x', 'quantidade', 'ano']]
    y = dados_filtrados['nivel']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    model = LinearRegression()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    st.write("Após a execução do modelo de regressão linear para prever o nível de um reservatório com base em variáveis como o volume de água, a quantidade de precipitação e a população de uma cidade, o sistema apresenta os seguintes resultados:")
    st.write(f"Erro quadrático médio: {mse:.2f}")
    st.write(f"R2 Score: {r2:.2f}")
    dados_filtrados['previsao_nivel'] = model.predict(X)
    st.write(dados_filtrados[['cidade', 'ano', 'nivel', 'previsao_nivel']])