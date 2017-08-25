#Main File
#Insert Bot Token in the line below.
token = ""
#Insert your ID in the line below.
owner = ''




#No need to edit this line below.
bot_version = "v0.2"




#Don't edit from this point, unless you know what you're doing.
"""-------------------------------------------------------------"""
import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import json
import os
#import pickle

Client = discord.Client()
bot_prefix= ";"
client = commands.Bot(command_prefix=bot_prefix)

'''@client.before_invoke
@client.remove_command("help")
async def before_any_command(ctx):
     """-------Monitor This--------"""
     blacklist = json.load('blacklist.json')
     if ctx.message.author.id is in blacklist:
     return await.ctx.author.send("Failed to execute the command! You've been blacklisted.")
     pass'''

@client.event
async def on_ready():
    print("ID: {}".format(client.user.id))
    await client.change_presence(game=discord.Game(name='say ;help'))

@client.command()
async def ping():
    pingtime = time.time()
    pingms = await client.say("Pinging...")
    ping = time.time() - pingtime
    await client.edit_message(pingms, "Pong! :ping_pong:  The ping time is `%.01f seconds`" % ping)

@client.command(pass_context = True, no_pm = True)
async def dm(ctx, member : discord.Member, *, message):
     #owner = '14587886429345792'
    if owner == ctx.message.author.id:
    return await client.send_message(member, message)
elif:
     await client.say("You can't use this command! Ask for help in Yotsugi Support Server, links in `;stats`. *Ask for help if You REALLY need it.")

@client.command(no_pm = True)
async def info(ctx, *, member: discord.Member):
"""User Information"""
fmt = '{0} joined on {0.joined_at} and has {1} roles.'
await ctx.send(fmt.format(member, len(member.roles)))

@info.error
async def info_error(ctx, error):
if isinstance(error, commands.BadArgument):
await ctx.send("No user found")

'''@client.command(no_pm = True)
async def roles(ctx, *, member: MemberRoles):
await ctx.send("The user has: " + ",".join(member))'''

@client.command(pass_context = True)
async def h(ctx):
     embed = discord.Embed(description = "For the list of commands, click at this link: https://goo.gl/w6Aoag", color = 0xFFFFF)
     await client.say(embed = embed)


@client.command(pass_context = True)
async def invite(ctx):
    embed = discord.Embed(title = "Here are invite links:", description = "Invite me to your server with this link: https://discordapp.com/oauth2/authorize?client_id=331766751765331969&scope=bot&permissions=0", color = 0xFFFFF)
    return await client.say(embed = embed)
 

@client.command(pass_context = True)
async def banlist(ctx):
    x = await client.get_bans(ctx.message.server)
    x = '\n'.join([y.name for y in x])
    embed = discord.Embed(title = "List of Banned Members", description = x, color = 0xFFFFF)
    return await client.say(embed = embed)
 

@client.command(pass_context=True)
async def connect(ctx):
    if client.is_voice_connected(ctx.message.server):
        return await client.say("I am already connected to a voice channel. Do not disconnect me if I am in use!")
    author = ctx.message.author
    voice_channel = author.voice_channel
    vc = await client.join_voice_channel(voice_channel)
 

@client.command(pass_context = True)
async def disconnect(ctx):
    for x in client.voice_clients:
        if(x.server == ctx.message.server):
            return await x.disconnect()
     
 

@client.command(pass_context=True)       
async def clear(ctx, number):
    mgs = []
    number = int(number) #Converting the amount of messages to delete to an integer
    async for x in client.logs_from(ctx.message.channel, limit = number):
        mgs.append(x)
    await client.delete_messages(mgs)
	

@client.command(pass_context = True)
async def stats(ctx):
    embed = discord.Embed(title = "Yotsugi Bot Stats:", description = "Author: Kyousei#8357  |  Version: v0.2  |  Support Server: https://discord.gg/Fj9uwmT  |  Say ;h for commands.", color = 0xFFFFF)
    embed.set_thumbnail(url = "http://i.imgur.com/Ow0oWwI.png")
    return await client.say(embed = embed)
	

bot_author = "Kyousei#8357"
@client.command(pass_context = True)
async def author(ctx):
    embed = discord.Embed(title = "Yotsugi Bot Author:", description = "Name: " + bot_author "  |  Joined Discord: 07.02.2016  1:10 PM  |  ID: 145878866429345792  |  Email: yotsugibot@gmail.com  |  Say ;h for commands.", color = 0xFFFFF)
    return await client.say(embed = embed)


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



