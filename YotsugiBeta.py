import discord
import asyncio
import random
from random import randint
import time
import datetime
import pickle
import os
import requests
import aiohttp
from lxml import html
import sqlite3
import colorama
from colorama import init
init(autoreset = True)
from colorama import Fore, Back, Style
from discord.ext.commands import Bot
from discord.ext import commands
from credentials import Prefix as prefix
from credentials import BotToken
from credentials import Owners as owner
from credentials import EmbedColor as embed_color
from credentials import LoggingChannel as loggingchannel



##-------------------------- Credentials -----------------------##
'''owner = '145878866429345792'
ver = 'v0.5.1'
embed_color = 0xFFFF
prefix = ";"'''
ver = 'v0.5.8'
bot_author = 'Kyousei#8357'
bot_author_id = '145878866429345792'
##-----------------------------------------##
######################################################################################## Database ########################################################################################


conn = sqlite3.connect('YotsugiBot.db')
c = conn.cursor()

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS Permissions(nsfw_is_enabled INT, server_id TEXT)')
    c.execute('CREATE TABLE IF NOT EXISTS UserData(user_id TEXT, user_name TEXT, level TEXT, description TEXT, reputation TEXT, currency TEXT, avatar TEXT)')
    c.execute('CREATE TABLE IF NOT EXISTS Hackbans(user_id TEXT, server_id TEXT)')
    c.execute('CREATE TABLE IF NOT EXISTS Currency(user_id TEXT, currency TEXT)')
    c.execute('CREATE TABLE IF NOT EXISTS Quotes(server_id TEXT, quote_trigger TEXT, quote_response TEXT, added_by TEXT)')


#def data_entry():
#    c.execute("INSERT INTO Permissions VALUES(0, 0)")
#    conn.commit()
def read_from_db():
    c.execute("SELECT * FROM Permissions")
    #data = c.fetchall()
    #print(data)
    for row in c.fetchall():
        print(row)

create_table()
#data_entry()
read_from_db()


######################################################################################## Database ########################################################################################


Client = discord.Client()
bot_prefix= prefix
client = commands.Bot(command_prefix=bot_prefix)
start_time = time.time()



        
@client.event
async def on_ready():
    print("Logging In...")
    time.sleep(2)
    print("Checking files..")
    if not os.path.isfile("credentials.py"):
        print(Back.RED + "credentials.py not found! Please add it then try again!")
        await client.logout()
    elif not os.path.isfile("heads.png"):
        print(Back.RED + "heads.png not found! Please add it then try again!")
        await client.logout()
    elif not os.path.isfile("tails.png"):
        print(Back.RED + "tails.png not found! Please add it then try again!")
        await client.logout()
    elif not os.path.isfile("bbbgame.py"):
        print(Back.RED + "bbbgame.py not found! Please add it then try again!")
        await client.logout()
    elif not os.path.isfile("trivia.py"):
        print(Back.RED + "trivia.py not found! Please add it then try again!")
        await client.logout()
    elif not os.path.isfile("YotsugiBot.db"):
        print(Back.RED + "YotsugiBot.db not found! Please add it then try again!")
        await client.logout()
    elif not os.path.isfile("levelsfile.py"):
        print(Back.RED + "levelsfile.py not found! Please add it then try again!")
        await client.logout()
    time.sleep(2)
    print("Logged In | Client Credentials")
    print(Fore.YELLOW + "\n       Client Name: {}".format(client.user.name) +"\n       Client ID: {}".format(client.user.id) + "\n       Prefix: {}".format(prefix) + "\n       Embed Color: {}".format(embed_color) + "\n       Version: {}".format(ver) + "\n       Owner ID: {}".format(owner))
    #Extra 1s
    await client.change_presence(game=discord.Game(name='say ;h'))


startup_extensions = ["bbbgame", "nnn", "trivia", "testtest"]


#---------------------------------------#



filename = 'greetmsgs.txt' #What you want your file to be called

if filename in os.listdir(): #checks if the file exists and opens it if it does
	myfile = open(filename, 'rb')
	messages = pickle.load(myfile)
	del myfile
else:
	messages = {}


@client.command(pass_context = True)
async def testcmd(ctx):
        await client.say(ctx.message.channel, user.avatar_url)
        await client.user.avatar_url


'''@client.event
async def on_member_join(member):
    channel = discord.utils.get(member.server.channels, id="331954079133597706")
    embed = discord.Embed(description = "Welcome **%s** to Yotsugi Support Server! Please read rules in #rules."%member.name, color = embed_color)
    embed.set_image(url = "https://68.media.tumblr.com/a8125bf2e000b6e72da048c5305627ae/tumblr_onhfl16sgE1vjrix1o1_500.gif")
    embed.set_thumbnail(url = "https://cdn.discordapp.com/attachments/328351969611874305/352587892645822464/YotsugiPfp.png")
    await client.send_message(channel,embed = embed)'''

'''@client.event
async def on_member_remove(member):
    channel = discord.utils.get(member.server.channels, id="331954079133597706")
    embed = discord.Embed(description = "**%s** has left the server."%member.name, color = embed_color)
    await client.send_message(channel,embed = embed)
    time.sleep(2)
    await client.delete_message(channel)'''


#Stats Command
@client.command(pass_context = True, no_pm = False)
async def stats(ctx):
    second = time.time() - start_time
    minute, second = divmod(second, 60)
    hour, minute = divmod(minute, 60)
    day, hour = divmod(hour, 24)
    week, day = divmod(day, 7)
    embed = discord.Embed(title = "Yotsugi **" + ver + "**", color = embed_color)
    embed.add_field(name='Author', value=bot_author, inline=True)
    embed.add_field(name='Uptime', value="**%d** weeks, \n**%d** days, \n**%d** hours, \n**%d** minutes, \n**%d** seconds"% (week, day, hour, minute, second), inline=True)
    embed.add_field(name='Owner IDs', value=bot_author_id, inline=True)
    await client.say(embed = embed)
    print(Fore.CYAN + "Command Successfully Executed |\n       Command Ran: ;stats\n       Command Ran In:[" + ctx.message.server.id + "]\n       User:[" + ctx.message.author.id + "]\n       Channel:[" + ctx.message.channel.id + "]")
	
#
@client.command(pass_context = True)
async def ping(ctx):
    pingtime = time.time()
    pingms = await client.say("Pinging...")
    ping = time.time() - pingtime
    await client.edit_message(pingms, "Pong! :ping_pong:  The ping time is `%.1f ms`" % ping)
    print(Fore.CYAN + "Command Successfully Executed |\n       Command Ran In:[" + ctx.message.server.id + "]\n       User:[" + ctx.message.author.id + "]\n       Channel:[" + ctx.message.channel.id + "]")

'''@client.command(pass_context = True, aliases=['die'])
async def shutdown(ctx):
    embed = discord.Embed(description = "Shutting down..", color = embed_color)
    await client.say(embed = embed)
    c.close()
    conn.close()
    await client.logout()'''
 
#command1
@client.command(pass_context = True)
async def invite(ctx):
    embed = discord.Embed(title = "Here are invite links:", description = "Invite me to your server with this link: https://discordapp.com/oauth2/authorize?client_id=331766751765331969&scope=bot&permissions=66186303", color = embed_color)
    return await client.say(embed = embed)
    print(Fore.CYAN + "Command Successfully Executed |\n       Command Ran In:[" + ctx.message.server.id + "]\n       User:[" + ctx.message.author.id + "]\n       Channel:[" + ctx.message.channel.id + "]")
 
#command2
@client.command(pass_context = True, no_pm = True, aliases=['bl'])
async def banlist(ctx):
    x = await client.get_bans(ctx.message.server)
    x = '\n'.join([y.name for y in x])
    embed = discord.Embed(title = "List of Banned Members", description = x, color = embed_color)
    return await client.say(embed = embed)
    print(Fore.CYAN + "Command Successfully Executed |\n       Command Ran In:[" + ctx.message.server.id + "]\n       User:[" + ctx.message.author.id + "]\n       Channel:[" + ctx.message.channel.id + "]")
 
#command3
@client.command(pass_context=True, no_pm = True)
async def connect(ctx):
    if client.is_voice_connected(ctx.message.server):
        return await client.say("I am already connected to a voice channel. Do not disconnect me if I am in use!")
    author = ctx.message.author
    voice_channel = author.voice_channel
    vc = await client.join_voice_channel(voice_channel)
    print(Fore.CYAN + "Command Successfully Executed |\n       Command Ran In:[" + ctx.message.server.id + "]\n       User:[" + ctx.message.author.id + "]\n       Channel:[" + ctx.message.channel.id + "]")
 
#command4
@client.command(pass_context = True, no_pm = True)
async def disconnect(ctx):
    for x in client.voice_clients:
        if(x.server == ctx.message.server):
            return await x.disconnect()
            print(Fore.CYAN + "Command Successfully Executed |\n       Command Ran In:[" + ctx.message.server.id + "]\n       User:[" + ctx.message.author.id + "]\n       Channel:[" + ctx.message.channel.id + "]")

@client.command(pass_context = True, no_pm = True)
async def send(ctx, member : discord.Member, *, message):
        if ctx.message.author.server_permissions.ban_members:
            return await client.send_message(member, embed=discord.Embed(description="Message from **" + ctx.message.author.mention + "**: " + message, color = embed_color))
            print(Fore.CYAN + "Command Successfully Executed |\n       Command Ran In:[" + ctx.message.server.id + "]\n       User:[" + ctx.message.author.id + "]\n       Channel:[" + ctx.message.channel.id + "]")
        else:
            return await client.say(":x: Insufficient permissions!")
            print(Fore.RED + "Command Failed To |\n       Command Ran In:[" + ctx.message.server.id + "]\n       User:[" + ctx.message.author.id + "]\n       Channel:[" + ctx.message.channel.id + "]\nReason: " + Fore.YELLOW + "Insufficient Permissions! Both user and bot need Ban Members permission!")


