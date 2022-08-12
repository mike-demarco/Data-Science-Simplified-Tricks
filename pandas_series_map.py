# pd.Series.map: Change Values of a Pandas Series Using a Dictionary
# May 21, 2021 by khuyentran1476
# If you want to change values of a pandas Series using a dictionary, use pd.Series.map. Find an example of this method above.
import pandas as pd

s = pd.Series(['a', 'b', 'c'])
s

s.map({'a': 1, 'b': 2, 'c': 3})
