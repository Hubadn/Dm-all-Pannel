import discord , os
from discord.ext import commands
from discord import Webhook, RequestsWebhookAdapter

class SetupTools :


    def dowloader():

        os.system("pip uninstall discord.py")
        os.system("pip install discord.py==1.7.3")

    def clear():
        os.system("cls")

intents = discord.Intents.all()    
client = commands.Bot(command_prefix="pannel!",help_command= None,intents=intents)

@client.event
async def on_ready():

    print("lets config you dm-all")