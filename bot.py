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

        now = datetime.now().strftime('%m月%d日 %H時%M分')
        
        if after.channel != None:

            text = f"{member.name} が {after.channel}に入室しました"
            notifyEmbed = discord.Embed(title="入室通知", color=0x00ff00, description=text, timestamp=datetime.now())
            notifyEmbed.set_thumbnail(url=member.avatar)


        elif after.channel == None:

            text = f"{member.name} が {before.channel}から退室しました"
            notifyEmbed = discord.Embed(title="退室通知", color=0xff0000, description=text, timestamp=datetime.now())
            notifyEmbed.set_thumbnail(url=member.avatar)
            
        
        await notifyChannel.send(embed = notifyEmbed)


@client.event
async def on_guild_join(guild):
    notifyChannel = discord.utils.get(guild.text_channels, name="vc-notify")

    if notifyChannel == None:
        notifyCategory = await guild.create_category("Notify")
        notifyChannel = await guild.create_text_channel("vc-notify", category = notifyCategory)


client.run(TOKEN)