'''#command5			
@client.command(pass_context = True, no_pm = True)
async def play(ctx, url):
    global queue
    global playingsong
    message = ctx.message
    print(url);
    if ctx.message.server.id in vc_clients:
        try:
            vc = await client.join_voice_channel(message.author.voice_channel) 
            vc_clients[message.server.id] = [vc]
        except Exception as e:
            print(e)
            
    if ctx.message.server.id not in vc_clients:
        try:
            vc = await client.join_voice_channel(message.author.voice_channel) 
            vc_clients[message.server.id] = [vc]

        except Exception as e:
            print(e)
            return await client.say("You are not in any voice channel.")
 
    try:
        
        mg = await client.say("Loading...")
        player = await vc_clients[ctx.message.server.id][0].create_ytdl_player(url)
        if (player.is_playing() == False):
            playingsong = False
        if (playingsong == True):
            await client.say("Added to queue")
            queue.append(url)
            print(queue)
        else:
            vc_clients[message.server.id].append(player)
            player.start()
            playingsong = True
            embed = discord.Embed(title = "Now playing :musical_note:", description = str(player.title), color = 0x0000FF)
            embed.add_field(name = "Duration (in seconds)", value = str(player.duration))
            embed.add_field(name = "Requested by", value = str(message.author))
            await client.delete_message(mg)
            await client.say(embed = embed)
            while True:
                if (playingsong == True):
                    continue
                else:
                    x = 1
                    player = await vc_clients[ctx.message.server.id][0].create_ytdl_player(queue[x])
                    vc_clients[message.server.id].append(player)
                    player.start()
                    playingsong = True
                    embed = discord.Embed(title = "Now playing :musical_note:", description = str(player.title), color = 0x0000FF)
                    embed.add_field(name = "Duration (in seconds)", value = str(player.duration))
                    embed.add_field(name = "Requested by", value = str(message.author))
                    await client.delete_message(mg)
                    await client.say(embed = embed)
                    x = x+1

    except Exception as e:
        return await client.say("ERROR: `%s"%e)'''
			
			
 
#command6
@client.command(pass_context=True, no_pm = True, aliases=['prune'])       
async def clear(ctx, number):
    embed = discord.Embed(description = ":x: Insufficient permissions!  You require **Manage Messages** permission in order to clear messages!", color = 0xF00000)
    if not ctx.message.author.server_permissions.manage_messages:
        return await client.say(embed = embed)
    mgs = []
    number = int(number) #Converting the amount of messages to delete to an integer
    async for x in client.logs_from(ctx.message.channel, limit = number):
        mgs.append(x)
    await client.delete_messages(mgs)
	
#command8
@client.command(pass_context = True)
async def author(ctx):
    embed = discord.Embed(title = "Yotsugi Bot Author:", description = "Name: **" + bot_author + "**  \n  Joined Discord: **07.02.2016  1:10 PM**  \n  **ID**: 145878866429345792  \n  **Email**: yotsugibot@gmail.com  \n  Say **;h** for commands.", color = embed_color)
    return await client.say(embed = embed)

#command9
@client.command(pass_context = True, no_pm = True, aliases=['b'])
async def ban(ctx, *, member : discord.Member = None):
    if not ctx.message.author.server_permissions.ban_members:
        return

    if not member:
        embed = discord.Embed(description = ctx.message.author.mention + ", you did not specify a user to ban! :x:", color = 0xF00000)
        return await client.say(embed = embed)
    try:
        await client.ban(member)
        print(Fore.CYAN + "Command Successfully Executed |\n       Command Ran In:[" + ctx.message.server.id + "]\n       User:[" + ctx.message.author.id + "]\n       Channel:[" + ctx.message.channel.id + "]")
    except Exception as e:
        if 'Privilege is too low' in str(e):
            embed = discord.Embed(description = "Privilege is too low. :x:", color = 0xF00000)
            return await client.say(embed = embed)

    embed = discord.Embed(description = "**%s** has been banned."  %member.name, color = 0xF00000)
    return await client.say(embed = embed)
    print(Fore.RED + "Command Failed To Execute |\n       Command Ran In:[" + ctx.message.server.id + "]\n       User:[" + ctx.message.author.id + "]\n       Channel:[" + ctx.message.channel.id + "]\n Reason: " + Fore.YELLOW + "Insufficient Permissions! Both user and bot need Ban Members permision!")
	
#command10
@client.command(pass_context = True, no_pm = True, aliases=['k'])
async def kick(ctx, *, member : discord.Member = None):
    if not ctx.message.author.server_permissions.kick_members:
        return

    if not member:
        return print("User to kick has not been specified.!")
    try:
        await client.kick(member)
        print(Fore.CYAN + "Command Successfully Executed |\n       Command Ran In:[" + ctx.message.server.id + "]\n       User:[" + ctx.message.author.id + "]\n       Channel:[" + ctx.message.channel.id + "]")
    except Exception as e:
        if 'Privilege is too low' in str(e):
            embed = discord.Embed(description = "Privilege is too low. :x:", color = 0xF00000)
            return await client.say(embed = embed)
            print(Fore.RED + "Command Failed To Execute |\n       Command Ran In:[" + ctx.message.server.id + "]\n       User:[" + ctx.message.author.id + "]\n       Channel:[" + ctx.message.channel.id + "]\n Reason: " + Fore.YELLOW + "Insufficient Permissions! Both user and bot need Kick Members permission!")

    embed = discord.Embed(description = "**%s** has been kicked."%member.name, color = 0xF00000)
    return await client.say(embed = embed)
	
#command11
@client.command(hidden = True, pass_context = True)
async def update(ctx, *update_message):
    if ctx.message.author.id != "145878866429345792": return

    update_message = ' '.join(update_message)

    embed = discord.Embed(title =  "***UPDATE***", description = update_message, color = embed_color)
    return await client.say(embed = embed)
	
#command12
@client.command(hidden = True, pass_context = True)
async def rules(ctx):
    if ctx.message.author.id != "145878866429345792": return
    embed = discord.Embed(title = 'Yotsugi Support Server Rules: ', description = "# Help is for help about bot, not a place for regular chat. 2. Spamming goes to  # spam. 3. Do not ping the owner. You will get banned. 4. Don not talk shit about anyone in  # help, # general  is where you can talk shit about anyone. ", color = embed_color)
    return await client.say(embed = embed)
	
#command14
@client.command(pass_context = True)
async def suggest(ctx, *update_message):
    if ctx.message.author.id != "145878866429345792": return
	
    update_message = ' '.join(update_message)
	
    embed = discord.Embed(title = 'Suggest new commands at:  https://github.com/YotsugiBot/suggestions/issues ', description = update_message, color = embed_color)
    return await client.say(embed = embed)
	
#command15
@client.command(hidden = True, pass_context = True)
async def announce(ctx, *update_message):
    if ctx.message.author.id != "145878866429345792": return print(Fore.RED + "Command Failed To Execute |\n       Command Ran In:[" + ctx.message.server.id + "]\n       User:[" + ctx.message.author.id + "]\n       Channel:[" + ctx.message.channel.id + "]\n Reason: " + Fore.YELLOW + "Not creator ID!")
	
    update_message = ' '.join(update_message)
	
    embed = discord.Embed(title = 'Announcement: ', description = update_message, color = embed_color)
    return await client.say(embed = embed)
	
#command16
@client.command(pass_context = True, no_pm = True)
async def mute(ctx, *, member : discord.Member):
    if not ctx.message.author.server_permissions.mute_members:
        return print(Fore.RED + "Command Failed To Execute |\n       Command Ran In:[" + ctx.message.server.id + "]\n       User:[" + ctx.message.author.id + "]\n       Channel:[" + ctx.message.channel.id + "]\n Reason: " + Fore.YELLOW + "Insufficient Permissions! User needs Mute Members permission and bot needs Manage Channels permission!")
    overwrite = discord.PermissionOverwrite()
    overwrite.send_messages = False
    await client.edit_channel_permissions(ctx.message.channel, member, overwrite)
    await client.say("**%s** has been muted!"%member.mention)

#command17
@client.command(pass_context = True, no_pm = True)
async def unmute(ctx, *, member : discord.Member):
    if not ctx.message.author.server_permissions.mute_members:
        return print(Fore.RED + "Command Failed To Execute |\n       Command Ran In:[" + ctx.message.server.id + "]\n       User:[" + ctx.message.author.id + "]\n       Channel:[" + ctx.message.channel.id + "]\n Reason: " + Fore.YELLOW + "Insufficient Permissions! User needs Mute Members permission and bot needs Manage Channels permission!")
    overwrite = discord.PermissionOverwrite()
    overwrite.send_messages = True
    await client.edit_channel_permissions(ctx.message.channel, member, overwrite)
    await client.say("**%s** has been unmuted!"%member.mention)

    
#command19
answers = ["My source say no.", "I completely disagree.", "No way in hell!", "Sure! :D", "Why not?", "Why would you say that?", "When life gives you lemons, throw them at people!", "HA, You wish!", "Keep dreaming!", "Does a green light mean go?", "Red is supposed to stop you, but your magic is TOO strong! :sweat:", "Power outage!??! WHAT ABOUT MY WIFI!??!!", "Hmmm.. this is hard", "lol, just lol.", "Cleverbot is no match for me! Haahahaha", "The chances of that happening are equal to the chances of shivaco getting a girlfriend. Null!", "There's an admin watching :scream:", "Ask me tomorrow :zzz:", "No... I mean yes... Well... Ask again later"]

@client.command(description='Decides for you.', aliases=['8ball'])
async def eightball(*choices):
    if len(choices) == 0:
        return await client.say("Ask me a yes or no question.")
    embed = discord.Embed(description = random.choice(answers), color = embed_color)
    await client.say(embed = embed)
    print(Fore.CYAN + "Command Successfully Executed |\n       Command Ran In:[" + ctx.message.server.id + "]\n       User:[" + ctx.message.author.id + "]\n       Channel:[" + ctx.message.channel.id + "]")


