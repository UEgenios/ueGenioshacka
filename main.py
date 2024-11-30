from datetime import datetime
import pandas as pd
import streamlit as st
from util import carrega_denuncia, carrega_populacao, carrega_precipitacao, carrega_reservatorios

################### Anotações temporarias ################################
# rodar a pagina, digitar no terminal "streamlit run main.py"
#
#
#
#
##########################################################################

st.set_page_config(layout="wide",page_title="Hacka")
st.title("EcoVision")

st.write("Equipe")
st.write("Cleverson Parreira Júnior")
st.write("Eduardo de Faria Souza")
st.write("Johnathan Rafael Pereira")
st.write("Lilian Reis Barbosa Parreira")
st.write("Yuri Barbosa Pires")
st.write()
st.write()
st.write()
st.write()


