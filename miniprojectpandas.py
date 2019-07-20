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

# We create calendar dates between '2000-01-01' and  '2016-12-31'
dates = pd.date_range('2000-01-01', '2016-12-31')

# We create and empty DataFrame that uses the above dates as indices
all_stocks = pd.DataFrame(index = dates)

# Change the Adj Close column label to Google
google_stock = google_stock.rename(columns = {'Adj Close': 'Google'})

# Change the Adj Close column label to Apple
apple_stock = apple_stock.rename(columns = {'Adj Close': 'Apple'})

# Change the Adj Close column label to Amazon
amazon_stock = amazon_stock.rename(columns = {'Adj Close': 'Amazon'})

# We join the Google stock to all_stocks
all_stocks = all_stocks.join(google_stock)

# We join the Apple stock to all_stocks
all_stocks = all_stocks.join(apple_stock)

# We join the Amazon stock to all_stocks
all_stocks = all_stocks.join(amazon_stock)

# Check if there are any NaN values in the all_stocks dataframe
print("\nPre cleanup there are a total of {} NaN values in the all_stock dataframe".format(all_stocks.isna().sum().sum()))

# Remove any rows that contain NaN values
all_stocks = all_stocks.dropna(axis=0)

#Check to see if there are any NaN values post data cleanup
print("\nPost cleanup there are a total of {} NaN values in all_stock dataframe".format(all_stocks.isna().sum().sum()))
