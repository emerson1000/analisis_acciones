from analyzer.data_fetcher import fetch_stock_data
from analyzer.analyzer import analyze_stocks, generate_recommendations

def main():
    # Lista de tickers de empresas
    tickers = ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'TSLA', 'NVDA', 'BRK-B', 'FB', 'V', 'JNJ']

    # Obtener datos de Yahoo Finance
    print("Obteniendo datos de Yahoo Finance...")
    stock_data = fetch_stock_data(tickers)

    # Analizar los datos
    print("Analizando datos...")
    analyzed_data = analyze_stocks(stock_data)

    # Generar recomendaciones
    print("Generando recomendaciones...")
    recommendations = generate_recommendations(analyzed_data)

    # Mostrar resultados
    print("\nRecomendaciones de inversión:")
    print(recommendations)

if __name__ == "__main__":
    main()