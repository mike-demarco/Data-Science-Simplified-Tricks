import pandas as pd

df = pd.DataFrame({"a": ["1,2", "4,5"],
                   "b": [11, 13]})

# Turn strings into lists
df.a = df.a.str.split(",")
df

# Split element in the list into
# multiple rows

# df.explode('a')
