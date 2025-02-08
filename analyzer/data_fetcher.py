import yfinance as yf
import pandas as pd

def fetch_stock_data(tickers):
    """
    Obtiene los datos fundamentales de las acciones desde Yahoo Finance.
    :param tickers: Lista de tickers de empresas.
    :return: DataFrame con los datos.
    """
    data = []

    for ticker in tickers:
        try:
            stock = yf.Ticker(ticker)
            info = stock.info

            # Extraer métricas clave
            stock_data = {
                'Ticker': ticker,
                'Nombre': info.get('shortName', 'N/A'),
                'Precio Actual': info.get('currentPrice', 'N/A'),
                'P/B': info.get('priceToBook', 'N/A'),
                'P/E': info.get('trailingPE', 'N/A'),
                'PEG': info.get('pegRatio', 'N/A'),
                'ROE': info.get('returnOnEquity', 'N/A'),
                'Deuda/Patrimonio': info.get('debtToEquity', 'N/A'),
                'Margen Beneficio': info.get('profitMargins', 'N/A'),
                'Div Yield': info.get('dividendYield', 'N/A'),
                'Sector': info.get('sector', 'N/A'),
                'Industria': info.get('industry', 'N/A')
            }
            data.append(stock_data)
        except Exception as e:
            print(f"Error obteniendo datos de {ticker}: {e}")

    return pd.DataFrame(data)