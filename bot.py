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
        print(f"{guild.member_count} menbers is in {guild.name} now")
        channel = guild.system_channel
        await channel.send("Hello!!")

    #guild = client.get_guild(guild_id)

    # debug
    #print(f"{guild.member_count} menbers is in {guild.name} now")


client.run(TOKEN)