#command20
@client.command()
async def roll(dice : str):
    """--- Rolled with NdN format. Example: 5d3"""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        embed = discord.Embed(description = ":x: Format has to be in NdN! (**Example:** `;roll 5d50`)", color = 0xFF0000)
        await client.say(embed = embed)
        return
    if (rolls > 100) or (limit > 100):
        embed = discord.Embed(description = ":x: You can't roll more than 100!", color = 0xFF0000)
        await client.say(embed = embed)
        print(Fore.RED + "Command Halted |\n       Command Ran In:[" + ctx.message.server.id + "]\n       User:[" + ctx.message.author.id + "]\n       Channel:[" + ctx.message.channel.id + "]\n Reason: " + Fore.YELLOW + "Rolled over 100! Try again with numbers lower than 100. Example= ;roll 100d100")
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    embed = discord.Embed(description = result, color = embed_color)
    await client.say(embed = embed)


#command21
@client.command()
async def github():
    """Link to Github"""
    embed = discord.Embed(description = "Yotsugi Github can be found here: https://github.com/YotsugiBot", color = embed_color)
    embed.set_thumbnail(url = "https://cdn.discordapp.com/attachments/328351969611874305/352587892645822464/YotsugiPfp.png")
    await client.say(embed = embed)
    print(Fore.CYAN + "Command Successfully Executed |\n       Command Ran In:[" + ctx.message.server.id + "]\n       User:[" + ctx.message.author.id + "]\n       Channel:[" + ctx.message.channel.id + "]")


#command22
@client.command(pass_context = True)
async def servers(ctx):
    x = '\n'.join([str(server) for server in client.servers])
    print(x)
    embed = discord.Embed(title = "Servers", description = x, color = 0xFFFFF)
    return await client.say(embed = embed)
    print(Fore.CYAN + "Command Successfully Executed |\n       Command Ran In:[" + ctx.message.server.id + "]\n       User:[" + ctx.message.author.id + "]\n       Channel:[" + ctx.message.channel.id + "]")


@client.event
async def on_member_join(member):
    channel = discord.utils.get(member.server.channels, id="331954079133597706")
    embed = discord.Embed(description = "Welcome to Yotsugi Support Server, %s"%member.mention, color = embed_color)
    embed.set_author(name=member.name, url=member.avatar_url, icon_url=avatar_url)
    await client.send_message(channel, embed = embed)
    await client.process_commands()



@client.command(pass_context = True, no_pm = True, aliases=['serid'])
async def serverid(ctx, *, member = discord.Member):
    embed = discord.Embed(description = ctx.message.author.mention + ", ID of this server is:** " + ctx.message.channel.server.id + "**", color = embed_color)
    await client.say(embed = embed)
    print(Fore.CYAN + "Command Successfully Executed |\n       Command Ran In:[" + ctx.message.server.id + "]\n       User:[" + ctx.message.author.id + "]\n       Channel:[" + ctx.message.channel.id + "]")

@client.command(pass_context = True, no_pm = True, aliases=['chnlid'])
async def channelid(ctx):
    embed = discord.Embed(description = ctx.message.author.mention + ", ID of this channel is:** " + ctx.message.channel.id + "**", color = embed_color)
    await client.say(embed = embed)
    print(Fore.CYAN + "Command Successfully Executed |\n       Command Ran In:[" + ctx.message.server.id + "]\n       User:[" + ctx.message.author.id + "]\n       Channel:[" + ctx.message.channel.id + "]")


@client.command(pass_context=True, no_pm=True, aliases=['remrl'])
async def removerole(ctx, user: discord.Member, *, role):
    if ctx.message.author.server_permissions.manage_roles:
        await client.remove_roles(user, discord.utils.get(ctx.message.server.roles, name=role))
        embed = discord.Embed(description = ("Removed %s from **%s**" % (user.mention, role)), color = embed_color)
        await client.say(embed = embed)
        print(Fore.CYAN + "Command Successfully Executed |\n       Command Ran In:[" + ctx.message.server.id + "]\n       User:[" + ctx.message.author.id + "]\n       Channel:[" + ctx.message.channel.id + "]")
    else:
        embed = discord.Embed(description = ":x: Insufficient permissions!", color = 0xFF0000)
        return await client.say(embed = embed)
        print(Fore.RED + "Command Failed To Execute |\n       Command Ran In:[" + ctx.message.server.id + "]\n       User:[" + ctx.message.author.id + "]\n       Channel:[" + ctx.message.channel.id + "]\n Reason: " + Fore.YELLOW + "Insufficient Permissions! Manage Roles permission is needed!")


@client.command(pass_context=True, no_pm=True, aliases=['setrl'])
async def setrole(ctx, user: discord.Member, *, role):
    if ctx.message.author.server_permissions.manage_roles:
        await client.add_roles(user, discord.utils.get(ctx.message.server.roles, name=role))
        embed = discord.Embed(description = ("Added %s to **%s** " % (user.mention, role)), color = embed_color)
        await client.say(embed = embed)
        print(Fore.CYAN + "Command Successfully Executed |\n       Command Ran In:[" + ctx.message.server.id + "]\n       User:[" + ctx.message.author.id + "]\n       Channel:[" + ctx.message.channel.id + "]")
    else:
        embed = discord.Embed(description = ":x: Insufficient permissions!", color = 0xFF0000)
        return await client.say(embed = embed)
        print(Fore.RED + "Command Failed To Execute |\n       Command Ran In:[" + ctx.message.server.id + "]\n       User:[" + ctx.message.author.id + "]\n       Channel:[" + ctx.message.channel.id + "]\n Reason: " + Fore.YELLOW + "Insufficient Permissions! Manage Roles permission is needed!")



@client.command(pass_context = True, no_pm = True)
async def setavatar(ctx):
    avatar1 = "F:/Yotsugi/Private/avatar1.jpg"
    with open('avatar1.jpg', 'rb') as f:
            await client.edit_profile(avatar=f.read())

@client.command(pass_context = True, no_pm = True)
async def linuxupdate(ctx):
    linuxupdate = "F:/Yotsugi/Private/linuxUPDATE.sh"
    with open(linuxupdate, 'rb') as f:
        await client.say("Updating.....")

@client.command(pass_context = True, no_pm = True)
async def warn(ctx, member : discord.Member, *, message):
        if ctx.message.author.server_permissions.kick_members:
                embed = discord.Embed(description = "You've been warned for: **" + message + "**\nResponsible Moderator: **" + ctx.message.author.mention + "**\nServer: **" + ctx.message.server.name + "**", color = 0xFF0000)
                return await client.send_message(member, embed = embed)
        else:
                embed = discord.Embed(description = ":x: Insufficient Permissions", color = 0xFF0000)
                return await client.say(embed = embed)

@client.command()
async def ud(*msg):
    word = ' '.join(msg)
    api = "http://api.urbandictionary.com/v0/define"
    response = requests.get(api, params=[("term", word)]).json()
    embed = discord.Embed(description = "No results found!", color = 0xFF0000)
    if len(response["list"]) == 0: return await client.say(embed = embed)
    
    embed = discord.Embed(title = "Word", description = word, color = embed_color)
    embed.add_field(name = "Top definition:", value = response['list'][0]['definition'])
    embed.add_field(name = "Examples:", value = response['list'][0]["example"])
    embed.set_footer(text = "Tags: " + ', '.join(response['tags']))

    await client.say(embed = embed)
    print(Fore.CYAN + "Command Successfully Executed |\n       Command Ran In:[" + ctx.message.server.id + "]\n       User:[" + ctx.message.author.id + "]\n       Channel:[" + ctx.message.channel.id + "]")


@client.command(pass_context = True)
async def setgame(ctx, *, game : str):
        if owner != ctx.message.author.id:
            return await client.say(embed=embeds.permission_denied("You aren't the bot owner!"), color = 0xFF0000)
        else:
            try:
                await client.change_presence(game=discord.Game(name=game), status=ctx.message.server.me.status)
                logging.info("Set game to " + str(game))
                print(Fore.CYAN + "Command Successfully Executed |\n       Command Ran In:[" + ctx.message.server.id + "]\n       User:[" + ctx.message.author.id + "]\n       Channel:[" + ctx.message.channel.id + "]")
            except Exception as e:
                print("Failed to set game: {}".format(str(e)) + "\nIgnore this error. It's Python who's being an ass.")
                print(Fore.RED + "Command Failed To Execute |\n       Command Ran In:[" + ctx.message.server.id + "]\n       User:[" + ctx.message.author.id + "]\n       Channel:[" + ctx.message.channel.id + "]\n Reason: " + Fore.YELLOW + "Python's an ass.")



@client.command(pass_context=True, no_pm=True)
async def restart(ctx):
    if owner == ctx.message.author.id:
        embed = discord.Embed(description = "Shutting Down...", color = embed_color)
        await client.say(embed = embed)
        await client.logout()



#-----------------------------------"From Here On, It's HEAVY Testing ZONE!"------------------------------------#





#-----------------------------"Above Is HEAVY Testing ZONE!"----------------------------------------#



@client.command(hidden = True)
async def load(extension_name : str):
    """Loads an extension."""
    try:
        client.load_extension(extension_name)
    except (AttributeError, ImportError) as e:
        await client.say("```py\n{}: {}\n```".format(type(e).__name__, str(e)))
        return
        await client.say("{} loaded.".format(extension_name))



@client.command(pass_context = True, hidden=True)
async def unload(ctx, extension_name : str):
	if ctx.message.author.id != owner:
		return await client.say("Not owner. This is bot owner only command!")
	else:
		client.unload_extension(extension_name)
		await client.say("{} unloaded.".format(extension_name))


if __name__ == "__main__":
    for extension in startup_extensions:
        try:
            client.load_extension(extension)
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print('Failed to load extension {}\n{}'.format(extension, exc))


heads = "heads.png"
tails = "tails.png"
@client.command(pass_context=True, aliases=['flip'])
async def flipcoin(ctx):
    choice = random.randint(1,2)
    if choice == 1:
        await client.send_file(ctx.message.channel, heads, content=ctx.message.author.mention + ", you flipped **Heads**!", tts=False)
    if choice == 2:
        await client.send_file(ctx.message.channel, tails, content=ctx.message.author.mention + ", you flipped **Tails**!", tts=False)


