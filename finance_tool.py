import yfinance as yf
import pandas as pd

class FinanceTool:
    """Tool to fetch stock market data using yfinance"""

    @staticmethod
    def get_stock_data(ticker: str, period="6mo"):
        """Fetch historical stock data"""
        stock = yf.Ticker(ticker)
        data = stock.history(period=period)
        
        if data.empty:
            raise ValueError("Invalid stock ticker or no data available.")
        
        return data

    @staticmethod
    def get_current_price(ticker: str):
        """Fetch the current stock price"""
        stock = yf.Ticker(ticker)
        return stock.history(period="1d")["Close"].iloc[-1]

