import sys
import os
import logging

# Añadir el directorio raíz del proyecto al path de Python
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from analyzer.data_fetcher import fetch_stock_data
from analyzer.analyzer import analyze_stocks, generate_recommendations

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    # Lista de tickers de empresas
    tickers = ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'TSLA', 'NVDA', 'BRK-B', 'FB', 'V', 'JNJ']

    # Obtener datos de Yahoo Finance
    print("Obteniendo datos de Yahoo Finance...")
    stock_data = fetch_stock_data(tickers)

    if stock_data.empty:
        logging.error("No se pudieron obtener datos de Yahoo Finance.")
        return

    # Mostrar los datos brutos de las empresas
    print("\nDatos brutos de las empresas:")
    print(stock_data)

    # Analizar los datos
    print("\nAnalizando datos...")
    analyzed_data = analyze_stocks(stock_data)

    if analyzed_data is None or analyzed_data.empty:
        logging.error("No se pudieron analizar los datos.")
        return

    # Generar recomendaciones
    print("\nGenerando recomendaciones...")
    recommendations = generate_recommendations(analyzed_data)

    if recommendations.empty:
        print("No se encontraron datos para generar recomendaciones.")
    else:
        # Mostrar todas las acciones con su valoración
        print("\nValoración de las acciones:")
        print(recommendations)

        # Filtrar y mostrar acciones infravaloradas, justamente valoradas y sobrevaloradas
        infravaloradas = recommendations[recommendations['Valoración'] == 'Infravalorada']
        justamente_valoradas = recommendations[recommendations['Valoración'] == 'Justamente Valorada']
        sobrevaloradas = recommendations[recommendations['Valoración'] == 'Sobrevalorada']

        print("\nAcciones infravaloradas:")
        print(infravaloradas if not infravaloradas.empty else "No hay acciones infravaloradas.")

        print("\nAcciones justamente valoradas:")
        print(justamente_valoradas if not justamente_valoradas.empty else "No hay acciones justamente valoradas.")

        print("\nAcciones sobrevaloradas:")
        print(sobrevaloradas if not sobrevaloradas.empty else "No hay acciones sobrevaloradas.")

if __name__ == "__main__":
    main()
