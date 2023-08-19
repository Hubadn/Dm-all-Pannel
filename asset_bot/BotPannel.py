import discord , os
from discord.ext import commands
from discord import Webhook, RequestsWebhookAdapter
user_dm = 0
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

    guild_id : int = input("enter discord guild id : ")
    time_sleep : int = input("coldown between send message (if you time sleep is littel your bot can be flagged) : ")
    type_message = input("what time of message do you want to send\n embed[1]\nmessage[2]")
    if type_message == "1":

        embed_title = input("title of embed : ")
        embed_description = input("description of embed : ")

        embed = discord.Embed(
            title = embed_title,
            description = embed_description
        )

        embed_image = input("enter image link (if you don't want press enter)")

        if embed_image == "":
            pass
        if embed_image != "":
            embed.set_image(url= embed_image)
    if type_message == "2":
        message_user = input("write your dm-all message : ")
    guild= client.get_guild(guild_id)
    print("you dm-all is ready to work ")
    input(
        f"""
guild name :  {guild.name}
guild members : {len(guild.members)}
type message : {type_message}
time sleep  : {time_sleep}

press enter for star dm-all        """)    
        
    print(f"user dm-all {user_dm}/{len(guild.members)}")
    for member in guild.members :
        if type_message =="1":
            try :
                await member.send(embed = embed)
                user_dm = user_dm  + 1
            except: 
                pass

        elif type_message == "2":

            try :
                await member.send(message_user)
                user_dm = user_dm  + 1
            except: 
                pass             

        SetupTools.clear()

        
        print(f"user dm-all {user_dm}/{len(guild.members)}")




            