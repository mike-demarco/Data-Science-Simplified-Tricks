# DataFrame.pipe: Increase the Readability of your Code when Applying Multiple Functions to a DataFrame
# April 20, 2021 by khuyentran1476
# If you want to increase the readability of your code when applying multiple functions to a DataFrame,
# use DataFrame.pipe method.
#
# Find an example of using the pipe method in the code above.
import pandas as pd
from textblob import TextBlob


def remove_white_space(df: pd.DataFrame):
    df['text'] = df['text'].apply(lambda row: row.strip())
    return df


def get_sentiment(df: pd.DataFrame):
    df['sentiment'] = df['text'].apply(lambda row:
                                       TextBlob(row).sentiment[0])
    return df


df = pd.DataFrame({'text': ["It is a beautiful day today   ",
                            "  This movie is terrible"]})

df = (df.pipe(remove_white_space)
      .pipe(get_sentiment)
      )
print(df)
