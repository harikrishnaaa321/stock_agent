from agents.stock_agent import StockAnalysisAgent

def main():
    print("📈 Welcome to the AI Stock Market Analysis Agent 📈")
    ticker = input("Enter a stock ticker (e.g., AAPL, TSLA, GOOGL): ").upper()
    try:
        agent = StockAnalysisAgent()
        result = agent.analyze_stock(ticker)
        print(result)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()

