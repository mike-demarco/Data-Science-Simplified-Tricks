# map and format: Insert a String into a Pandas series
# January 25, 2022 by khuyentran1476
# If you want to insert a string into all values of a pandas Series, use pandas map and format.

import pandas as pd

s = pd.Series(
    ["berries", "apples", "cherries"]
)

s.map(
    "Today I bought some {}.".format
)
