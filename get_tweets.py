from typing import List
import csv
import sys, subprocess

try:
    import snscrape.modules.twitter as scraper
    import pandas as pd
except ModuleNotFoundError:
    install_module("snscrape")
    install_module("pandas")

def install_module(module):
    return subprocess.check_call([sys.executable, "-m", "pip", "install", module])

def retrieve(phrase: "str") -> pd.DataFrame:
    # get data from CSV file
    accounts = ["DavidOrnstein", "FabrizioRomano", "NizaarKinsella"]
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
    output = tweet_df.to_dict()
    print("\n\n\n\n\n")
    return output

retrieve("Chelsea")