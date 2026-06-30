import pandas as pd

def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
       # Filter the DataFrame to find tweets where the content length is strictly greater than 15
    invalid = tweets[tweets['content'].str.len() > 15]
    
    # Select and return only the 'tweet_id' column
    return invalid[['tweet_id']]