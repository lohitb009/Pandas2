import pandas as pd

def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    
    # get the Series
    isValid = tweets['content'].str.len() > 15

    # print(type(invalid_tweets))
    # print(invalid_tweets)

    # get True tweets
    df = tweets[isValid] # from tweets pick up True value.

    return df[['tweet_id']]