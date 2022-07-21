from typing import List
try:
    import snscrape.modules.twitter as scraper
    import pandas as pd
except ModuleNotFoundError:
    !pip install snscrape
    !pip install pandas

import snscrape.modules.twitter as scraper
import pandas as pd

def retrieve(accounts: List, phrase: "str") -> pd.DataFrame:

    data = []

    # crude iteration method - will make it more efficient soon
    for account in accounts:
        for iteration, tweet in enumerate(scraper.TwitterSearchScraper(f'from:{account} {phrase}').get_items()):
            if iteration > 5:
                break
            data.append([account, tweet.date, tweet.content])

    tweet_df = pd.DataFrame(data, columns=["Account Username", "Date Tweeted", "Tweet"])
    display(tweet_df)
retrieve(["FabrizioRomano, David_Ornstein"])