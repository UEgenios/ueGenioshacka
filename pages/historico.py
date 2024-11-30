from datetime import datetime
import pandas as pd
import streamlit as st
import plotly.express as px
from util import carrega_denuncia, carrega_populacao, carrega_precipitacao, carrega_reservatorios

st.title("Historico")

denuncias = carrega_denuncia()
populacao = carrega_populacao()
precipitacoes = carrega_precipitacao()
reservatorios = carrega_reservatorios()


###### Informações ######
st.write("Variação do Nível de reservatorios")
reservatorios['data'] = pd.to_datetime(reservatorios['data'])
reservatorios['ano_mes'] = reservatorios['data'].dt.to_period('M').astype(str)  # Converter para string

cidades = reservatorios['cidade'].unique()
cidades_selecionadas = st.multiselect("Escolha as cidades:", cidades, default=cidades[:1])
dados_filtrados = reservatorios[reservatorios['cidade'].isin(cidades_selecionadas)]

fig = px.bar(dados_filtrados, x='ano_mes', y='nivel', color='cidade',
             title='Nível do Reservatório por Cidade e Mês',
             labels={'ano_mes': 'Ano-Mês', 'nivel': 'Nível do Reservatório'},
             barmode='group')
st.plotly_chart(fig)

st.write("Quantidade de Denúncias vs. Nível do Reservatório")
denuncias['data'] = pd.to_datetime(denuncias['data'])
merged_denuncia_reserv = pd.merge(reservatorios, denuncias, on=['cidade', 'ano', 'mes'], how='inner')

fig = px.bar(merged_denuncia_reserv, x='nivel', y='quantidade', color='cidade',
                 title='Quantidade de Denúncias vs Nível do Reservatório',
                 labels={'nivel': 'Nível do Reservatório', 'quantidade': 'Quantidade de Denúncias'},
                 hover_data=['cidade', 'ano', 'mes'])

st.plotly_chart(fig)