@client.event
async def on_message(message):
    embed = discord.Embed(color = embed_color)
    embed.set_image(url = "https://cdn.discordapp.com/attachments/169950217007923201/360431137526382604/JPEG_20170917_221818.jpg")
    if message.content.startswith('rekt'):
        await client.send_message(message.channel, embed=embed)
    await client.process_commands(message)


@client.event
async def on_message(message):
    embed = discord.Embed(color = embed_color)
    embed.set_image(url = "https://i.imgur.com/BpfHgAd.jpg")
    if message.content.startswith('¯\\_(ツ)_/¯'):
        await client.send_message(message.channel, embed=embed)
    await client.process_commands(message)



@client.command(pass_context = True)
async def safebooru(ctx, args):
    if not args:
        tag = 'cute'
    else:
        tag = ''.join(args)
    resource = 'http://safebooru.org/index.php?page=dapi&s=post&q=index&tags=' + tag
    async with aiohttp.ClientSession() as session:
        async with session.get(resource) as data:
            data = await data.read()
    posts = html.fromstring(data)
    print(data)
    print(posts)
    print(resource)
    if len(posts) == 0:
        embed = discord.Embed(title='🔍 Nothing found.', color = 0xFF0000)
    else:
        choice = random.choice(posts)
        image_url = choice.attrib['file_url']
        icon_url = 'https://i.imgur.com/3Vb6LdJ.png'
        post_url = f'http://safebooru.org/index.php?page=post&s=view&id={choice.attrib["id"]}'
        if image_url.startswith('//'):
            image_url = 'http:' + image_url
        embed = discord.Embed(color=embed_color)
        embed.set_author(name='Safebooru', icon_url=icon_url, url=post_url)
        embed.set_image(url=image_url)
        embed.set_footer(
            text=f'Score: {choice.attrib["score"]} | Size: {choice.attrib["width"]}x{choice.attrib["height"]}')
    await client.send_message(ctx.message.channel, embed=embed)

