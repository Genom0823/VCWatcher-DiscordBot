# python3

import discord
from datetime import datetime

import cogs.channel as ch

intents = discord.Intents.all()
intents.message_content = True
client = discord.Client(intents = intents)

@client.event
async def on_ready():
    await client.wait_until_ready()
    print('起動しました')


@client.event
async def on_voice_state_update(member, before, after):
    if (before.channel != after.channel) and (member.status == discord.Status.online):
        
        # get guild
        notifyGuild = member.guild
        # get notify channel
        notifyChannel = discord.utils.get(notifyGuild.text_channels, name="vc-notify")

        now = datetime.now().strftime('%Y.%m.%d %H:%M:%S')
        
        if after.channel != None:

            notifyEmbed = discord.Embed(title="入室通知", color=0x00ff00, timestamp=datetime.now())
            notifyEmbed.add_field(name = "日時", value = now)
            text = f"{now}: {member.name} が {after.channel}　に参加しました"


        elif after.channel == None:

            text = f"{now}: {member.name} が {before.channel}　から退室しました"
        

        await notifyChannel.send(embed = notifyEmbed)


@client.event
async def on_guild_join(guild):
    notifyChannel = discord.utils.get(guild.text_channels, name="vc-notify")

    if notifyChannel == None:
        notifyCategory = await guild.create_category("Notify")
        notifyChannel = await guild.create_text_channel("vc-notify", category = notifyCategory)


client.run(TOKEN)