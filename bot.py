# python3

import discord

import cogs.channel as ch

client = discord.Client()

@client.event
async def on_ready():
    for channel in ch.get_channelId(client):
        print("----------")
        print("チャンネル名：" + str(channel.name))
        print("チャンネルID：" + str(channel.id))
        print("----------")

client.run(TOKEN)