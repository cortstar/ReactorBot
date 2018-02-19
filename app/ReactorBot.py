import discord
import asyncio
import sys

'''Technically, users with the same username but different IDs 
could be reacted to if Reactorbot is in both servers.
The bot is for personal use. All you have to do is include the ID in 
the configuration and check for it in the code if you want to deploy Reactorbot to a bunch of servers.'''

if len(sys.argv) < 2:
    print("Failure to launch, provide an app token for the bot!")
    exit()

client = discord.Client()

user_emoji_pairs = {}

#parse the config file
config_file = open("config.txt", "r")

for line in config_file.readlines()[1:]:
    args = line.split("~")
    try:
        user_emoji_pairs[args[0].lower()] = args[1].lower()
    except KeyError:
        print("Misconfigured line in config file, skipping.")

config_file.close()

print(user_emoji_pairs)

@client.event
async def on_ready():
    print("Logged in as {}{} \n".format(client.user.name, client.user.id))

@client.event
async def on_message(message):
    reaction = None
    try:
        reaction = user_emoji_pairs[message.author.name]
    except KeyError:
        return

    for emoji in message.author.server.emojis:
        if emoji.name.lower() == reaction.lower():
            print("Reacting to {}'s message @{}".format(message.author, message.timestamp))
            try:
                await client.add_reaction(message, emoji)
            except discord.Forbidden:
                print("warning, bot does not have permission to add a reaction.")

client.run(sys.argv[1])
