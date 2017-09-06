#Edit the credentials below.
token = ""
owner = ''
embed_color = 0xFFFFF
#Embed color is customizable. Put it like this: 0xYOUR-HEX-CODE

#Do NOT edit past this point!!!#
#---------------------------------------#
#---------------------------------------#
#---------------------------------------#
#---------------------------------------#
#---------------------------------------#
#---------------------------------------#
#---------------------------------------#
#---------------------------------------#
import discord
import asyncio
import random
import time
import requests
from discord.ext.commands import Bot
from discord.ext import commands
import pickle
import os

filename = 'greetmsgs.txt'

if filename in os.listdir(): 
	myfile = open(filename, 'rb')
	messages = pickle.load(myfile)
	del myfile
else:
	messages = {}

Client = discord.Client()
bot_prefix= ";"
client = commands.Bot(command_prefix=bot_prefix)
start_time = time.time()

 
@client.event
async def on_ready():
    print("Bot Logged In, Running")
    print("Name: {}".format(client.user.name))
    print("ID: {}".format(client.user.id))
    print("-------------------------------------")
    await client.change_presence(game=discord.Game(name=''))


@client.command(pass_context = True)
async def send(ctx, member : discord.Member, *, message):
        if ctx.message.author.id != owner: return await client.say(":x: You are not the bot owner")
        if ctx.message.author.id == owner: return await client.send_message(member, message)

@client.command(pass_context = True)
async def h(ctx):
    embed = discord.Embed(description = "**Hosting Guides: https://github.com/Kyousei/YotsugiBot/wiki** \n **Commands List: https://goo.gl/w6Aoag**", color = embed_color)
    await client.say(embed = embed) 

@client.command
async def h(command = None):
    if not command:
        #do normal help command
        return

    #some code to check if the command is an actual command (depends on how you make commands)
    return

 
@client.command()
async def ping():
    pingtime = time.time()
    pingms = await client.say("Pinging...")
    ping = time.time() - pingtime
    await client.edit_message(pingms, "Pong! :ping_pong:  The ping time is `%.01f seconds`" % ping)
 
#command1
@client.command(pass_context = True)
async def invite(ctx):
    embed = discord.Embed(title = "Here are invite links:", description = "Invite me to your server with this link: https://discordapp.com/oauth2/authorize?client_id=331766751765331969&scope=bot&permissions=66186303", color = embed_color)
    return await client.say(embed = embed)
 
#command2
@client.command(pass_context = True, no_pm = True)
async def banlist(ctx):
    x = await client.get_bans(ctx.message.server)
    x = '\n'.join([y.name for y in x])
    embed = discord.Embed(title = "List of Banned Members", description = x, color = embed_color)
    return await client.say(embed = embed)
 
#command3
@client.command(pass_context=True, no_pm = True)
async def connect(ctx):
    if client.is_voice_connected(ctx.message.server):
        return await client.say("I am already connected to a voice channel. Do not disconnect me if I am in use!")
    author = ctx.message.author
    voice_channel = author.voice_channel
    vc = await client.join_voice_channel(voice_channel)
 
#command4
@client.command(pass_context = True, no_pm = True)
async def disconnect(ctx):
    for x in client.voice_clients:
        if(x.server == ctx.message.server):
            return await x.disconnect()
        
#command6
@client.command(pass_context=True, no_pm = True)       
async def clear(ctx, number):
    embed = discord.Embed(description = ":x: Insufficient permissions! You require **Manage Messages** permission in order to clear messages!", color = 0xF00000)
    if not ctx.message.author.server_permissions.manage_messages:
        return await client.say(embed = embed)
    mgs = []
    number = int(number) #Converting the amount of messages to delete to an integer
    async for x in client.logs_from(ctx.message.channel, limit = number):
        mgs.append(x)
    await client.delete_messages(mgs)

bot_version = 'v0.4.4'
#command8
bot_author = 'Kyousei#8357'
@client.command(pass_context = True, no_pm = True)
async def author(ctx):
    embed = discord.Embed(title = "Yotsugi Bot Author:", description = "Name: **" + bot_author + "**  \n  Joined Discord: **07.02.2016  1:10 PM**  \n  **ID**: 145878866429345792  \n  **Email**: yotsugibot@gmail.com  \n  Say **;h** for commands.", color = embed_color)
    return await client.say(embed = embed)

