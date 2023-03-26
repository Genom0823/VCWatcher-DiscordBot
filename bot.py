# python3

import discord

import cogs.channel as ch

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents = intents)

@client.event
async def on_ready():

    await client.wait_until_ready()

    for guild in client.guilds:
        try:
            print(f"{guild.member_count} menbers is in {guild.name} now")
            channel = discord.utils.get(client.guilds, name="d")
            await channel.send("Hello!!")

        except:
            print("no exist channel")


client.run(TOKEN)