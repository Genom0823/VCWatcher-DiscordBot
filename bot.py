# python3

import discord
from datetime import datetime

#import cogs.channel as ch

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
        notify_guild = member.guild
        # get notify channel
        notify_channel = discord.utils.get(notify_guild.text_channels, name="vc-notify")
        
        if after.channel != None:

            text = f"{member.name} が 『{after.channel}』 に入室しました"

            notify_embed = discord.Embed(
                title="入室通知", 
                color=0xabdab5, 
                description=text, 
                timestamp=datetime.now()
                )
            
            notify_embed.set_thumbnail(url=member.avatar)

        elif after.channel == None:

            text = f"{member.name} が 『{before.channel}』 から退室しました"

            notify_embed = discord.Embed(
                title="退室通知", 
                color=0xf28b82, 
                description=text, 
                timestamp=datetime.now()
                )
            
            notify_embed.set_thumbnail(url=member.avatar)

        
        await notify_channel.send(embed = notify_embed)


@client.event
async def on_guild_join(guild):

    notify_channel = discord.utils.get(guild.text_channels, name="vc-notify")

    
    # create notify channel
    if notify_channel == None:
        notify_category = await guild.create_category("Notify")
        notify_channel = await guild.create_text_channel("vc-notify", category = notify_category)


@client.event
async def on_presence_update(before, after):

    if after.activity != None:
        activity_guild = after.guild
        activity_channel = discord.utils.get(activity_guild.text_channels, name="vc-notify")
        print(f'{after.guild}:{after.activity.name}')


client.run(TOKEN)