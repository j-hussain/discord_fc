# Bot.py

import hikari, lightbulb
import datetime
import get_tweets

def format_tweets(name: str) -> pd.DataFrame:
    get_tweets.retrieve()

with open("../APIKeys/DFN_token.txt") as f:
    api_token = f.read()

bot = lightbulb.BotApp(api_token)
@bot.listen(hikari.StartedEvent)
async def on_started(event):
    print(f"Bot has started at {datetime.now()}")

@bot.command
@lightbulb.command("search", "Searches for twitter related news about a given player.")
@lightbulb.option("phrase", "Phrase you'd like to search", type=str)
@lightbulb.implements(lightbulb.SlashCommand)
async def search(ctx):
    await ctx.respond( format_tweets(ctx.options.phrase) )

bot.run()