################## HELP COMMAND ##################
@client.command(aliases=['help'])
async def h(command = None):
    embed = discord.Embed(description = "**Hosting Guides: https://github.com/Kyousei/YotsugiBot/wiki** \n**Commands List: https://goo.gl/w6Aoag**", color = embed_color)
    if not command:
            await client.say(embed = embed)
            return

        #some code to check if the command is an actual command (depends on how you make commands)
    if command == prefix+'b':
        embed = discord.Embed(title = "`" + prefix + "ban` / `" + prefix + "b`", description = "Bans the user from the server", color = embed_color)
        embed.add_field(name='Usage', value="`"+ prefix +"ban @User/ID` or `"+ prefix +"b @User/UserID`", inline=True)
        embed.add_field(name='User Permissions:', value='Ban Members', inline=True)
        embed.add_field(name='Bot Permissions:', value='Ban Members', inline=True)
        await client.say(embed = embed)
        return

    if command == prefix+'ban':
        embed = discord.Embed(title = "`" + prefix + "ban` / `" + prefix + "b`", description = "Bans the user from the server", color = embed_color)
        embed.add_field(name='Usage', value="`"+ prefix +"ban @User/ID` or `"+ prefix +"b @User/UserID`", inline=True)
        embed.add_field(name='User Permissions:', value='Ban Members', inline=True)
        embed.add_field(name='Bot Permissions:', value='Ban Members', inline=True)
        await client.say(embed = embed)
        return


    if command == prefix+'kick':
        embed = discord.Embed(title = "`"+ prefix +"kick` / `"+ prefix +"k`", description = "Kicks the user from the server", color = embed_color)
        embed.add_field(name='Usage', value="`" + prefix +"kick @User/ID` or `" + prefix +"k @User/UserID`", inline=True)
        embed.add_field(name='User Permissions:', value='Kick Members', inline=True)
        embed.add_field(name='Bot Permissions:', value='Kick Members', inline=True)
        await client.say(embed = embed)
        return

    if command == prefix+'k':
        embed = discord.Embed(title = "`"+ prefix +"kick` / `"+ prefix +"k`", description = "Kicks the user from the server", color = embed_color)
        embed.add_field(name='Usage', value="`" + prefix +"kick @User/ID` or `" + prefix +"k @User/UserID`", inline=True)
        embed.add_field(name='User Permissions:', value='Kick Members', inline=True)
        embed.add_field(name='Bot Permissions:', value='Kick Members', inline=True)
        await client.say(embed = embed)
        return

    if command == prefix+'serverid':
        embed = discord.Embed(title = "`"+ prefix +"serverid` / `"+ prefix +"serid`", description = "Show's the ID of the server.", color = embed_color)
        embed.add_field(name='Usage', value="`"+ prefix +"serverid` or `;serid`", inline=True)
        embed.add_field(name='User Permissions:', value='**Bot Owner**', inline=True)
        embed.add_field(name='Bot Permissions:', value='Send Messages', inline=True)
        await client.say(embed = embed)
        return

    if command == prefix+'ud':
        embed = discord.Embed(title = "`"+ prefix +"ud`", description = "Searches urban disctionary for the meaning of a word.", color = embed_color)
        embed.add_field(name='Usage', value="`"+ prefix +"ud lol`", inline=True)
        embed.add_field(name='User Permissions:', value='`None`', inline=True)
        embed.add_field(name='Bot Permissions:', value='Send Messages', inline=True)
        await client.say(embed = embed)
        return

    if command == prefix+'8ball':
        embed = discord.Embed(title = "`"+ prefix +"eightball` / `"+ prefix +"8ball`", description = "8balls your question.", color = embed_color)
        embed.add_field(name='Usage', value="`"+ prefix +"eightball to be or not to be` or `"+ prefix +"8ball to be or not to be`", inline=True)
        embed.add_field(name='User Permissions:', value='`None`', inline=True)
        embed.add_field(name='Bot Permissions:', value='Send Messages', inline=True)
        await client.say(embed = embed)
        return

    if command == prefix+'eightball':
        embed = discord.Embed(title = "`"+ prefix +"eightball` / `"+ prefix +"8ball`", description = "8balls your question.", color = embed_color)
        embed.add_field(name='Usage', value="`"+ prefix +"eightball to be or not to be` or `"+ prefix +"8ball to be or not to be`", inline=True)
        embed.add_field(name='User Permissions:', value='`None`', inline=True)
        embed.add_field(name='Bot Permissions:', value='Send Messages', inline=True)
        await client.say(embed = embed)
        return

    if command == prefix+'serid':
        embed = discord.Embed(title = "`"+ prefix +"serverid` / `"+ prefix +"serid`", description = "Show's the ID of the server.", color = embed_color)
        embed.add_field(name='Usage', value="`"+ prefix +"serverid` or `"+ prefix +"serid`", inline=True)
        embed.add_field(name='User Permissions:', value='`None`', inline=True)
        embed.add_field(name='Bot Permissions:', value='Send Messages', inline=True)
        await client.say(embed = embed)
        return

    if command == prefix+'clear':
        embed = discord.Embed(title = "`"+ prefix +"clear` / `"+ prefix +"prune` / `"+ prefix +"purge`", description = "Deletes `x` amount of messages.", color = embed_color)
        embed.add_field(name='Usage', value="`"+ prefix +"clear 5` or `"+ prefix +"prune 5` or `"+ prefix +"purge 5`", inline=True)
        embed.add_field(name='User Permissions:', value='Manage Messages', inline=True)
        embed.add_field(name='Bot Permissions:', value='Send Messages', inline=True)
        await client.say(embed = embed)
        return

    if command == prefix+'prune':
        embed = discord.Embed(title = "`"+ prefix +"clear` / `"+ prefix +"prune` / `"+ prefix +"purge`", description = "Deletes `x` amount of messages.", color = embed_color)
        embed.add_field(name='Usage', value="`"+ prefix +"clear 5` or `"+ prefix +"prune 5` or `"+ prefix +"purge 5`", inline=True)
        embed.add_field(name='User Permissions:', value='Manage Messages', inline=True)
        embed.add_field(name='Bot Permissions:', value='Send Messages', inline=True)
        await client.say(embed = embed)
        return

    if command == prefix+'purge':
        embed = discord.Embed(title = "`"+ prefix +"clear` / `"+ prefix +"prune` / `"+ prefix +"purge`", description = "Deletes `x` amount of messages.", color = embed_color)
        embed.add_field(name='Usage', value="`"+ prefix +"clear 5` or `"+ prefix +"prune 5` or `"+ prefix +"purge 5`", inline=True)
        embed.add_field(name='User Permissions:', value='Manage Messages', inline=True)
        embed.add_field(name='Bot Permissions:', value='Send Messages', inline=True)
        await client.say(embed = embed)
        return

    if command == prefix+'mute':
        embed = discord.Embed(title = "`"+ prefix +"mute`", description = "Mutes the user in the channel where command was ran.", color = embed_color)
        embed.add_field(name='Usage', value="`"+ prefix +"mute @User`", inline=True)
        embed.add_field(name='User Permissions:', value='Mute Members', inline=True)
        embed.add_field(name='Bot Permissions:', value='Manage Channels', inline=True)
        await client.say(embed = embed)
        return

    if command == prefix+'unmute':
        embed = discord.Embed(title = "`"+ prefix +"unmute`", description = "Mutes the user in the channel where command was ran.", color = embed_color)
        embed.add_field(name='Usage', value="`"+ prefix +"unmute @User`", inline=True)
        embed.add_field(name='User Permissions:', value='Mute Members', inline=True)
        embed.add_field(name='Bot Permissions:', value='Manage Channels', inline=True)
        await client.say(embed = embed)
        return

    if command == prefix+'stats':
        embed = discord.Embed(title = "`"+ prefix +"stats`", description = "Shows bot's statistics.", color = embed_color)
        embed.add_field(name='Usage', value="`"+ prefix +"stats`", inline=True)
        embed.add_field(name='User Permissions:', value='`None`', inline=True)
        embed.add_field(name='Bot Permissions:', value='Send Messages', inline=True)
        await client.say(embed = embed)
        return

    if command == prefix+'author':
        embed = discord.Embed(title = "`"+ prefix +"author`", description = "Shows information about bot author.", color = embed_color)
        embed.add_field(name='Usage', value="`"+ prefix +"author`", inline=True)
        embed.add_field(name='User Permissions:', value='`None`', inline=True)
        embed.add_field(name='Bot Permissions:', value='Send Messages', inline=True)
        await client.say(embed = embed)
        return

    if command == prefix+'banlist':
        embed = discord.Embed(title = "`"+ prefix +"banlist`", description = "Shows list of banned users for that server..", color = embed_color)
        embed.add_field(name='Usage', value="`"+ prefix +"banlist`", inline=True)
        embed.add_field(name='User Permissions:', value='`None`', inline=True)
        embed.add_field(name='Bot Permissions:', value='Send Messages', inline=True)
        await client.say(embed = embed)
        return

    if command == prefix+'ping':
        embed = discord.Embed(title = "`"+ prefix +"ping`", description = "Shows your ping to the bot..", color = embed_color)
        embed.add_field(name='Usage', value="`"+ prefix +"ping`", inline=True)
        embed.add_field(name='User Permissions:', value='`None`', inline=True)
        embed.add_field(name='Bot Permissions:', value='Send Messages', inline=True)
        await client.say(embed = embed)
        return

    if command == prefix+'connect':
        embed = discord.Embed(title = "`"+ prefix +"connect`", description = "Joins the voice channel.", color = embed_color)
        embed.add_field(name='Usage', value="`"+ prefix +"connect`", inline=True)
        embed.add_field(name='User Permissions:', value='`None`', inline=True)
        embed.add_field(name='Bot Permissions:', value='Connect', inline=True)
        await client.say(embed = embed)
        return

    if command == prefix+'disconnect':
        embed = discord.Embed(title = "`"+ prefix +"disconnect`", description = "Leaves the voice channel.", color = embed_color)
        embed.add_field(name='Usage', value="`"+ prefix +"disconnect`", inline=True)
        embed.add_field(name='User Permissions:', value='`None`', inline=True)
        embed.add_field(name='Bot Permissions:', value='Connect', inline=True)
        await client.say(embed = embed)
        return

    if command == prefix+'channelid':
        embed = discord.Embed(title = "`"+ prefix +"channelid` / `"+ prefix +"chnlid``", description = "Shows the channel ID the command was ran in.", color = embed_color)
        embed.add_field(name='Usage', value="`"+ prefix +"channelid` or `"+ prefix +"chnlid`", inline=True)
        embed.add_field(name='User Permissions:', value='`None`', inline=True)
        embed.add_field(name='Bot Permissions:', value='Send Messages', inline=True)
        await client.say(embed = embed)
        return

    if command == prefix+'chnlid':
        embed = discord.Embed(title = "`"+ prefix +"channelid` / `"+ prefix +"chnlid``", description = "Shows the channel ID the command was ran in.", color = embed_color)
        embed.add_field(name='Usage', value="`"+ prefix +"channelid` or `"+ prefix +"chnlid`", inline=True)
        embed.add_field(name='User Permissions:', value='`None`', inline=True)
        embed.add_field(name='Bot Permissions:', value='Send Messages', inline=True)
        await client.say(embed = embed)
        return

    if command == prefix+'github':
        embed = discord.Embed(title = "`"+ prefix +"github`", description = "Gives the link to GitHub.", color = embed_color)
        embed.add_field(name='Usage', value="`"+ prefix +"github`", inline=True)
        embed.add_field(name='User Permissions:', value='`None`', inline=True)
        embed.add_field(name='Bot Permissions:', value='Send Messages', inline=True)
        await client.say(embed = embed)
        return

    if command == prefix+'send':
        embed = discord.Embed(title = "`"+ prefix +"send`", description = "Sends a message to a user.", color = embed_color)
        embed.add_field(name='Usage', value="`"+ prefix +"send @User Hi`", inline=True)
        embed.add_field(name='User Permissions:', value='`None`', inline=True)
        embed.add_field(name='Bot Permissions:', value='Send Messages', inline=True)
        await client.say(embed = embed)
        return

    if command == prefix+'shutdown':
        embed = discord.Embed(title = "`"+ prefix +"die` / `"+ prefix +"shutdown`", description = "Boots the bot offline.", color = embed_color)
        embed.add_field(name='Usage', value="`"+ prefix +"shutdown` or `"+ prefix +"die`", inline=True)
        embed.add_field(name='User Permissions:', value='`None`', inline=True)
        embed.add_field(name='Bot Permissions:', value='Send Messages', inline=True)
        await client.say(embed = embed)
        return

    if command == prefix+'die':
        embed = discord.Embed(title = "`"+ prefix +"die` / `"+ prefix +"shutdown`", description = "Boots the bot offline.", color = embed_color)
        embed.add_field(name='Usage', value="`"+ prefix +"shutdown` or `"+ prefix +"die`", inline=True)
        embed.add_field(name='User Permissions:', value='`None`', inline=True)
        embed.add_field(name='Bot Permissions:', value='Send Messages', inline=True)
        await client.say(embed = embed)
        return

    if command == prefix+'setrole':
        embed = discord.Embed(title = "`"+ prefix +"setrole` / `"+ prefix +"setrl`", description = "Gives a role to a user.", color = embed_color)
        embed.add_field(name='Usage', value="`"+ prefix +"setrole @User Role-Name` or `"+ prefix +"setrl @User Role-Name`", inline=True)
        embed.add_field(name='User Permissions:', value='`None`', inline=True)
        embed.add_field(name='Bot Permissions:', value='Send Messages', inline=True)
        await client.say(embed = embed)
        return

    if command == prefix+'setrl':
        embed = discord.Embed(title = "`"+ prefix +"setrole` / `"+ prefix +"setrl`", description = "Gives a role to a user.", color = embed_color)
        embed.add_field(name='Usage', value="`"+ prefix +"setrole @User Role-Name` or `"+ prefix +"setrl @User Role-Name`", inline=True)
        embed.add_field(name='User Permissions:', value='`None`', inline=True)
        embed.add_field(name='Bot Permissions:', value='Send Messages', inline=True)
        await client.say(embed = embed)
        return

    if command == prefix+'removerole':
        embed = discord.Embed(title = "`"+ prefix +"removerole` / `"+ prefix +"remrl`", description = "Removes a role from the user.", color = embed_color)
        embed.add_field(name='Usage', value="`"+ prefix +"removerole @User Role-Name` or `"+ prefix +"remrl @User Role-Name`", inline=True)
        embed.add_field(name='User Permissions:', value='`None`', inline=True)
        embed.add_field(name='Bot Permissions:', value='Send Messages', inline=True)
        await client.say(embed = embed)
        return

    if command == prefix+'remrl':
        embed = discord.Embed(title = "`"+ prefix +"removerole` / `"+ prefix +"remrl`", description = "Removes a role from the user.", color = embed_color)
        embed.add_field(name='Usage', value="`"+ prefix +"removerole @User Role-Name` or `"+ prefix +"remrl @User Role-Name`", inline=True)
        embed.add_field(name='User Permissions:', value='`None`', inline=True)
        embed.add_field(name='Bot Permissions:', value='Send Messages', inline=True)
        await client.say(embed = embed)
        return

    if command == prefix+'flip':
        embed = discord.Embed(title = "`"+ prefix +"flip` / `"+ prefix +"flipcoin`", description = "Flips the coin.", color = embed_color)
        embed.add_field(name='Usage', value="`"+ prefix +"flip` or `"+ prefix +"flipcoin`", inline=True)
        embed.add_field(name='User Permissions:', value='`None`', inline=True)
        embed.add_field(name='Bot Permissions:', value='Send Messages, Attach Files', inline=True)
        await client.say(embed = embed)
        return

    if command == prefix+'roll':
        embed = discord.Embed(title = "`"+ prefix +"roll`", description = "Rolls the dice in NdN format.", color = embed_color)
        embed.add_field(name='Usage', value="`"+ prefix +"roll 5d5`", inline=True)
        embed.add_field(name='User Permissions:', value='`None`', inline=True)
        embed.add_field(name='Bot Permissions:', value='Send Messages', inline=True)
        await client.say(embed = embed)
        return

    if command == prefix+'servers':
        embed = discord.Embed(title = "`"+ prefix +"servers`", description = "Shows the list of servers the bot is in.", color = embed_color)
        embed.add_field(name='Usage', value="`"+ prefix +"servers`", inline=True)
        embed.add_field(name='User Permissions:', value='`None`', inline=True)
        embed.add_field(name='Bot Permissions:', value='Send Messages', inline=True)
        await client.say(embed = embed)
        return

    if command == prefix+'warn':
        embed = discord.Embed(title = "`"+ prefix +"warn`", description = "Warns the user.", color = embed_color)
        embed.add_field(name='Usage', value="`"+ prefix +"warn @USer Rude`", inline=True)
        embed.add_field(name='User Permissions:', value='Kick Members', inline=True)
        embed.add_field(name='Bot Permissions:', value='Send Messages', inline=True)
        await client.say(embed = embed)
        return

    if command == prefix+'h':
        embed = discord.Embed(title = "`"+ prefix +"h`", description = "Shows the info about a command.", color = embed_color)
        embed.add_field(name='Usage', value="`"+ prefix +"h "+ prefix +"ban`", inline=True)
        embed.add_field(name='User Permissions:', value='`None`', inline=True)
        embed.add_field(name='Bot Permissions:', value='Send Messages', inline=True)
        await client.say(embed = embed)
        return

    if command == prefix+'hentai':
        embed = discord.Embed(title = "`"+ prefix +"hentai`", description = "Posts hentai!", color = embed_color)
        embed.add_field(name='Usage', value="`"+ prefix +"hentai`", inline=True)
        embed.add_field(name='User Permissions:', value='`None`', inline=True)
        embed.add_field(name='Bot Permissions:', value='Send Messages, Attach Files, Embed Links', inline=True)
        await client.say(embed = embed)
        return

    if command == prefix+'now':
        embed = discord.Embed(title = "`"+ prefix +"now`", description = "Shows the current day, date, time, year and hours/minutes.", color = embed_color)
        embed.add_field(name='Usage', value="`"+ prefix +"now`", inline=True)
        embed.add_field(name='User Permissions:', value='`None`', inline=True)
        embed.add_field(name='Bot Permissions:', value='Send Messages, Attach Files, Embed Links', inline=True)
        await client.say(embed = embed)
        return

    if command == prefix+'prof':
        embed = discord.Embed(title = "`"+ prefix +"profile` / `" + prefix + "prof`", description = "Shows your EXP stats.", color = embed_color)
        embed.add_field(name='Usage', value="`"+ prefix +"exp` or "+prefix+"`xp`", inline=True)
        embed.add_field(name='User Permissions:', value='`None`', inline=True)
        embed.add_field(name='Bot Permissions:', value='Send Messages', inline=True)
        await client.say(embed = embed)
        return

    if command == prefix+'profile':
        embed = discord.Embed(title = "`"+ prefix +"profile` / `" + prefix + "prof`", description = "Shows your EXP stats.", color = embed_color)
        embed.add_field(name='Usage', value="`"+ prefix +"exp` or "+prefix+"`xp`", inline=True)
        embed.add_field(name='User Permissions:', value='`None`', inline=True)
        embed.add_field(name='Bot Permissions:', value='Send Messages', inline=True)
        await client.say(embed = embed)
        return

    if command == prefix+'setdesc':
        embed = discord.Embed(title = "`"+ prefix +"setdesc` / `" + prefix + "setdescription`", description = "Changes your `;sexp` description to whatever you put.", color = embed_color)
        embed.add_field(name='Usage', value="`"+ prefix +"setdesc My cool description` or "+prefix+"`setdescription My cool description`", inline=True)
        embed.add_field(name='User Permissions:', value='`None`', inline=True)
        embed.add_field(name='Bot Permissions:', value='Send Messages', inline=True)
        await client.say(embed = embed)
        return

    if command == prefix+'setdescription':
        embed = discord.Embed(title = "`"+ prefix +"setdesc` / `" + prefix + "setdescription`", description = "Changes your `;sexp` description to whatever you put.", color = embed_color)
        embed.add_field(name='Usage', value="`"+ prefix +"setdesc My cool description` or "+prefix+"`setdescription My cool description`", inline=True)
        embed.add_field(name='User Permissions:', value='`None`', inline=True)
        embed.add_field(name='Bot Permissions:', value='Send Messages', inline=True)
        await client.say(embed = embed)
        return

    if command == prefix+'hackban':
        embed = discord.Embed(title = "`"+ prefix +"hb` / `" + prefix + "hackban`", description = "Bans the user which is not in the server. **Must Be ID of the user**", color = embed_color)
        embed.add_field(name='Usage', value="`"+ prefix +"hb 123123123123` or "+prefix+"`hackban 123123123123`", inline=True)
        embed.add_field(name='User Permissions:', value='Ban Members', inline=True)
        embed.add_field(name='Bot Permissions:', value='Ban Members', inline=True)
        await client.say(embed = embed)
        return

    if command == prefix+'hb':
        embed = discord.Embed(title = "`"+ prefix +"hb` / `" + prefix + "hackban`", description = "Bans the user which is not in the server. **Must Be ID of the user**", color = embed_color)
        embed.add_field(name='Usage', value="`"+ prefix +"hb 123123123123` or "+prefix+"`hackban 123123123123`", inline=True)
        embed.add_field(name='User Permissions:', value='Ban Members', inline=True)
        embed.add_field(name='Bot Permissions:', value='Ban Members', inline=True)
        await client.say(embed = embed)
        return
