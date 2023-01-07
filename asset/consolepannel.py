
import sys,time,json, urllib.request,os,platform, discord
from colorama import Back, Fore, Style, deinit, init
from discord.ext import commands
from discord import Webhook, RequestsWebhookAdapter
with open('asset/db/config.json', 'r') as f:
                prefixes = json.load(f)
prefix = prefixes["prefix"]
intents = discord.Intents.all()
client = commands.Bot(command_prefix=prefix,help_command= None,intents=intents)
@client.event
async def on_ready():
    with open('asset/db/config.json', 'r') as f:
                prefixes = json.load(f)
    weburl = prefixes["webhook"]
    webhook = Webhook.from_url(f"{weburl}", adapter=RequestsWebhookAdapter())
    webhook.send("your successfully ready to dm-all")
    print(Fore.WHITE + "what is the status of your bot for setupt rep <stream/play/watch>")
    rep = input()
    if rep == "stream":
            aac = input("What do you want y Stream ?")
            game = discord.Streaming(name=f"{aac}",url='https://twitch.tv/abcdefg')
            await client.change_presence(status=discord.Status.online, activity=game)
            ac1 = print(f"Activiter change for : stream {aac}")
    if rep == "play":
        aab = input("What do you want y play ?")
        game = discord.Game(name=f"{aab}")
        await client.change_presence(status=discord.Status.online, activity=game)
        print(f"Activiter  change for  :  play at {aab}")
    if rep == "watch":
            regarde1 = input("What do you want y watch ?")
            await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name= regarde1))
            print(f"Activiter change for  : Regarde {regarde1} ")        
    print(f'{Fore.GREEN}Logged in as {client.user.name}#{client.user.discriminator}!')
    print("how server do you woold like to dm-all all or id")
    rep_dmall =input("all/serverid : ")
    if rep_dmall == "all":
        print("y have to do y do later bro ;)")
        basemenureboot()
        return
    else:
        try :
            guild = client.get_guild(int(rep_dmall))
        except:
            print(f"{Fore.RED}Invalid server id")
            rep_dmall2 = input("please re send an server id correctly")
            guild = client.get_guild(int(rep_dmall2))
        sleeptime = 0
        sleeptime = input("How many y sleep between messages? : ")
        int(sleeptime)
        timeeti = guild.member_count * sleeptime
        fdmall = 0
        tdmall = 0
        erreur = 0
        message = input("Message : ")
        members = guild.members
        timedm =  datetime.timedelta(seconds=int(timeeti))
        for member in members:
            time.sleep(sleeptime)
            try:
                    await member.send(message)
                    tdmall = tdmall + 1
                
            except:
                    fdmall = fdmall + 1
                    erreur = erreur + 1
                    if erreur ==  20:
                        webhook.send("je n'ai pas pu envoyer le message a 20 membre je pense que je suis flag va verifier sur le portal dev bg ;)")
        embed = discord.Embed(
            title = f"{guild.name} Dm-all",
            description = f"{tdmall} message(s) envoyé(s) & {fdmall} message(s) non-envoyé(s)",
        )    
        embed.set_author(name= client.user.name,icon_url= client.user.avatar_url,url ="https://discord.gg/cheznimo")
        webhook.send(embed = embed)
        await client.close()
        basemenureboot()


def connect():
    try:
        urllib.request.urlopen('http://google.com') #Python 3.x
        return True
    except:
        return False
def slowtype(str):
   for c in str + '\n':
     sys.stdout.write(c)
     sys.stdout.flush()
     time.sleep(9./90)
def getmenu(type):
    with open('asset/db/config.json', 'r') as f:
        prefixes = json.load(f)
    if prefixes[type] == "":
        return  None
    else :
        return prefixes[type]
def basemenureboot():
    set.configreboot()
