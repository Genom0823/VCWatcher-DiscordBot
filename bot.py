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
            channel = discord.utils.get(guild.text_channels, name="d")
            await channel.send("Hello!!")

        except:
            print("no exist channel")


@client.event
async def on_voice_state_update(member, before, after):
    if before.channel != after.channel:
        print(f"{member.name} join {after.channel}")


@client.event
async def on_guild_join(guild):
    print("new!")


client.run(TOKEN)