################## HELP COMMAND ##################


@client.command(pass_context = True, aliases=['slotroll'])
async def rollslots(ctx):
        """ Roll the slot machine """
        emojis = "🍎🍊🍐🍋🍉🍇🍓🍒"
        a = random.choice(emojis)
        b = random.choice(emojis)
        c = random.choice(emojis)

        embed = discord.Embed(description = "Congratulations, You won!")
        if (a == b == c):
            message = 'and won! 🎉'
        elif (a == b) or (a == c) or (b == c):
            message = 'and almost won (2/3)'
        else:
            message = 'and lost...'


        result = f"**{ctx.message.author.mention}** rolled the slots...\n**[ {a} {b} {c} ]**\n{message}"
        await client.say(result)



@client.command(pass_context = True)
async def cmdtest(ctx):
    emojis = [
        ":credit_card:",
        ":moneybag:",
        ":hammer:",
        ":gear:",
        ":knife:"
        ]
    a = random.choice(emojis)
    b = random.choice(emojis)
    c = random.choice(emojis)

    if (a == b == c):
        message = "You won!"
    elif (a == b) or (b == c) or (c == a):
        message = "You still won!"
    else:
        message = "That's a shame, you lose"

        embed = discord.Embed(description = f"**{ctx.message.author.mention}** rolled the slots.\n\n\n\n **[{a} | {b} | {c}]**\n\n\n\n{message}", color = embed_color)
        await client.say(embed = embed)


hentai_images = [
    'https://cdn.discordapp.com/attachments/331827935030018048/362015619991994368/DAX32vyXkAAvSVN.jpg',
    'https://cdn.discordapp.com/attachments/331827935030018048/362015622319833098/DAXhM29W0AAHPwJ.jpg',
    'https://cdn.discordapp.com/attachments/331827935030018048/362015626744692736/e4e9524f-a2dd-4083-b768-2aab8bdde78b.jpg',
    'https://cdn.discordapp.com/attachments/331827935030018048/362015634571132940/ec4b81dd9a.jpg',
    'https://cdn.discordapp.com/attachments/331827935030018048/362015632281305088/ea527770601c3a2a9f529d12bee97ac4.png',
    'https://cdn.discordapp.com/attachments/331827935030018048/362015636983119872/eyJ1cmwiOiJodHRwczovL2Rpc2NvcmQuc3RvcmFnZS5nb29nbGVhcGlzLmNvbS9hdHRhY2htZW50cy8yODIzODU2ODAyODAxOTA5.png',
    'https://cdn.discordapp.com/attachments/331827935030018048/362015639277142017/f54c8c6dcf622c707bb2be228de18f32.jpg',
    'https://cdn.discordapp.com/attachments/331827935030018048/362015649742192640/image-59.jpg',
    'https://cdn.discordapp.com/attachments/331827935030018048/362015651780624385/image-159.jpg',
    'https://cdn.discordapp.com/attachments/331827935030018048/362015656675246081/jZx6pWTGcwE.jpg',
    'https://cdn.discordapp.com/attachments/331827935030018048/362015665009328129/Konachan.com_-_177821_aisare_roommate_bow_brown_eyes_brown_hair_censored_game_cg_loli_nohara_karen_p.png',
    'https://cdn.discordapp.com/attachments/331827935030018048/362015668356251648/Konachan.com_-_180438_bed_black_hair_blue_eyes_blush_game_cg_inagaki_sae_loli_masturbation_nonohara_.png',
    'https://cdn.discordapp.com/attachments/331827935030018048/362015670030041091/Konachan.com_-_181291_alice_parade_anus_black_hair_blush_green_eyes_inemuri_yamane_itou_noiji_loli_l.jpg',
    'https://cdn.discordapp.com/attachments/331827935030018048/362015683510272001/Konachan.com_-_186160_2girls_ass_bed_blush_breasts_cum_fang_garter_glasses_loli_navel_nipples_origin.jpg',
    'https://cdn.discordapp.com/attachments/331827935030018048/362015701411823616/Konachan.com_-_192657_animal_ears_bell_catgirl_collar_fang_green_hair_loli_long_hair_mvv_navel_nude_.jpg',
    'https://cdn.discordapp.com/attachments/331827935030018048/362015704825987072/Konachan.com_-_193097_aqua_eyes_blush_flat_chest_gray_hair_konpaku_youmu_loli_namamo_nanase_navel_ni.png',
    'https://cdn.discordapp.com/attachments/331827935030018048/362017919414042635/1eb61d80-2f2c-4adf-84e0-74a5298a35b4.jpg',
    'https://cdn.discordapp.com/attachments/331827935030018048/362017921926430720/2ecf8d51-2ca2-461e-a266-0145f604eb74.jpg',
    'https://cdn.discordapp.com/attachments/331827935030018048/362017929232908288/3a19b7c173d61998ca3a628cd3209a59.png',
    'https://cdn.discordapp.com/attachments/331827935030018048/362017932106006548/4a4dde28b1e7915b5a0abcd279e7dd1d.jpeg',
    'https://cdn.discordapp.com/attachments/331827935030018048/362017935780478976/6fbdc8211503c43ee309738b0036eb73.png',
    'https://cdn.discordapp.com/attachments/331827935030018048/362017946580811776/8da1020b2d0c6737dcced9b2112c4650.png',
    'https://cdn.discordapp.com/attachments/331827935030018048/362017947637645323/8f72dc37-0a17-4b77-9166-dd03510bd73a.jpg',
    'https://cdn.discordapp.com/attachments/331827935030018048/362017952322551808/9f1ee1c9bc557768218ae05de95b3500.png',
    'https://cdn.discordapp.com/attachments/331827935030018048/362017958781779968/30b1b22977b258e0a5eea49d2396deda.jpeg',
    'https://cdn.discordapp.com/attachments/331827935030018048/362019786483433473/tumblr_on5gf9L1ZT1sm2fjbo1_1280.png',
    'https://cdn.discordapp.com/attachments/331827935030018048/362019790069563392/tumblr_oot3coeLu31sm2fjbo1_1280.png',
    'https://cdn.discordapp.com/attachments/331827935030018048/362019798013575168/unknown.png',
    'https://cdn.discordapp.com/attachments/331827935030018048/362019797812117514/tumblr_opvjpciSvp1sm2fjbo1_1280.png',
    'https://cdn.discordapp.com/attachments/331827935030018048/362019810898477056/yande.re_378545_animal_ears_anus_ass_breast_grab_bunny_ears_censored_inaba_tewi_kitsunerider_loli_ni.jpg',
    'https://cdn.discordapp.com/attachments/331827935030018048/362019811464839168/yande.re_371508_bug_system_censored_cunnilingus_game_cg_gothic_lolita_koushou_aika_lolita_fashion_ma.png',
    'https://cdn.discordapp.com/attachments/331827935030018048/362019815692435466/yande.re_380386_aida_takanobu_game_cg_naked_nipples_onohara_hazuki_sono_hanabira_ni_kuchizuke_wo_suo.png',
    'https://cdn.discordapp.com/attachments/331827935030018048/362019819559714826/yande.re_383918_anal_anus_bottomless_bra_breast_hold_breasts_dildo_kopianget_megane_naked_nipples_op.jpg',
    'https://cdn.discordapp.com/attachments/331827935030018048/362019852468224000/yande.re_389847_game_cg_k-ko_loli_pantsu_pantyhose_pussy_juice_seguchi_mahiru_skirt_lift_tinkle_posi.png',
    'https://cdn.discordapp.com/attachments/331827935030018048/362019852027953153/yande.re_386873_ass_bondage_bug_system_fingering_game_cg_koushou_aika_marushin_mihama_yomi_naked_nip.png',
    'https://cdn.discordapp.com/attachments/331827935030018048/362021088923746304/6529e06f81946d23ed7bf7775310dad0.jpg',
    'https://cdn.discordapp.com/attachments/331827935030018048/362021093164187660/7279d52eecfcfca95b1f01394b3df0f4.jpeg',
    'https://cdn.discordapp.com/attachments/331827935030018048/362021099300454400/9877a3eb0eb4726cf7642cf1aaf2ad95.jpeg',
    'https://cdn.discordapp.com/attachments/331827935030018048/362021118334205952/2180256b-d859-4402-beae-eed99abab820.jpg',
    'https://cdn.discordapp.com/attachments/331827935030018048/362021120368443394/781707f639299eaaa5b384c32478bb7e.jpeg',
    'https://cdn.discordapp.com/attachments/331827935030018048/362021124118413324/43495068_p0.jpg',
    'https://cdn.discordapp.com/attachments/331827935030018048/362021130267131906/424033c8f5b6de18bb4f5461b040992c.png',
    'https://cdn.discordapp.com/attachments/331827935030018048/362021134692122624/a63ca51e57765b3336a38f819a05272c.jpeg',
    'https://cdn.discordapp.com/attachments/331827935030018048/362021130049159178/47069417d93b8ed815f284afc6e2c23e.jpg',
    'https://cdn.discordapp.com/attachments/331827935030018048/362021138366464001/a434c297-a7df-4cfd-99e4-e98d698809d2.jpg',
    'https://cdn.discordapp.com/attachments/331827935030018048/362025063786217482/FB_IMG_1506090797599.jpg',
    'https://cdn.discordapp.com/attachments/331827935030018048/362025067414159361/FB_IMG_1506090806514.jpg',
    'https://cdn.discordapp.com/attachments/331827935030018048/362025068366397461/FB_IMG_1506090864607.jpg',
    'https://cdn.discordapp.com/attachments/331827935030018048/362025070526201867/FB_IMG_1506090890627.jpg'
    ]

