from datetime import date


def calculate_age(born):
    today = date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

def exclui_outliers(DataFrame, col_name):
  intervalo = 3*DataFrame[col_name].std() ## Fator * Desvio padrão
  media = DataFrame[col_name].mean() ## Média
  DataFrame.loc[DataFrame[col_name] < (media - intervalo), col_name] = np.nan
  DataFrame.loc[DataFrame[col_name] > (media + intervalo), col_name] = np.nan

