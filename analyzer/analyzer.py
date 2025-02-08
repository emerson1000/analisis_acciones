import pandas as pd

def analyze_stocks(stock_data):
    """
    Analiza los datos de las acciones y asigna una valoración.
    :param stock_data: DataFrame con los datos de las acciones.
    :return: DataFrame con la valoración.
    """
    analyzed_data = stock_data.copy()

    # Reglas de valoración
    def valuation_rule(row):
        pe = row['P/E']
        pb = row['P/B']
        peg = row['PEG']
        roe = row['ROE']
        debt_equity = row['Deuda/Patrimonio']

        if pd.isna(pe) or pd.isna(pb) or pd.isna(peg):
            return 'N/A'

        if pe < 15 and pb < 2 and peg < 1 and roe > 0.15 and debt_equity < 1:
            return 'Infravalorada'
        elif pe > 25 or pb > 5 or peg > 2 or debt_equity > 2:
            return 'Sobrevalorada'
        else:
            return 'Justamente Valorada'

    analyzed_data['Valoración'] = analyzed_data.apply(valuation_rule, axis=1)
    return analyzed_data

def generate_recommendations(analyzed_data):
    """
    Genera recomendaciones de compra basadas en la valoración.
    :param analyzed_data: DataFrame con los datos analizados.
    :return: DataFrame con las recomendaciones.
    """
    return analyzed_data[analyzed_data['Valoración'] == 'Infravalorada']