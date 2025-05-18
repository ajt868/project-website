import yfinance as yf

# Function to get stock data
def get_stock_price(ticker):
    # Get stock data for a specific ticker symbol
    stock = yf.Ticker(ticker)
    
    # Fetch historical market data (you can adjust the period and interval)
    stock_data = stock.history(period="1d", interval="1m")
    
    # Print the most recent stock data
    print(f"Latest stock data for {ticker}:")
    print(stock_data.tail(1))

# Example: Get stock price for Apple (AAPL)
get_stock_price('WWWW')
