import discord
import asyncio
from discord.ext import commands
import squadFunctionsHelp

description = '''The official EM2 Bot and the official Discord Bot for Saberfront: Alderaanian Assault 3
The main set of comands that can be used here are for the new UMS Squad System.
'''
EM2Server = commands.Bot(command_prefix='em2:', description=description)

@EM2Server.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

    
@EM2Server.command()
async def squadFunctionInfo(squadFunc : str):
    """Helps you understand what a specified UMS Squad Function means."""
    await EM2Server.say(squadFunctionsHelp.getSquadFunction(squadFunc))


client.run('MzI1NzI1Nzc4MDMxNDExMjAx.DCc2_Q.o3z3f-Msx8I_uO8YeN-b7AL2hG0')