def read_from_db(sq):
    print(sq)
    c.execute(sq)
    conn.commit()
    print(sq)
    global data
    data = c.fetchall()
    print("Sql query sent off!")

@client.command(pass_context = True)
async def hentai(ctx):
    server_id = ctx.message.server.id
    sq = "SELECT COUNT(*), nsfw_is_enabled, server_id FROM Permissions WHERE server_id = '" + server_id + "'"
    read_from_db(sq)
    if data[0][1] < 1:
        embed = discord.Embed(description = "NSFW is disabled!", color = 0xFF0000)
        await client.say(embed = embed)
    elif data[0][1] > 0: 
        embed = discord.Embed(desciption = "Here's your hentai, " + ctx.message.author.mention + "!", color = embed_color)
        embed.set_image(url = random.choice(hentai_images))
        await client.say(embed = embed)
        print(Fore.CYAN + "Command Successfully Executed |\n       Command Ran In:[" + ctx.message.server.id + "]\n       User:[" + ctx.message.author.id + "]\n       Channel:[" + ctx.message.channel.id + "]")


############ FIX THIS ############
def data_entry(sqlstr):
    print(sqlstr)
    c.execute(sqlstr)
    conn.commit()
    print("sql query sent off")

def read_from_db(sqlstr):
    data = [[]]
    print(sqlstr)
    c.execute(sqlstr)
    conn.commit()
    data = c.fetchall()
    print("Sql query sent off!")
    print(data)
    return data

@client.command(pass_context = True, aliases=['dnsfw'])
async def disablensfw(ctx):
    data = 0
    server_id = ctx.message.server.id
    sqlstr = "SELECT CASE WHEN nsfw_is_enabled = '1' THEN '0' WHEN nsfw_is_enabled = '0' THEN '1' END FROM Permissions WHERE server_id = '" + server_id + "'"
    data = read_from_db(sqlstr)
    print(data)
    sql2 = "UPDATE Permissions SET nsfw_is_enabled = '" + data + "' WHERE server_id = '" + server_id + "'"
    print(sql2)
    data_entry(sql2)
    if data == "1":
        await client.say("NSFW is now enabled!")
    else:
        await client.say("NSFW is now disabled!")

############ FIX THIS ############

@client.command(pass_context = True, aliases=['ser'])
async def server(ctx):
    embed = discord.Embed(color = embed_color)
    embed.add_field(name="Owner:", value=ctx.message.server.owner, inline=True)
    embed.add_field(name="AFK Channel:", value=ctx.message.server.afk_channel, inline=True)
    embed.add_field(name="Server Region:", value=ctx.message.server.region, inline=True)
    embed.add_field(name="Features:", value=ctx.message.server.features, inline=True)
    embed.add_field(name="Verification Level:", value=ctx.message.server.verification_level, inline=True)
    embed.add_field(name="Member Count:", value=ctx.message.server.member_count, inline=True)
    embed.add_field(name="Creation:", value=ctx.message.server.created_at, inline=True)
    await client.say(embed = embed)
    print(Fore.CYAN + "Command Successfully Executed |\n       Command Ran In:[" + ctx.message.server.id + "]\n       User:[" + ctx.message.author.id + "]\n       Channel:[" + ctx.message.channel.id + "]")

@client.event
async def on_message(message):
    embed = discord.Embed(color = embed_color)
    embed.set_image(url = "https://cdn.discordapp.com/attachments/331549832382775297/364526022533578752/1457739351_tumblr_nophoixqFH1tlyjpto1_500.gif")
    if message.content.startswith('salty'):
        await client.send_message(message.channel, embed=embed)
    await client.process_commands(message)



'''@client.command(pass_context = True)
async def randomquote(ctx):
    with open("quote_file.pk1", "rb") as quote_file:
        quote_list = pickle.load(quote_file)
        await client.say(ctx.message.author.mention + ", here's your random quote!" + random.choice(quote_list))

@client.command(pass_context = True)
async def addquote(ctx, *, args):
    if not os.path.isfile("quote_file.pk1"):
        await client.say("FIle missing!")
        quote_list = []
        print(Fore.RED + quotefile + " is missing from the directory!")
    else:
        with open("quote_file.pk1", "rb") as quote_file:
            quote_list = pickle.load(quote_file)
        quote_list.append(message.content[9:])
        with open("quote_file.pk1", "rb") as quote_file:
                pickle.dump(quote_list, quote_file)'''

@client.command(pass_context = True)
async def now(ctx):
    date = datetime.datetime.now().strftime("%A, %d.%m.%Y, **%H:%M**") 
    embed = discord.Embed(description = ctx.message.author.mention + ", now is: " + date, color = embed_color)
    await client.say(embed=embed)



### LOGGING ###
'''
@client.event
async def on_message_edit(message, after, channel = loggingchannel):
    embed = discord.Embed(title = "Message Edited!", description = "In channel: <#" + message.channel.id + ">", color = embed_color)
    embed.add_field(name="New Content: ", value=after.content, inline=True)
    embed.add_field(name="Old Content: ", value=message.content, inline=False)
    embed.add_field(name="User: ", value=message.author.name + "#" + message.author.discriminator, inline=False)
    print("Message Edited, New Content: " + after.content)
    await client.send_message(discord.Object(id=loggingchannel), embed = embed)
    await client.process_commands(message)


@client.event
async def on_message_delete(message, channel = loggingchannel):
    embed = discord.Embed(title = "Message Deleted!", description = "In channel: <#" + message.channel.id + ">", color = embed_color)
    embed.add_field(name="Message Content: ", value=message.content, inline=True)
    embed.add_field(name="User: ", value=message.author.name + "#" + message.author.discriminator)
    await client.send_message(discord.Object(id=loggingchannel), embed = embed)
    await client.process_commands(message)


@client.event
async def on_channel_create(message, channel = loggingchannel):
    embed = discord.Embed(title = "New Channel Created!", color = embed_color)
    embed.add_field(name="Channel Name: ", value="%%", inline=True)
    await client.send_message(discord.Object(id=loggingchannel), embed = embed)
    await client.process_commands(message)


@client.event
async def on_channel_delete(message, channel = loggingchannel):
    embed = discord.Embed(title = "Channel Deleted!", color = embed_color)
    embed.add_field(name="Channel Name: ", value="%%", inline=True)
    await client.send_message(discord.Object(id=loggingchannel), embed = embed)
    await client.process_commands(message)


@client.event
async def on_channel_update(message, channel = loggingchannel):
    embed = discord.Embed(title = "Channel Updated!", color = embed_color)
    embed.add_field(name="Channel Name: ", value="%%", inline=True)
    await client.send_message(discord.Object(id=loggingchannel), embed = embed)
    await client.process_commands(channel)


@client.event
async def on_server_role_create(role, channel = loggingchannel):
    embed = discord.Embed(title = "New Role Created!", color = embed_color)
    embed.add_field(name="Role Name: ", value=role.name, inline=True)
    await client.send_message(discord.Object(id=loggingchannel), embed=embed)
    await client.process_commands(role)


@client.event
async def on_server_role_delete(role, channel = loggingchannel):
    embed = discord.Embed(title = "Role Deleted", color = 0xF00000)
    embed.add_field(name="Role Name: ", value=role.name, inline=True)
    await client.send_message(discord.Object(id=loggingchannel), embed=embed)
    await client.process_commands(role)


@client.event
async def on_member_ban(member, channel = loggingchannel):
    embed = discord.Embed(title = "User Banned!", color = 0xF00000)
    embed.add_field(name="User: ", value=member.name + "#" + member.discriminator, inline=True)
    await client.send_message(discord.Object(id=loggingchannel), embed=embed)
    await client.process_commands(member)


@client.event
async def on_member_unban(server, channel = loggingchannel):
    embed = discord.Embed(title = "User Unbanned", color = 0xFF0000)
    await client.send_message(discord.Object(id=loggingchannel), embed=embed)
    await client.process_commands(member)


@client.event
async def on_member_kick(member, channel = loggingchannel):
    embed = discord.Embed(title = "User Kicked!", color = 0xFF0000)
    embed.add_field(name="User: ", value=member.name + "#" + member.discriminator, inline=True)
    await client.send_message(discord.Object(id=loggingchannel), embed=embed)
    await client.process_commands(member)
    '''
