import unittest
import pandas as pd
from analyzer.analyzer import analyze_stocks, generate_recommendations

class TestAnalyzer(unittest.TestCase):
    def test_analyze_stocks(self):
        data = pd.DataFrame({
            'Ticker': ['AAPL', 'MSFT'],
            'P/E': [10, 30],
            'P/B': [1, 5],
            'PEG': [0.5, 2.5],
            'ROE': [0.2, 0.1],
            'Deuda/Patrimonio': [0.5, 2.5]
        })
        analyzed_data = analyze_stocks(data)
        self.assertIn('Valoración', analyzed_data.columns)

    def test_generate_recommendations(self):
        data = pd.DataFrame({
            'Ticker': ['AAPL', 'MSFT'],
            'Valoración': ['Infravalorada', 'Sobrevalorada']
        })
        recommendations = generate_recommendations(data)
        self.assertEqual(len(recommendations), 1)

if __name__ == "__main__":
    unittest.main()