#command9
@client.command(pass_context = True, no_pm = True)
async def ban(ctx, *, member : discord.Member = None):
    if not ctx.message.author.server_permissions.ban_members:
        return

    if not member:
        embed = discord.Embed(description = ctx.message.author.mention + ", you did not specify a user to ban! :x:", color = 0xF00000)
        return await client.say(embed = embed)
    try:
        await client.ban(member)
    except Exception as e:
        if 'Privilege is too low' in str(e):
            embed = discord.Embed(description = "Privilege is too low. :x:", color = 0xF00000)
            return await client.say(embed = embed)

    embed = discord.Embed(description = "**%s** has been banned."%member.name, color = 0xF00000)
    return await client.say(embed = embed)
	
#command10
@client.command(pass_context = True, no_pm = True)
async def kick(ctx, *, member : discord.Member = None):
    if not ctx.message.author.server_permissions.kick_members:
        return

    if not member:
        return await client.say(ctx.message.author.mention + "Specify a user to kick!")
    try:
        await client.kick(member)
    except Exception as e:
        if 'Privilege is too low' in str(e):
            embed = discord.Embed(description = "Privilege is too low. :x:", color = 0xF00000)
            return await client.say(embed = embed)

    embed = discord.Embed(description = "**%s** has been kicked."%member.name, color = 0xF00000)
    return await client.say(embed = embed)
	
#command12
@client.command(pass_context = True, no_pm = True)
async def mute(ctx, *, member : discord.Member):
    if not ctx.message.author.server_permissions.mute_members:
        return
    overwrite = discord.PermissionOverwrite()
    overwrite.send_messages = False
    await client.edit_channel_permissions(ctx.message.channel, member, overwrite)
    await client.say("**%s** has been muted!"%member.mention)

#command13
@client.command(pass_context = True, description='Unmutes the muted members.', no_pm = True)
async def unmute(ctx, *, member : discord.Member):
    if not ctx.message.author.server_permissions.mute_members:
        return
    overwrite = discord.PermissionOverwrite()
    overwrite.send_messages = True
    await client.edit_channel_permissions(ctx.message.channel, member, overwrite)
    await client.say("**%s** has been unmuted!"%member.mention)

#command14
answers = ["My source say no.", "I completely disagree.", "No way in hell!", "Sure! :D", "Why not?", "Why would you say that?", "When life gives you lemons, throw them at people!", "HA, You wish!", "Keep dreaming!", "Does a green light mean go?", "Red is supposed to stop you, but your magic is TOO strong! :sweat:", "Power outage!??! WHAT ABOUT MY WIFI!??!!", "Hmmm.. this is hard", "lol, just lol.", "Cleverbot is no match for me! Haahahaha", "The chances of that happening are equal to the chances of shivaco getting a girlfriend. Null!", "There's an admin watching :scream:", "Ask me tomorrow :zzz:", "No... I mean yes... Well... Ask again later"]

@client.command(description='Decides for you.')
async def eightball(*choices):
    if len(choices) == 0:
        return await client.say("Ask me a yes or no question.")
    embed = discord.Embed(description = random.choice(answers), color = embed_color)
    await client.say(embed = embed)


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
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    embed = discord.Embed(description = result, color = embed_color)
    await client.say(embed = embed)


#command17
@client.command()
async def github():
    """  ---Link to Github"""
    embed = discord.Embed(description = "Yotsugi Github can be found here: https://github.com/YotsugiBot", color = embed_color)
    await client.say(embed = embed)


#command18
@client.command(pass_context = True, no_pm = True)
async def servers(ctx):
    x = '\n'.join([str(server) for server in client.servers])
    print(x)
    embed = discord.Embed(title = "Servers", description = x, color = embed_color)
    return await client.say(embed = embed)

#command19
@client.command(pass_context = True, no_pm = True)
async def setgreet(ctx):
    global messages
    greet_message = ctx.message.content
    messages[ctx.message.server] = greet_message
    with open(filename, 'wb') as myfile:
            pickle.dump(messages, myfile)


