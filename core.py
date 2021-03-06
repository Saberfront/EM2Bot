import discord
import asyncio
from discord.ext import commands
import squadFunctionsHelp
import mobItems

description = '''The official EM2 Bot and the official Discord Bot for Saberfront: Alderaanian Assault 3
The main set of commands that can be used here are for the new UMS Squad System AND Extraction Mode 2.
'''
EM2Server = commands.Bot(command_prefix='em2:', description=description)

@EM2Server.event
async def on_ready():
    print('Logged in as')
    print(EM2Server.user.name)
    print(EM2Server.user.id)
    print('------')

    
@EM2Server.command()
async def squadFunctionInfo(squadFunc : str):
    """Helps you understand what a specified UMS Squad Function means."""
    await EM2Server.say(squadFunctionsHelp.getSquadFunction(squadFunc))

@EM2Server.command()
async def availableSquadBlasters():
    """ Shows a list of blasters available for Player Soldiers (Mobs) to use. """
    await EM2Server.say(mobItems.getBlasterString())

EM2Server.run('MzI1NzI1Nzc4MDMxNDExMjAx.DCc2_Q.o3z3f-Msx8I_uO8YeN-b7AL2hG0')
