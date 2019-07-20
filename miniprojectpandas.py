# We import pandas into Python
import pandas as pd

# We read in a stock data data file into a data frame and see what it looks like
goog_data = pd.read_csv("GOOG.csv")

# We display the first 5 rows of the DataFrame
print(goog_data.head(5))

# We load the Google stock data into a DataFrame
google_stock = pd.read_csv("GOOG.csv", index_col="Date", parse_dates=True, usecols=['Date','Adj Close'])
print("\nGOOG.csv dataframe first 5 lines using Date as row index and Adj Close as column:\n",google_stock.head(5))
# We load the Apple stock data into a DataFrame
apple_stock = pd.read_csv("AAPL.csv", index_col="Date", parse_dates=True, usecols=['Date','Adj Close'])
print("\nAAPL.csv dataframe first 5 lines using Date as row index and Adj Close as column:\n",apple_stock.head(5))
# We load the Amazon stock data into a DataFrame
amazon_stock = pd.read_csv("AMZN.csv", index_col="Date", parse_dates=True, usecols=['Date','Adj Close'])
print("\nAMZN.csv dataframe first 5 lines using Date as row index and Adj Close as column:\n",amazon_stock.head(5))
