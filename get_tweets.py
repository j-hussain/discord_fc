from typing import List
try:
    import snscrape.modules.twitter as scraper
    import pandas as pd
except ModuleNotFoundError:
    !pip install snscrape
    !pip install pandas

def retrieve(accounts: List, phrase: "str") -> pd.DataFrame:

    data = []

    # crude iteration method - will make it more efficient soon
    for account in accounts:
        for iteration, tweet in enumerate(scraper.TwitterSearchScraper(f'from:{account} {phrase}').get_items()):
            if iteration > 5:
                break
            data.append([account, tweet.date.date(), tweet.content])
    # make dataframe
    tweet_df = pd.DataFrame(data, columns=["Account Username", "Date Tweeted", "Tweet"])
    # convert dates from object to datetime type
    tweet_df["Date Tweeted"] = pd.to_datetime(tweet_df["Date Tweeted"])
    # sort values in recency
    tweet_df.sort_values(by="Date Tweeted", ascending=False, inplace=True)
    display(tweet_df)


retrieve(["FabrizioRomano", "David_Ornstein", "NizaarKinsella"], "Chelsea")