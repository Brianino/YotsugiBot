#Edit the credentials below
#Need help? Join https://discord.gg/Fj97uwmT
token = ""
bot_version = 'v0.4'
owner = ''


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
    await client.change_presence(game=discord.Game(name='say ;h'))


@client.command(pass_context = True)
async def send(ctx, member : discord.Member, *, message):
    return await client.send_message(member, message)

@client.command(pass_context = True)
async def h(ctx):
    embed = discord.Embed(description = "**Hosting Guides: https://github.com/Kyousei/YotsugiBot/wiki** \n **Commands List: https://goo.gl/w6Aoag**", color = 0xFFFF)
    embed.set_thumbnail(url = "https://cdn.discordapp.com/attachments/328351969611874305/352587892645822464/YotsugiPfp.png")
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
    embed = discord.Embed(title = "Here are invite links:", description = "Invite me to your server with this link: https://discordapp.com/oauth2/authorize?client_id=331766751765331969&scope=bot&permissions=66186303", color = 0xFFFFF)
    return await client.say(embed = embed)
 
#command2
@client.command(pass_context = True)
async def banlist(ctx):
    x = await client.get_bans(ctx.message.server)
    x = '\n'.join([y.name for y in x])
    embed = discord.Embed(title = "List of Banned Members", description = x, color = 0xFFFFF)
    return await client.say(embed = embed)
 
#command3
@client.command(pass_context=True)
async def connect(ctx):
    if client.is_voice_connected(ctx.message.server):
        return await client.say("I am already connected to a voice channel. Do not disconnect me if I am in use!")
    author = ctx.message.author
    voice_channel = author.voice_channel
    vc = await client.join_voice_channel(voice_channel)
 
#command4
@client.command(pass_context = True)
async def disconnect(ctx):
    for x in client.voice_clients:
        if(x.server == ctx.message.server):
            return await x.disconnect()
        
#command6
@client.command(pass_context=True)       
async def clear(ctx, number):
    mgs = []
    number = int(number) #Converting the amount of messages to delete to an integer
    async for x in client.logs_from(ctx.message.channel, limit = number):
        mgs.append(x)
    await client.delete_messages(mgs)
	
#command8
bot_author = 'Kyousei#8357'
@client.command(pass_context = True)
async def author(ctx):
    embed = discord.Embed(title = "Yotsugi Bot Author:", description = "Name: **" + bot_author + "**  \n  Joined Discord: **07.02.2016  1:10 PM**  \n  **ID**: 145878866429345792  \n  **Email**: yotsugibot@gmail.com  \n  Say **;h** for commands.", color = 0xFFFFF)
    return await client.say(embed = embed)

#command9
@client.command(pass_context = True)
async def ban(ctx, *, member : discord.Member = None):
    if not ctx.message.author.server_permissions.administrator:
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
@client.command(pass_context = True)
async def kick(ctx, *, member : discord.Member = None):
    if not ctx.message.author.server_permissions.administrator:
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
@client.command(pass_context = True)
async def mute(ctx, *, member : discord.Member):
    if not ctx.message.author.server_permissions.administrator:
        return
    overwrite = discord.PermissionOverwrite()
    overwrite.send_messages = False
    await client.edit_channel_permissions(ctx.message.channel, member, overwrite)
    await client.say("**%s** has been muted!"%member.mention)

#command13
@client.command(pass_context = True, description='Unmutes the muted members.')
async def unmute(ctx, *, member : discord.Member):
    if not ctx.message.author.server_permissions.administrator:
        return
    overwrite = discord.PermissionOverwrite()
    overwrite.send_messages = True
    await client.edit_channel_permissions(ctx.message.channel, member, overwrite)
    await client.say("**%s** has been unmuted!"%member.mention)

#command14
answers = ["My source say no.", "I completely disagree.", "No way in hell!", "Sure! :D", "Why not?", "Why would you say that?", "When life gives you lemons, throw them at people!"]

@client.command(description='Decides for you.')
async def eightball(*choices):
    if len(choices) == 0:
        return await client.say("Give me a proper question.")

    await client.say(random.choice(answers))


#command16
@client.command()
async def roll(dice : str):
    """--- Rolled with NdN format. Example: 5d3"""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await client.say('Format has to be in NdN!')
        return
    if (rolls > 100) or (limit > 100):
        await client.say(":x: You cannot roll more than 100.")
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await client.say(result)


#command17
@client.command()
async def github():
    """  ---Link to Github"""
    embed = discord.Embed(description = "Yotsugi Github can be found here: https://github.com/YotsugiBot", color = 0xFFFFF)
    embed.set_thumbnail(url = "https://cdn.discordapp.com/attachments/328351969611874305/352587892645822464/YotsugiPfp.png")
    await client.say(embed = embed)


#command18
@client.command(pass_context = True)
async def servers(ctx):
    x = '\n'.join([str(server) for server in client.servers])
    print(x)
    embed = discord.Embed(title = "Servers", description = x, color = 0xFFFFF)
    return await client.say(embed = embed)

#command19
@client.command(pass_context = True)
async def setgreet(ctx):
    global messages
    greet_message = ctx.message.content
    messages[ctx.message.server] = greet_message
    with open(filename, 'wb') as myfile:
            pickle.dump(messages, myfile)


@client.command(no_pm = True)
async def stats():
    second = time.time() - start_time
    minute, second = divmod(second, 60)
    hour, minute = divmod(minute, 60)
    day, hour = divmod(hour, 24)
    week, day = divmod(day, 7)
    embed = discord.Embed(title = "Yotsugi **" + bot_version + "**", description = "**Yotsugi Emote:** <:YotsugiHeadTilt:332840281525452800> \n\n\n **Author: **" + bot_author + " \n\n\n **Uptime:** \n **%d** weeks, \n **%d** days, \n **%d** hours, \n **%d** minutes, \n **%d** seconds"% (week, day, hour, minute, second), color = 0xFFFF)
    embed.set_thumbnail(url = "https://cdn.discordapp.com/attachments/328351969611874305/352587892645822464/YotsugiPfp.png")
    await client.say(embed = embed)


@client.command(pass_context=True, no_pm=True)
async def shutdown(ctx):
    if owner== ctx.message.author.id:
        embed = discord.Embed(description = "Shutting Down...", color = 0xFFFF)
        await client.say(embed = embed)
        await client.logout()
        
@client.command(pass_context = True, no_pm = True)
async def warn(ctx, member : discord.Member, *, message):
    await client.send_message(member, "You've been muted for: " + message + ", Time Left: ")

@client.command(pass_context = True, no_pm = True)
async def serverid(ctx):
    embed = discord.Embed(description = ctx.message.author.mention + "**, ID Of this server/guild is: " + ctx.message.channel.server.id + "**", color = 0xFFFFF)
    await client.say(embed = embed)

@client.command(pass_context = True, no_pm = True)
async def channelid(ctx):
    embed = discord.Embed(description = ctx.message.author.mention + "**, ID of this channel is:** " + ctx.message.channel.id, color = 0xFFFFF)
    await client.say(embed = embed)


'''---------------------------------------------------------------------'''

client.run(token)
