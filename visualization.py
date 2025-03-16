import plotly.graph_objects as go
import pandas as pd

class Visualization:
    """Handles interactive visualizations for stock analysis"""

    @staticmethod
    def plot_stock_data(data: pd.DataFrame, ticker: str):
        """Generate a candlestick chart for stock prices"""
        fig = go.Figure()

        fig.add_trace(go.Candlestick(
            x=data.index,
            open=data["Open"],
            high=data["High"],
            low=data["Low"],
            close=data["Close"],
            name="Candlestick"
        ))

        fig.update_layout(
            title=f"{ticker} Stock Price Analysis",
            xaxis_title="Date",
            yaxis_title="Stock Price (USD)",
            template="plotly_dark"
        )

        fig.show()

    @staticmethod
    def plot_stock_volume(data: pd.DataFrame, ticker: str):
        """Generate a bar chart for stock trading volume"""
        fig = go.Figure()

        fig.add_trace(go.Bar(
            x=data.index,
            y=data["Volume"],
            name="Volume",
            marker_color="blue"
        ))

        fig.update_layout(
            title=f"{ticker} Trading Volume",
            xaxis_title="Date",
            yaxis_title="Volume",
            template="plotly_dark"
        )

        fig.show()