@client.command(no_pm = False)
async def stats():
    second = time.time() - start_time
    minute, second = divmod(second, 60)
    hour, minute = divmod(minute, 60)
    day, hour = divmod(hour, 24)
    week, day = divmod(day, 7)
    embed = discord.Embed(title = "Yotsugi **" + bot_version + "**", description = "**Author: **" + bot_author + " \n\n\n **Uptime:** \n **%d** weeks, \n **%d** days, \n **%d** hours, \n **%d** minutes, \n **%d** seconds"% (week, day, hour, minute, second), color = embed_color)
    await client.say(embed = embed)


@client.command(pass_context=True, no_pm=True)
async def shutdown(ctx):
    if owner == ctx.message.author.id:
        embed = discord.Embed(description = "Shutting Down...", color = embed_color)
        await client.say(embed = embed)
        await client.logout()
        

@client.command(pass_context = True, no_pm = True)
async def serverid(ctx, *, member = discord.Member):
    embed = discord.Embed(description = ctx.message.author.mention + ", ID of this server is:** " + ctx.message.channel.server.id + "**", color = embed_color)
    await client.say(embed = embed)

@client.command(pass_context = True, no_pm = True)
async def channelid(ctx):
    embed = discord.Embed(description = ctx.message.author.mention + ", ID of this channel is:** " + ctx.message.channel.id + "**", color = embed_color)
    await client.say(embed = embed)


@client.command(pass_context=True, no_pm=True)
async def removerole(ctx, user: discord.Member, *, role):
    if ctx.message.author.server_permissions.manage_roles:
        await client.remove_roles(user, discord.utils.get(ctx.message.server.roles, name=role))
        embed = discord.Embed(description = ("Removed %s from **%s**" % (user.mention, role)), color = embed_color)
        await client.say(embed = embed)
    else:
        embed = discord.Embed(description = ":x: Insufficient permissions!", color = 0xFF0000)
        return await client.say(embed = embed)


@client.command(pass_context=True, no_pm=True)
async def setrole(ctx, user: discord.Member, *, role):
    if ctx.message.author.server_permissions.manage_roles:
        await client.add_roles(user, discord.utils.get(ctx.message.server.roles, name=role))
        embed = discord.Embed(description = ("Added %s to  **%s**" % (user.mention, role)), color = embed_color)
        await client.say(embed = embed)
    else:
        embed = discord.Embed(description = ":x: Insufficient permissions!", color = 0xFF0000)
        return await client.say(embed = embed)

'''@client.event
async def on_message(message):
    if message.content.startswith(";h ;ban"):
            embed = discord.Embed(title = ";ban", description = "Bans the mentioned users. \n**Requires *Ban Members* permission**\n\n `Usage: ` ;ban @user", color = embed_color)
            await client.send_message(message.channel, embed = embed)'''

@client.command(pass_context = True, no_pm = True)
async def warn(ctx, member : discord.Member, *, message):
        if ctx.message.author.id != owner:
                return print("User **" + ctx.message.author.id + "** tried to use :warn in **" + ctx.message.channel.server.id + "**! It did NOT work because they are not the owner")
        if ctx.message.author.id == owner:
                embed = discord.Embed(description = "You've been warned for: **" + message + "**\n Responsible Moderator: **" + ctx.message.author.mention + "**\nServer: **" + ctx.message.server.name + "**", color = 0xFF0000)
                return await client.send_message(member, embed = embed)


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



@client.command(pass_context = True)
async def setgame(ctx, *, game : str):
        if owner != ctx.message.author.id:
            return await client.say(embed=embeds.permission_denied("You aren't the bot owner!"), color = 0xFF0000)
        else:
            try:
                await client.change_presence(game=discord.Game(name=game), status=ctx.message.server.me.status)
                logging.info("Set game to " + str(game))
            except Exception as e:
                print("Failed to set game: {}".format(str(e)) + "\nIgnore this error. It's Python who's being an ass.\nPlease report this on github, https://github.com/Kyousei/YotsugiBot/issues")
    


'''---------------------------------------------------------------------'''

client.run(token)
