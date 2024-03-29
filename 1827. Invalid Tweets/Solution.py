import pandas as pd

def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    tweets["length"] = [len(x) for x in tweets["content"]]
    short_tweets = tweets[tweets["length"] > 15]
    short_tweets = short_tweets[["tweet_id"]]
    return short_tweets
