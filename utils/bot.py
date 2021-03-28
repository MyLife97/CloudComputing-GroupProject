# -*- coding: utf-8 -*-
import discord

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    print(message)
    await message.channel.send("Message Received.")

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

client.run('ODI1NjA5ODE1NzMyNTE4OTQz.YGAbDw.M8ao6H2Dw1pnevN_p-r_Ul6qlOI')
