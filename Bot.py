# Bot.py

import hikari
with open("../APIKeys/DFN_token.txt") as f:
    api_token = f.read()

bot = hikari.GatewayBot(token=api_token)

@bot.listen()
async def soap(event: hikari.GuildMessageCreateEvent) -> None:
    # don't want bot to reply to itself
    if event.is_bot or not event.content:
        return

    if.event.content.startswith("!soap"):
        await event.message.respond("Soap? What kinda name is soap?")

# async def transfer_request(event: hikari.GuildMessageCreateEvent) -> None:
"""

Implement actual interaction

"""

bot.run()