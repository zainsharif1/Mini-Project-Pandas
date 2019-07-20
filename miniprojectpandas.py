# We import pandas into Python
import pandas as pd

# We read in a stock data data file into a data frame and see what it looks like
goog_data = pd.read_csv("GOOG.csv")

# We display the first 5 rows of the DataFrame
print(goog_data.head(5))
