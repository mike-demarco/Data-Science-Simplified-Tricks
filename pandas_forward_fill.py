# Forward Fill in Pandas: Use the Previous Value to Fill the Current Missing Value
# August 20, 2021 by khuyentran1476
# If you want to use the previous value in a column or a row to fill the current missing value in a pandas DataFrame,
# use df.fillna(method=’ffill’). ffill stands for forward fill.

import pandas as pd
import numpy as np

df = pd.DataFrame({'a': [1, np.nan, 3],
                   'b': [4, 5, np.nan],
                   'c': [1, 2, 3]})
print(df)

df = df.fillna(method='ffill')
print(df)
