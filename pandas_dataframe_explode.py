# pd.DataFrame.explode: Transform Each Element in an Iterable to a Row
# July 8, 2021 by khuyentran1476
# When working with pandas DataFrame, if you want to transform each element in an iterable to a row, use explode.
import pandas as pd

df = pd.DataFrame({'a': [[1, 2], [4, 5]],
                   'b': [11, 13]})
df

df.explode('a')

