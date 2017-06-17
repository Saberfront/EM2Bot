import discord
import asyncio

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):

client.run('MzI1NzI1Nzc4MDMxNDExMjAx.DCc2_Q.o3z3f-Msx8I_uO8YeN-b7AL2hG0')