### LOGGING ###



### MODULES ###
@client.command(pass_context = True)
async def modules(ctx):
    embed = discord.Embed(title = "Available Modules", description = "-Fun\n-Logging (Requires You to input a channel for logging in `credentials.py`)", color = embed_color)
    await client.say(embed = embed)


@client.command(pass_context = True, aliases=['module-fun'])
async def modulefn(ctx):
    embed = discord.Embed(title = "Commands In Module: Fun", description = ";slotroll\n;flip\n;8ball\n;roll", color = embed_color)
    embed.set_footer(text="To see the usage of a command, do `;h ;command-name`, example: `;h ;8ball`")
    await client.say(embed = embed)
### MODULES ###


def read_from_db(s):
    print(s)
    c.execute(s)
    conn.commit()
    global data
    data = c.fetchall()
    print("SQL Query Sent off! AAAAA")

@client.command(pass_context = True)
async def testt(ctx, *, userid:str):
    s = "SELECT * FROM UserData WHERE user_name = '" + userid + "'"
    read_from_db(s)
    await client.say(data)



###### EXP AND OTHER STUFF ######


## Currency ##
def data_entry(sqlstr2):
    print(sqlstr2)
    c.execute(sqlstr2)
    conn.commit()
    global datta
    datta = c.fetchall()
    print("Sql query sent off!")
    print(datta)

def read_from_db(sqlstr):
    print(sqlstr)
    c.execute(sqlstr)
    conn.commit()
    global data
    data = c.fetchall()
    print("Sql query sent off!")
    print(data)

@client.command(pass_context = True, aliases=['cash', 'currency'])
async def cur(ctx):
    currency = "0"
    user_id = ctx.message.author.id
    sqlstr = "SELECT COUNT(*), user_id, currency FROM Currency WHERE user_id = '" + user_id + "'"
    sqlstr2 = "INSERT INTO Currency (user_id, currency) VALUES ('" + user_id + "', " + currency + ")"
    read_from_db(sqlstr)
    if data[0][0] < 1:
        data_entry(sqlstr2)
        embed = discord.Embed(description = ctx.message.author.mention + ", your current balance is: **" + currency + "**", color = embed_color) 
    else:
        embed = discord.Embed(description = ctx.message.author.mention + ", your current balance is: **" + data[0][2] + "**", color = embed_color) 
    await client.say(embed = embed)


## Hackbans The User By ID ##
def data_entry(hkban):
    print(hkban)
    c.execute(hkban)
    conn.commit()
    global data
    data = c.fetchall()
    print("Sql query sent off!")

@client.command(pass_context = True, aliases=['hb'])
async def hackban(ctx, *, id: str):
    server_id = ctx.message.server.id
    hkban = "INSERT INTO Hackbans (user_id, server_id) VALUES ('" + id + "', '" + server_id + "')"
    print(hkban)
    data_entry(hkban)
    embed = discord.Embed(description = "Successfully Hackbanned: " + id, color = embed_color)
    await client.say("Hackbanned: " + id)


def read_from_db(banonjoin):
    print(banonjoin)
    c.execute(banonjoin)
    conn.commit()
    global datta
    datta = c.fetchall()
    print(datta)
    print("Sql query sent off!")

@client.event
async def on_member_join(member):
    server_id = member.server.id
    user_id = member.id
    banonjoin = "SELECT COUNT(*) FROM Hackbans WHERE user_id = '" + user_id + "' AND server_id = '" + server_id + "'"
    read_from_db(banonjoin)
    print(datta)
    print("A hackbanned member joined and was banned")
    await client.process_commands(message)



## Sets User's level ##
def data_entry(sqll):
    print(sqll)
    c.execute(sqll)
    conn.commit()
    global data
    data = c.fetchall()
    print("Sql query sent off!")


@client.command(pass_context = True, aliases=['setlvl'])
async def setlevel(ctx, user: str, level: str):
    if ctx.message.author.id != owner:
        embed = discord.Embed(desciption = "Not the owner!", color = 0xFF0000)
        await client.say(embed = embed)
    else:
        sqll = "UPDATE UserData SET level = '" + level + "' WHERE user_id = '" + user + "'"
        data_entry(sqll)
        embed = discord.Embed(description = "Change the level of " + user + " to: **" + level + "**", color = embed_color)
        await client.say(embed = embed)


## Gives a reputation point to a user ##
def data_entry(sqll):
    print(sqll)
    c.execute(sqll)
    conn.commit()
    global data
    data = c.fetchall()
    print("Sql query sent off!")


@client.command(pass_context = True, aliases=['rep'])
async def giverep(ctx, user: str, rep: str):
    sqll = "UPDATE UserData SET reputation = '" + rep + "' WHERE user_id = '" + user + "'"
    data_entry(sqll)
    embed = discord.Embed(description = ctx.message.author.mention + ", you gave " + user + ", **" + rep + "**, reputation!", color = embed_color)
    await client.say(embed = embed)


## Updates Description ##
def data_entry(de):
    print(de)
    c.execute(de)
    conn.commit()
    global data
    data = c.fetchall()
    print(Fore.YELLOW + "SQL Query sent off!")

@client.command(pass_context = True, aliases=['setdesc'])
async def setdescription(ctx, *, desc: str):
    user_id = ctx.message.author.id
    de = "UPDATE UserData SET description = '" + desc + "' WHERE user_id = '" + user_id + "'"
    data_entry(de)
    embed = discord.Embed(description = "Updated your description to: **" + desc + "**", color = embed_color)
    await client.say(embed = embed)


## Checks the NSFW status ##
def read_from_db(sqls):
    print(sqls)
    c.execute(sqls)
    conn.commit()
    global data
    data = c.fetchall()
    print("sql query sent off")

@client.command(pass_context = True, aliases=['nsfws'])
async def nsfwstatus(ctx):
    server_id = ctx.message.server.id
    sqls = "SELECT nsfw_is_enabled FROM Permissions WHERE server_id = '" + server_id + "'"
    print(sqls)
    read_from_db(sqls)
    embed = discord.Embed(title = "NSFW Is currently: ", color = embed_color)
    embed.add_field(name="NSFW Status", value=data, inline=True)
    await client.say(embed = embed)


## EXP Stats ##
def read_from_db(getxps):
    print(getxps)
    c.execute(getxps)
    conn.commit()
    global data
    data = c.fetchall()
    print(data)
    print("SQL Query Sent Off!")

def data_entry(st2):
    print(st2)
    c.execute(st2)
    conn.commit()
    global datta
    datta = c.fetchall()
    print(datta)
    print("SQL Query Sent Off!")

@client.command(pass_context =  True, aliases=['prof'])
async def profile(ctx, *, user: str):
    user_id = ctx.message.author.id
    user_name = ctx.message.author.name
    level = "0"
    description = "A very empty description :^)"
    reputation = "0"
    currency = "0"
    avatar = ctx.message.author.avatar_url
    getxp = "SELECT * FROM UserData WHERE user_name = '" + user + "'"
    getxps = "SELECT COUNT(*), user_id, user_name, level, description, reputation, currency, avatar FROM UserData WHERE user_name = '" + user + "'"
    sqlstr2 = "INSERT INTO UserData (user_id, user_name, level, description, reputation, currency, avatar) VALUES ('" + user_id + "', '" + user_name + "', '" + level + "', '" + description + "', '" + reputation + "', '" + currency + "', '" + avatar + "')"
    read_from_db(getxps)
    if data[0][0] < 1:
        data_entry(sqlstr2)
    embed = discord.Embed(title = "EXP stats", color = embed_color)
    embed.set_thumbnail(url = data[0][7])
    embed.add_field(name = "User ID", value=data[0][1], inline=True)
    embed.add_field(name = "User Name", value=data[0][2], inline=True)
    embed.add_field(name="Level", value=data[0][3], inline=True)
    embed.add_field(name="Description", value=data[0][4], inline=True)
    embed.add_field(name="Reputation", value=data[0][5], inline=True)
    embed.add_field(name="Currency", value=data[0][6])
    embed.set_footer(text=ctx.message.author)
    await client.say(embed = embed)
    print("SQL Query completed!")

###### EXP AND DATABASE STUFF ######

'''---------------------------------------------------------------------'''
client.run(BotToken)
