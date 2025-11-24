import pandas as pd

# DATAFRAME
# A dataframe is a table
pd.DataFrame({'Yes': [50, 21], 'No': [131, 2]})
"""
    Yes    No
0   50     131
1   21     2
"""
# the "0, No" entry has the value of 131. The "0, Yes" entry has a value of 50

pd.DataFrame({'Bob': ['I liked it.', 'It was awful.'], 
              'Sue': ['Pretty good.', 'Bland.']},
             index=['Product A', 'Product B'])
"""
            Bob	            Sue
Product A	I liked it.	    Pretty good.
Product B	It was awful.	Bland.
"""


# SERIES
# A Series is a sequence of data values. If a DataFrame is a table, a Series is a list
pd.Series([30, 35, 40], index=['2015 Sales', '2016 Sales', '2017 Sales'], name='Product A')
"""
2015 Sales    30
2016 Sales    35
2017 Sales    40
Name: Product A, dtype: int64
"""


# READ CSV (Comma-Separated Values)
wine_reviews = pd.read_csv("../input/wine-reviews/winemag-data-130k-v2.csv")

# Check size
wine_reviews.shape
"""
(129971, 14)
wine_reviews has 130,000 records split across 14 different columns, about 2 million entries
"""

# Check top few lines
wine_reviews.head()

# Use the first column as index
wine_reviews = pd.read_csv("../input/wine-reviews/winemag-data-130k-v2.csv", index_col=0)
wine_reviews.head()