# python3

import discord

import cogs.channel as ch

intents = discord.Intents.all()
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
    if (before.channel != after.channel) and (after.channel != None) and (member.status == discord.Status.online):
        notifyGuild = member.guild
        notifyChannel = discord.utils.get(notifyGuild.text_channels, name="vc-notify")
        await notifyChannel.send(f"{member.name} join {after.channel}")
        print(f"{member.name} が {after.channel}　に参加しました")


@client.event
async def on_guild_join(guild):
    notifyChannel = discord.utils.get(guild.text_channels, name="vc-notify")

    if notifyChannel == None:
        notifyCategory = await guild.create_category("Notify")
        notifyChannel = await guild.create_text_channel("vc-notify", category = notifyCategory)


client.run(TOKEN)