class set:
    def up():
        with open('asset/db/config.json', 'r') as f:
            prefixes = json.load(f)
        if prefixes["nbst"] == 0:
            slowtype("please read this")
            print("""
    Disclaimer for Nimo Dev
    If you require any more information or have any questions about our site's disclaimer, please feel free to contact us by email at flocoweb@gmail.com. Our Disclaimer was generated with the help of the Free Disclaimer Generator.

    Disclaimers for Nimo Dev
    All the information on this website - https://discord.gg/cheznimo - is published in good faith and for general information purpose only. Nimo Dev does not make any warranties about the completeness, reliability and accuracy of this information. Any action you take upon the information you find on this website (Nimo Dev), is strictly at your own risk. Nimo Dev will not be liable for any losses and/or damages in connection with the use of our website.

    From our website, you can visit other websites by following hyperlinks to such external sites. While we strive to provide only quality links to useful and ethical websites, we have no control over the content and nature of these sites. These links to other websites do not imply a recommendation for all the content found on these sites. Site owners and content may change without notice and may occur before we have the opportunity to remove a link which may have gone 'bad'.

    Please be also aware that when you leave our website, other sites may have different privacy policies and terms which are beyond our control. Please be sure to check the Privacy Policies of these sites as well as their "Terms of Service" before engaging in any business or uploading any information.

    Consent
    By using our website, you hereby consent to our disclaimer and agree to its terms.

    Update
    Should we update, amend or make any changes to this document, those changes will be prominently posted here.        
            """)
            with open('asset/db/config.json', 'r') as f:
                prefixes = json.load(f)
            nb = prefixes["nbst"] + 1 
            prefixes["nbst"] = nb

            with open('asset/db/config.json', 'w') as f: 
                    json.dump(prefixes, f, indent=4)
            return
        else:
            with open('asset/db/config.json', 'r') as f:
                prefixes = json.load(f)
            nb = prefixes["nbst"] + 1 
            prefixes["nbst"] = nb

            with open('asset/db/config.json', 'w') as f: 
                    json.dump(prefixes, f, indent=4)
    def config():
        slowtype("hello and welcome in this tools dm-all amuse to well")
        slowtype("Owner : Nimo#OOO1\nsupport : htpps://discord.gg/cheznimo")
        print("Internet Check.")
        print( 'connected' if connect() else 'no internet!')
        try :
            os.system("clear")
        except:
            os.system("CLS")
        banner = """
███╗   ██╗██╗███╗   ███╗ ██████╗ 
████╗  ██║██║████╗ ████║██╔═══██╗
██╔██╗ ██║██║██╔████╔██║██║   ██║
██║╚██╗██║██║██║╚██╔╝██║██║   ██║
██║ ╚████║██║██║ ╚═╝ ██║╚██████╔╝
╚═╝  ╚═══╝╚═╝╚═╝     ╚═╝ ╚═════╝         
help for more information"""
        print(banner)
        repmenu = input("nimo@root:~$ ")
        while repmenu != "exit":
            if repmenu == "help":
                menu.help()     
                basemenureboot()      
            if repmenu == "config":
                menu.menuconfig()
                if menu.menuconfig() == True:
                  basemenureboot()  
            if repmenu == "botconfig":
                menu.botconfig()
                if menu.botconfig() == True:
                  basemenureboot()  
            if repmenu == "dmall":
                    menu.dmall()
        while repmenu == "exit":
            return
    def configreboot():
                banner = """
███╗   ██╗██╗███╗   ███╗ ██████╗ 
████╗  ██║██║████╗ ████║██╔═══██╗
██╔██╗ ██║██║██╔████╔██║██║   ██║
██║╚██╗██║██║██║╚██╔╝██║██║   ██║
██║ ╚████║██║██║ ╚═╝ ██║╚██████╔╝
╚═╝  ╚═══╝╚═╝╚═╝     ╚═╝ ╚═════╝         
help for more information"""
                print(banner)
                repmenu = input("nimo@root:~$ ")
                while repmenu != "exit":
                    if repmenu == "help":
                        menu.help()
                        basemenureboot()
                    if repmenu == "config":
                        menu.menuconfig()
                        if menu.menuconfig() == True:
                            basemenureboot()  
                    if repmenu == "botconfig":
                        menu.botconfig()
                        if menu.botconfig() == True:
                            basemenureboot() 
                    if repmenu == "dmall":
                        menu.dmall()
                
                while repmenu == "exit":
                    return

class menu:  
    def help():
        print("config\ndmall")
        input()
    def menuconfig():
        bannerconfig = f"""
[1]Token : {getmenu(type = "token")}
[2]Prefix : {getmenu(type = "prefix")}
[3]Ownerid : {getmenu(type = "ownerid")}
[4]Webhook : {getmenu(type = "webhook")}
        """
        print(bannerconfig)
        request_valeur = input("enter the number corresponding to your request: ")
        while request_valeur != "exit":
            if request_valeur == "1": 
                print("What is the new token of your bot")
                token = input(": ")
                with open('asset/db/config.json', 'r') as f:
                    prefixes = json.load(f)
                prefixes["token"] = token

                with open('asset/db/config.json', 'w') as f: 
                        json.dump(prefixes, f, indent=4)
                return
            if request_valeur == "2": 
                print("What is the new prefix of your bot")
                prefix = input(": ")
                with open('asset/db/config.json', 'r') as f:
                    prefixes = json.load(f)
                prefixes["prefix"] = prefix

                with open('asset/db/config.json', 'w') as f: 
                        json.dump(prefixes, f, indent=4)
                return
            if request_valeur == "3": 
                print("What is the owner id of your bot")
                ownerid = input(": ")
                with open('asset/db/config.json', 'r') as f:
                    prefixes = json.load(f)
                prefixes["ownerid"] = ownerid

                with open('asset/db/config.json', 'w') as f: 
                        json.dump(prefixes, f, indent=4)
                return
            if request_valeur == "4": 
                print("What is the webhook logs:")
                webhook = input(": ")
                with open('asset/db/config.json', 'r') as f:
                    prefixes = json.load(f)
                prefixes["webhook"] = webhook

                with open('asset/db/config.json', 'w') as f: 
                        json.dump(prefixes, f, indent=4)
                return
        while request_valeur == "exit":
            print("do exit one more time")
            try :
                os.system("clear")
            except:
                os.system("CLS")
            print("do exit one more time")
            return True
    def menubot():
        content ="""
[1]Command"""
        print(content)
        content_rep = input(":")
        while content_rep!= "exit":
                if content_rep == "1":
                    print("Do you would like To load Dm-all Command to your bot in run or just use interface console for manage bot ?")
                    command_rep = input("y/n : ")
                    if command_rep == "y":
                        with open('asset/db/config.json', 'r') as f:
                            prefixes = json.load(f)
                        prefixes["load__commmand"] = "y"

                        with open('asset/db/config.json', 'w') as f: 
                                json.dump(prefixes, f, indent=4)
                    if command_rep == "y":
                        with open('asset/db/config.json', 'r') as f:
                            prefixes = json.load(f)
                        prefixes["load__commmand"] = "n"

                        with open('asset/db/config.json', 'w') as f: 
                                json.dump(prefixes, f, indent=4)
        while content_rep == "exit":
            try :
                os.system("clear")
            except:
                os.system("CLS")
            print("do exit one more time")
            return True
    def dmall():
        print(Fore.RED +"Your bot will be running in few seconds")
        with open('asset/db/config.json', 'r') as f:
                prefixes = json.load(f)
        token = prefixes["token"]
        try :
            client.run(token)
            print(Fore.GREEN +"successfully started")
        except:
            print(Fore.RED +"failed to start\n Check if you coche the privilige intentsie or verif your token")
            return
