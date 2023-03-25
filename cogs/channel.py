"""
Python program that manages Discord channels.

The program includes the following main features:
- A function to retrieve channel IDs using the Discord API

"""

import discord
from discord.ext import commands

def get_channelId(client):
    return client.get_all_channels()