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

Client = discord.Client()
bot_prefix= ";"
client = commands.Bot(command_prefix=bot_prefix)

@client.before_invoke
async def before_any_command(ctx):
     blacklist = ["id-here"]
     if ctx.message.author.id is in blacklist:
     return await.ctx.author.send("Failed to execute the command! You've been blacklisted.")
     pass

@client.event
async def on_ready():
    print("ID: {}".format(client.user.id))

@client.command(pass_context=True)
async def ping(ctx):
    await client.say("Pong!")

@client.command(pass_context = True)
async def dm(ctx, member : discord.Member, *, message):
     #owner = '14587886429345792'
    if owner == ctx.message.author.id:
    return await client.send_message(member, message)
elif:
     await client.say("You can't use this command! Ask for help in Yotsugi Support Server, links in `;stats`. *Ask for help if You REALLY need it.")

@client.command()
async def info(ctx, *, member: discord.Member):
"""User Information"""
fmt = '{0} joined on {0.joined_at} and has {1} roles.'
await ctx.send(fmt.format(member, len(member.roles)))

@info.error
async def info_error(ctx, error):
if isinstance(error, commands.BadArgument):
await ctx.send("No user found")

@client.command()
async def roles(ctx, *, member: MemberRoles):
"""Shows a list of roles."""
await ctx.send("The user has: " + ",".join(member))

@client.command(pass_context = True)
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

@client.command(pass_context = True)
async def ban(ctx, *, member : discord.Member = None):
    '''Unbans A User From The Server'''
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

@client.command(pass_context=True)
async def announce(args):
        """Sends a message to all servers the bot is in."""
     #owner = '14587886429345792'
     if owner == ctx.message.author.id: 
     for s in bot.servers:
            await client.send_message(args)

@client.command()
async def uptime():
    second = time.time() - start_time
    minute, second = divmod(second, 60)
    hour, minute = divmod(minute, 60)
    day, hour = divmod(hour, 24)
    week, day = divmod(day, 7)
    embed = discord.Embed(title = "Yotsugi Bot's Uptime", description = "Uptime: %d weeks %d days %d houes %d minutes %d seconds" % (week, day, hour, minute, second))
    await client.say(embed = embed)
    

@client.command(pass_context = True, Hidden = True)
async def shutdown(ctx):
"""Quits the bot"""
    #owner = '14587886429345792'
    if owner == ctx.message.author.id:
        for server in client.servers:
            await client.send_message(server, "Shutting Down")
        await client.logout()
        exit()


client.run(token)
