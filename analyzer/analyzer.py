import pandas as pd
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def analyze_stocks(stock_data):
    """
    Analiza los datos de las acciones y asigna una valoración.
    :param stock_data: DataFrame con los datos de las acciones.
    :return: DataFrame con la valoración.
    """
    if stock_data.empty:
        logging.warning("El DataFrame de entrada está vacío.")
        return None

    analyzed_data = stock_data.copy()

    # Regla de valoración ponderada
    def valuation_rule(row):
        # Convertir valores a numéricos, si no son válidos, usar NaN
        pe = pd.to_numeric(row['P/E'], errors='coerce')
        pb = pd.to_numeric(row['P/B'], errors='coerce')
        peg = pd.to_numeric(row['PEG'], errors='coerce')
        roe = pd.to_numeric(row['ROE'], errors='coerce')
        debt_equity = pd.to_numeric(row['Deuda/Patrimonio'], errors='coerce')

        # Calcular una puntuación basada en las métricas disponibles
        score = 0
        total_metrics = 0

        if not pd.isna(pe):
            if pe < 15:
                score += 1
            elif pe > 25:
                score -= 1
            total_metrics += 1

        if not pd.isna(pb):
            if pb < 2:
                score += 1
            elif pb > 5:
                score -= 1
            total_metrics += 1

        if not pd.isna(peg):
            if peg < 1:
                score += 1
            elif peg > 2:
                score -= 1
            total_metrics += 1

        if not pd.isna(roe):
            if roe > 0.15:
                score += 1
            elif roe < 0.10:
                score -= 1
            total_metrics += 1

        if not pd.isna(debt_equity):
            if debt_equity < 1:
                score += 1
            elif debt_equity > 2:
                score -= 1
            total_metrics += 1

        # Determinar la valoración basada en la puntuación
        if total_metrics == 0:
            return 'N/A'  # No hay métricas disponibles

        if score / total_metrics > 0.5:
            return 'Infravalorada'
        elif score / total_metrics < -0.5:
            return 'Sobrevalorada'
        else:
            return 'Justamente Valorada'

    # Aplicar la regla de valoración
    analyzed_data['Valoración'] = analyzed_data.apply(valuation_rule, axis=1)
    return analyzed_data

def generate_recommendations(analyzed_data):
    """
    Genera recomendaciones de compra basadas en la valoración.
    :param analyzed_data: DataFrame con los datos analizados.
    :return: DataFrame con todas las acciones y su valoración.
    """
    if analyzed_data is None or analyzed_data.empty:
        logging.warning("No hay datos analizados para generar recomendaciones.")
        return pd.DataFrame()  # Devuelve un DataFrame vacío

    if 'Valoración' not in analyzed_data.columns:
        logging.warning("La columna 'Valoración' no existe en el DataFrame.")
        return pd.DataFrame()  # Devuelve un DataFrame vacío

    # Devolver todas las acciones con su valoración
    return analyzed_data[['Ticker', 'Nombre', 'Precio Actual', 'P/B', 'P/E', 'PEG', 'ROE', 'Deuda/Patrimonio', 'Sector', 'Industria', 'Valoración']]