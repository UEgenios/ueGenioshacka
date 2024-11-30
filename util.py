from datetime import date
import streamlit as st
import pandas as pd


def calculate_age(born):
    today = date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

def exclui_outliers(DataFrame, col_name):
  intervalo = 3*DataFrame[col_name].std() ## Fator * Desvio padrão
  media = DataFrame[col_name].mean() ## Média
  DataFrame.loc[DataFrame[col_name] < (media - intervalo), col_name] = np.nan
  DataFrame.loc[DataFrame[col_name] > (media + intervalo), col_name] = np.nan

def carrega_precipitacao():
    precipitacao = pd.read_csv("bd/precipitacao.csv", sep=",", decimal=".")
    return precipitacao

def carrega_denuncia():
    denuncias = pd.read_csv("bd/denuncias.csv", sep=",", decimal=".")
    return denuncias

def carrega_populacao():
    populacao = pd.read_csv("bd/populacao.csv", sep=",", decimal=".")
    return populacao

def carrega_reservatorios():
    reservatorios = pd.read_csv("bd/populacao.csv", sep=",", decimal=".")
    return reservatorios

def verificar_cidades(df, coluna_cidade, nome_planilha):
    if not df.empty:
        return set(df[coluna_cidade]), False
    else:
        st.warning(f"A planilha '{nome_planilha}' está vazia.")
        return set(), True