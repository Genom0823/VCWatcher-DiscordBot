# python3

import discord

import cogs.channel as ch

client = discord.Client(intents = discord.Intents())

@client.event
async def on_ready():

    await client.wait_until_ready()

    for guild in client.guilds:
        channel = guild.system_channel
        await channel.send("Hello!!")

    #guild = client.get_guild(guild_id)

    # debug
    #print(f"{guild.member_count} menbers is in {guild.name} now")


client.run(TOKEN)