import yfinance as yf
import pandas as pd

def download_and_format_stock_data(ticker, start_date, end_date):
    """
    Downloads and formats stock price data from Yahoo Finance.

    Parameters:
        ticker (str): Stock ticker symbol (e.g., 'TSLA' for Tesla).
        start_date (str): Start date in 'YYYY-MM-DD' format.
        end_date (str): End date in 'YYYY-MM-DD' format.

    Returns:
        pd.DataFrame: DataFrame containing the formatted stock price data.
    """
    try:
        # Fetch the stock data
        stock_data = yf.download(ticker, start=start_date, end=end_date)
        
        if stock_data.empty:
            print(f"No data found for ticker: {ticker}")
            return None

        # Reset index to get 'Date' from index
        stock_data.reset_index(inplace=True)

        # Select and rename the required columns
        stock_data = stock_data[['Date', 'Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']]

        # Rename columns as per your specified format
        stock_data.rename(columns={
            'Adj Close': 'MarketClose',
            'Open': 'MarketOpen'
        }, inplace=True)

        # Add 'Ticker' column
        stock_data['Ticker'] = ticker

        # Reorder columns
        stock_data = stock_data[['Ticker', 'Date', 'MarketClose', 'Volume', 'MarketOpen', 'High', 'Low']]

        # Format the prices with $ sign and two decimal places
        price_columns = ['MarketClose', 'MarketOpen', 'High', 'Low']
        stock_data[price_columns] = stock_data[price_columns].applymap(lambda x: f"${x:,.2f}")

        # Format the 'Date' as 'MM/DD/YYYY'
        stock_data['Date'] = stock_data['Date'].dt.strftime('%m/%d/%Y')

        return stock_data

    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Example usage
if __name__ == "__main__":
    
    start_date = "2000-01-01"
    end_date = "2024-11-18"  # Current date
        
    tickers = ["NVDA", "AAPL", "TSLA"]  # List of ticker symbols
    for ticker in tickers:
        data = download_and_format_stock_data(ticker, start_date, end_date)
        if data is not None:
            print(f"Data for {ticker}:")
            print(data.head())
            data.to_csv(f"{ticker}_formatted_stock_data.csv", index=False)