@client.command()
async def roll(dice : str):
    """--- Rolled with NdN format. Example: 5d3"""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await client.say('Format has to be in NdN!')
        return
    if (rolls > 100) or (limit > 100):
	embed = discord.Embed(description = ":x: You can't roll more than 100")
        await client.say(embed = embed)
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await client.say(result)



@client.command()
async def github():
    """  ---Link to Github"""
    embed = discord.Embed(description = "Yotsugi Github can be found here: https://github.com/YotsugiBot", color = 0xFFFFF)
    embed.set_thumbnail(url = "http://i.imgur.com/Ow0oWwI.png")
    await client.say(embed = embed)

     

@client.command(pass_context = True)
async def servers(ctx):
    x = '\n'.join([str(server) for server in client.servers])
    embed = discord.Embed(title = "Servers", description = x, color = 0xFFFFF)
    return await client.say(embed = embed)


@client.command(pass_context=True)
async def shitpost(ctx):
    await client.say("http://i.imgur.com/NB1EpSm.png | GitHub Link: https://github.com/YotsugiBot/suggest-things/issues/1")


@client.command(pass_context = True)
async def mute(ctx, *, member : discord.Member):
    if not ctx.message.author.server_permissions.administrator:
        return
    overwrite = discord.PermissionOverwrite()
    overwrite.send_messages = False
    await client.edit_channel_permissions(ctx.message.channel, member, overwrite)
    await client.say("**%s** has been muted!"%member.mention)


@client.command(pass_context = True, description='Unmutes the muted members.')
async def unmute(ctx, *, member : discord.Member):
    if not ctx.message.author.server_permissions.administrator:
        return
    overwrite = discord.PermissionOverwrite()
    overwrite.send_messages = True
    await client.edit_channel_permissions(ctx.message.channel, member, overwrite)
    await client.say("**%s** has been unmuted!"%member.mention)

    
answers = ["My source say no.", "I completely disagree.", "No way in hell!", "Sure! :D", "Why not?", "Why would you say that?", "When life gives you lemons, throw them at people!","Highly doubtful!","Not in a million years!!!","That sounds interesting!")

@client.command(description='Decides for you.')
async def eightball(*choices):
    if len(choices) == 0:
        return await client.say("Give me a proper question.")

    await client.say(random.choice(answers))

@client.command(pass_context = True, no_pm = True)
async def unban(ctx, *, member : discord.Member = None):
    '''Unbans A User From The Server'''
    if not ctx.message.author.server_permissions.administrator:
        return
 
    if not member:
        return await client.say(ctx.message.author.mention + "Specify a user to Unban!")
    try:
        await client.unban(member)
    except Exception as e:
        if 'Privilege is too low' in str(e):
            return await client.say("Privilege too low :x:")
        embed = discord.Embed(description = "**%s** has been Unbanned!!"%member.name, color = 0xFF0000)

@client.command(pass_context = True, no_pm = True)
async def ban(ctx, *, member : discord.Member = None):
    '''Bans A User From The Server'''
    if not ctx.message.author.server_permissions.administrator:
        return
 
    if not member:
        return await client.say(ctx.message.author.mention + "Specify a user to Unban!")
    try:
        await client.ban(member)
    except Exception as e:
        if 'Privilege is too low' in str(e):
            return await client.say("Privilege too low :x:")

        embed = discord.Embed(description = "**%s** has been banned!!"%member.name, color = 0xF00000)

@client.command(pass_context=True, no_pm = True)
async def announce(args):
        """Sends a message to all servers the bot is in."""
     #owner = '14587886429345792'
     if owner == ctx.message.author.id: 
     for s in bot.servers:
            await client.send_message(args)

@client.command(no_pm = True)
async def uptime():
    second = time.time() - start_time
    minute, second = divmod(second, 60)
    hour, minute = divmod(minute, 60)
    day, hour = divmod(hour, 24)
    week, day = divmod(day, 7)
    embed = discord.Embed(title = "Yotsugi Bot's Uptime", description = "Uptime: %d weeks %d days %d houes %d minutes %d seconds" % (week, day, hour, minute, second))
    await client.say(embed = embed)
    

@client.command(pass_context = True, Hidden = True, no_pm = True)
async def shutdown(ctx):
"""Quits the bot"""
    #owner = '14587886429345792'
    if owner == ctx.message.author.id:
        for server in client.servers:
            await client.send_message(server, "Shutting Down")
        await client.logout()
        exit()


client.run(token)
