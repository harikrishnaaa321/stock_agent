import requests
from tools.finance_tool import FinanceTool
from tools.visualization import Visualization

class StockAnalysisAgent:
    """AI Agent for analyzing stock trends using a lightweight GPT-2 model"""

    def __init__(self, model_name="gpt2"):
        self.api_url = f"https://api-inference.huggingface.co/models/{model_name}"
        self.api_key = os.getenv("HUGGINGFACE_TOKEN")


        if not self.api_key:
            raise ValueError("Error: Hugging Face API key is missing!")

        self.headers = {"Authorization": f"Bearer {self.api_key}"}

    def analyze_stock(self, ticker: str):
        """Fetch stock data, visualize trends, and generate AI insights."""

        # Fetch stock data
        stock_data = FinanceTool.get_stock_data(ticker)
        current_price = FinanceTool.get_current_price(ticker)

        # Generate visualizations
        Visualization.plot_stock_data(stock_data, ticker)
        Visualization.plot_stock_volume(stock_data, ticker)

        # AI-powered stock analysis
        prompt = f"Predict the stock trend for {ticker} in the next few weeks."

        try:
            response = requests.post(self.api_url, headers=self.headers, json={"inputs": prompt})
            response.raise_for_status()  # Handle HTTP errors
            result = response.json()

            # Extract AI analysis safely
            ai_analysis = result[0].get("generated_text", "No analysis available.")

            return f" **Stock Analysis for {ticker}**\n\n **Current Price:** ${current_price:.2f}\n\n **AI Analysis:**\n{ai_analysis}"

        except requests.exceptions.RequestException as e:
            return f" API Error: {e}"

        except (KeyError, IndexError):
            return " Error: Unexpected API response format."

# Example usage:
# agent = StockAnalysisAgent()
# print(agent.analyze_stock("AAPL"))
