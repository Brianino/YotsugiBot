
#Do NOT edit past this point, unless you know what you're doing!#
#---------------------------------------------------------------------------------------------------------------------#
import discord
import asyncio
import random
import time
import requests
from discord.ext.commands import Bot
from discord.ext import commands
import pickle
import os
from credentials import BotToken
from credentials import Owners as owner
from credentials import EmbedColor as embed_color
from credentials import Prefix as prefix
###
bot_version = 'v0.5.3'
bot_author = 'Kyousei#8357'
bot_author_id = '145878866429345792'
###
Client = discord.Client()
bot_prefix= prefix
client = commands.Bot(command_prefix=bot_prefix)
start_time = time.time()

 
@client.event
async def on_ready():
    print("Logging In...")
    time.sleep(4)
    print("Checking files..")
    time.sleep(2)
    print("Logged In | Client Credentials")
    print("\n       Client Name: {}".format(client.user.name) +"\n       Client ID: {}".format(client.user.id) + "\n       Prefix: {}".format(prefix) + "\n       Embed Color: {}".format(embed_color) + "\n       Version: {}".format(bot_version) + "\n       Owner ID: {}".format(owner))
    await client.change_presence(game=discord.Game(name=''))


@client.command(pass_context = True, no_pm = True)
async def send(ctx, member : discord.Member, *, message):
        if ctx.message.author.server_permissions.ban_members:
            return await client.send_message(member, embed=discord.Embed(description="Message from **" + ctx.message.author.mention + "**: " + message, color = embed_color))
            print("Command Successfully Executed |\n       Command Ran In:[" + ctx.message.server.id + "]\n       User:[" + ctx.message.author.id + "]\n       Channel:[" + ctx.message.channel.id + "]")
        else:
            return await client.say(":x: Insufficient permissions!")
            print("Command Failed To |\n       Command Ran In:[" + ctx.message.server.id + "]\n       User:[" + ctx.message.author.id + "]\n       Channel:[" + ctx.message.channel.id + "]\nReason: " + Fore.YELLOW + "Insufficient Permissions! Both user and bot need Ban Members permission!")


@client.command
async def h(command = None):
    if not command:
        #do normal help command
        return

    #some code to check if the command is an actual command (depends on how you make commands)
    return

 
@client.command(pass_context = True)
async def ping(ctx):
    pingtime = time.time()
    pingms = await client.say("Pinging...")
    ping = time.time() - pingtime
    await client.edit_message(pingms, "Pong! :ping_pong:  The ping time is `%.1f ms`" % ping)
    print(Fore.CYAN + "Command Successfully Executed |\n       Command Ran In:[" + ctx.message.server.id + "]\n       User:[" + ctx.message.author.id + "]\n       Channel:[" + ctx.message.channel.id + "]")
 
#command1
@client.command(pass_context = True)
async def invite(ctx):
    embed = discord.Embed(title = "Here are invite links:", description = "Invite me to your server with this link: https://discordapp.com/oauth2/authorize?client_id=331766751765331969&scope=bot&permissions=66186303", color = embed_color)
    return await client.say(embed = embed)
    print(Fore.CYAN + "Command Successfully Executed |\n       Command Ran In:[" + ctx.message.server.id + "]\n       User:[" + ctx.message.author.id + "]\n       Channel:[" + ctx.message.channel.id + "]")
 
#command2
@client.command(pass_context = True, no_pm = True)
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
        
#command6
@client.command(pass_context=True, no_pm = True, aliases=['prune', 'purge'])       
async def clear(ctx, number):
    embed = discord.Embed(description = ":x: Insufficient permissions! You require **Manage Messages** permission in order to clear messages!", color = 0xF00000)
    if not ctx.message.author.server_permissions.manage_messages:
        return await client.say(embed = embed)
        print(Fore.CYAN + "Command Failed To Execute |\n       Command Ran In:[" + ctx.message.server.id + "]\n       User:[" + ctx.message.author.id + "]\n       Channel:[" + ctx.message.channel.id + "]\n       Reason: " + Fore.YELLOW  + "Insufficient Permissions! Both user and bot need Manage Messages permission!")
    mgs = []
    number = int(number) #Converting the amount of messages to delete to an integer
    async for x in client.logs_from(ctx.message.channel, limit = number):
        mgs.append(x)
    await client.delete_messages(mgs)
    print(Fore.CYAN + "Command Successfully Executed |\n       Command Ran In:[" + ctx.message.server.id + "]\n       User:[" + ctx.message.author.id + "]\n       Channel:[" + ctx.message.channel.id + "]")


#command8
@client.command(pass_context = True, no_pm = True)
async def author(ctx):
    embed = discord.Embed(title = "Yotsugi Bot Author:", description = "Name: **" + bot_author + "**  \nJoined Discord: **07.02.2016  1:10 PM**  \n  **ID**: 145878866429345792  \n**Email**: yotsugibot@gmail.com  \nSay **;h** for commands.", color = embed_color)
    return await client.say(embed = embed)
    print(Fore.CYAN + "Command Successfully Executed |\n       Command Ran In:[" + ctx.message.server.id + "]\n       User:[" + ctx.message.author.id + "]\n       Channel:[" + ctx.message.channel.id + "]")

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
    except Exception as e:
        if 'Privilege is too low' in str(e):
            embed = discord.Embed(description = "Privilege is too low. :x:", color = 0xF00000)
            return await client.say(embed = embed)
            print(Fore.RED + "Command Failed To Execute |\n       Command Ran In:[" + ctx.message.server.id + "]\n       User:[" + ctx.message.author.id + "]\n       Channel:[" + ctx.message.channel.id + "]\n       Reason: " + Fore.YELLOW + "Insufficient Permissions! Both user and bot need Ban Members permission!")

    embed = discord.Embed(description = "**%s** has been banned."%member.name, color = 0xF00000)
    return await client.say(embed = embed)
    print(Fore.CYAN + "Command Successfully Executed |\n       Command Ran In:[" + ctx.message.server.id + "]\n       User:[" + ctx.message.author.id + "]\n       Channel:[" + ctx.message.channel.id + "]")


#command10
@client.command(pass_context = True, no_pm = True, aliases=['k'])
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
            print(Fore.RED + "Command Failed To Execute |\n       Command Ran In:[" + ctx.message.server.id + "]\n       User:[" + ctx.message.author.id + "]\n       Channel:[" + ctx.message.channel.id + "]\n       Reason: " + Fore.YELLOW + "Inusfficient Permissions! Both user and bot need Kick Members permission!")

    embed = discord.Embed(description = "**%s** has been kicked."%member.name, color = 0xF00000)
    return await client.say(embed = embed)
    print(Fore.CYAN + "Command Successfully Executed |\n       Command Ran In:[" + ctx.message.server.id + "]\n       User:[" + ctx.message.author.id + "]\n       Channel:[" + ctx.message.channel.id + "]")
	
#command12
@client.command(pass_context = True, no_pm = True)
async def mute(ctx, *, member : discord.Member):
    if not ctx.message.author.server_permissions.mute_members:
        return print(Fore.RED + "Command Failed To Execute |\n       Command Ran In:[" + ctx.message.server.id + "]\n       User:[" + ctx.message.author.id + "]\n       Channel:[" + ctx.message.channel.id + "]\n       Reason: " + Fore.YELLOW + "Insufficient Permissions! Both user and member need Mute Members permission!")
    overwrite = discord.PermissionOverwrite()
    overwrite.send_messages = False
    await client.edit_channel_permissions(ctx.message.channel, member, overwrite)
    await client.say("**%s** has been muted!"%member.mention)
    print(Fore.CYAN + "Command Successfully Executed |\n       Command Ran In:[" + ctx.message.server.id + "]\n       User:[" + ctx.message.author.id + "]\n       Channel:[" + ctx.message.channel.id + "]")

#command13
@client.command(pass_context = True, description='Unmutes the muted members.', no_pm = True)
async def unmute(ctx, *, member : discord.Member):
    if not ctx.message.author.server_permissions.mute_members:
        return print(Fore.RED + "Command Failed To Execute |\n       Command Ran In:[" + ctx.message.server.id + "]\n       User:[" + ctx.message.author.id + "]\n       Channel:[" + ctx.message.channel.id + "]\n       Reason: " + Fore.YELLOW + "Insufficient Permissions! Both user and bot need Mute Members permission!")
    overwrite = discord.PermissionOverwrite()
    overwrite.send_messages = True
    await client.edit_channel_permissions(ctx.message.channel, member, overwrite)
    await client.say("**%s** has been unmuted!"%member.mention)
    print(Fore.CYAN + "Command Successfully Executed |\n       Command Ran In:[" + ctx.message.server.id + "]\n       User:[" + ctx.message.author.id + "]\n       Channel:[" + ctx.message.channel.id + "]")

#command14
answers = ["My source say no.", "I completely disagree.", "No way in hell!", "Sure! :D", "Why not?", "Why would you say that?", "When life gives you lemons, throw them at people!", "HA, You wish!", "Keep dreaming!", "Does a green light mean go?", "Red is supposed to stop you, but your magic is TOO strong! :sweat:", "Power outage!??! WHAT ABOUT MY WIFI!??!!", "Hmmm.. this is hard", "lol, just lol.", "Cleverbot is no match for me! Haahahaha", "The chances of that happening are equal to the chances of shivaco getting a girlfriend. Null!", "There's an admin watching :scream:", "Ask me tomorrow :zzz:", "No... I mean yes... Well... Ask again later"]

@client.command(description='Decides for you.', aliases=['8ball'])
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
@client.command(pass_context = True)
async def github(ctx):
    """  ---Link to Github"""
    embed = discord.Embed(description = "Yotsugi Github can be found here: https://github.com/YotsugiBot", color = embed_color)
    await client.say(embed = embed)
    print(Fore.CYAN + "Command Successfully Executed |\n       Command Ran In:[" + ctx.message.server.id + "]\n       User:[" + ctx.message.author.id + "]\n       Channel:[" + ctx.message.channel.id + "]")
	
	
@client.command(pass_context = True)
async def license(ctx):
	embed = discord.Embed(description = "Read the License [here](https://github.com/Kyousei/YotsugiBot/blob/master/LICENSE.md)", color = embed_color)
	await client.say(embed = embed)
	print(Fore.CYAN + "Command Successfully Executed |\n       Command Ran In:[" + ctx.message.server.id + "]\n       User:[" + ctx.message.author.id + "]\n       Channel:[" + ctx.message.channel.id + "]")

	
#command18
@client.command(pass_context = True, no_pm = True)
async def servers(ctx):
    x = '\n'.join([str(server) for server in client.servers])
    print(x)
    embed = discord.Embed(title = "Servers", description = x, color = embed_color)
    return await client.say(embed = embed)
    print(Fore.CYAN + "Command Successfully Executed |\n       Command Ran In:[" + ctx.message.server.id + "]\n       User:[" + ctx.message.author.id + "]\n       Channel:[" + ctx.message.channel.id + "]")


#Stats Command
@client.command(pass_context = True, no_pm = False)
async def stats(ctx):
    second = time.time() - start_time
    minute, second = divmod(second, 60)
    hour, minute = divmod(minute, 60)
    day, hour = divmod(hour, 24)
    week, day = divmod(day, 7)
    embed = discord.Embed(title = "Yotsugi **" + bot_version + "**", color = embed_color)
    embed.add_field(name='Author', value=bot_author, inline=True)
    embed.add_field(name='Uptime', value="**%d** weeks, \n**%d** days, \n**%d** hours, \n**%d** minutes, \n**%d** seconds"% (week, day, hour, minute, second), inline=True)
    embed.add_field(name='Owner IDs', value=bot_author_id, inline=True)
    await client.say(embed = embed)
    print(Fore.CYAN + "Command Successfully Executed |\n       Command Ran In:[" + ctx.message.server.id + "]\n       User:[" + ctx.message.author.id + "]\n       Channel:[" + ctx.message.channel.id + "]")


@client.command(pass_context=True, no_pm=True, aliases=['die'])
async def shutdown(ctx):
    if owner == ctx.message.author.id:
        embed = discord.Embed(description = "Shutting Down...", color = embed_color)
        await client.say(embed = embed)
        print(Fore.CYAN + "Command Successfully Executed |\n       Command Ran In:[" + ctx.message.server.id + "]\n       User:[" + ctx.message.author.id + "]\n       Channel:[" + ctx.message.channel.id + "]")
        await client.logout()
        

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
        print(Fore.RED + "Command Failed To Execute |\n       Command Ran In:[" + ctx.message.server.id + "]\n       User:[" + ctx.message.author.id + "]\n       Channel:[" + ctx.message.channel.id + "]\n       Reason: " + Fore.YELLOW + "Insufficient Permissions! Both user and bot need Manage Roles permission!")


@client.command(pass_context=True, no_pm=True, aliases=['setrl'])
async def setrole(ctx, user: discord.Member, *, role):
    if ctx.message.author.server_permissions.manage_roles:
        await client.add_roles(user, discord.utils.get(ctx.message.server.roles, name=role))
        embed = discord.Embed(description = ("Added %s to  **%s** " % (user.mention, role)), color = embed_color)
        await client.say(embed = embed)
        print(Fore.CYAN + "Command Successfully Executed |\n       Command Ran In:[" + ctx.message.server.id + "]\n       User:[" + ctx.message.author.id + "]\n       Channel:[" + ctx.message.channel.id + "]")
    else:
        embed = discord.Embed(description = ":x: Insufficient permissions!", color = 0xFF0000)
        return await client.say(embed = embed)
        print(Fore.RED + "Command Failed To Execute |\n       Command Ran In:[" + ctx.message.server.id + "]\n       User:[" + ctx.message.author.id + "]\n       Channel:[" + ctx.message.channel.id + "]\n       Reason: " + Fore.YELLOW + "Insufficient Permissions! Both user and bot need Manage Roles permission!")

@client.command(pass_context = True, no_pm = True)
async def warn(ctx, member : discord.Member, *, message):
        if ctx.message.author.id != owner:
                return print("User **" + ctx.message.author.id + "** tried to use :warn in **" + ctx.message.channel.server.id + "**! It did NOT work because they are not the owner")
                print(Fore.RED + "Command Failed To Execute |\n       Command Ran In:[" + ctx.message.server.id + "]\n       User:[" + ctx.message.author.id + "]\n       Channel:[" + ctx.message.channel.id + "]\n       Reason: " + Fore.YELLOW + "Not owner!")
        if ctx.message.author.id == owner:
                embed = discord.Embed(description = "You've been warned for: **" + message + "**\nResponsible Moderator: **" + ctx.message.author.mention + "**\nServer: **" + ctx.message.server.name + "**", color = 0xFF0000)
                return await client.send_message(member, embed = embed)
                print(Fore.CYAN + "Command Successfully Executed |\n       Command Ran In:[" + ctx.message.server.id + "]\n       User:[" + ctx.message.author.id + "]\n       Channel:[" + ctx.message.channel.id + "]")


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
                print(Fore.RED + "Command Error Raised, But The Command Was Still Executed |\n       Command Ran In:[" + ctx.message.server.id + "]\n       User:[" + ctx.message.author.id + "]\n       Channel:[" + ctx.message.channel.id + "]\n       Reason: " + Fore.YELLOW + "Ignore this error!")


heads = "heads.png"
tails = "tails.png"
@client.command(pass_context=True, aliases=['flip'])
async def flipcoin(ctx):
    choice = random.randint(1,2)
    if choice == 1:
        await client.send_file(ctx.message.channel, heads, content=ctx.message.author.mention + ", you flipped **Heads**!", tts=False)
    if choice == 2:
        await client.send_file(ctx.message.channel, tails, content=ctx.message.author.mention + ", you flipped **Tails**!", tts=False)


@client.command()
async def h(command = None):
    embed = discord.Embed(description = "**Hosting Guides: https://github.com/Kyousei/YotsugiBot/wiki** \n**Commands List: https://goo.gl/w6Aoag**", color = embed_color)
    if not command:
            await client.say(embed = embed)
            return

        #some code to check if the command is an actual command (depends on how you make commands)
    if command == ';b':
        embed = discord.Embed(title = "`;ban` / `;b`", description = "Bans the user from the server", color = embed_color)
        embed.add_field(name='Usage', value="`;ban @User/ID` or `;b @User/UserID`", inline=True)
        embed.add_field(name='User Permissions:', value='Ban Members', inline=True)
        embed.add_field(name='Bot Permissions:', value='Ban Members', inline=True)
        await client.say(embed = embed)
        return


    if command == ';k':
        embed = discord.Embed(title = "`;kick` / `;k`", description = "Kicks the user from the server", color = embed_color)
        embed.add_field(name='Usage', value="`;kick @User/ID` or `;k @User/UserID`", inline=True)
        embed.add_field(name='User Permissions:', value='Kick Members', inline=True)
        embed.add_field(name='Bot Permissions:', value='Kick Members', inline=True)
        await client.say(embed = embed)
        return

    if command == ';serverid':
        embed = discord.Embed(title = "`;serverid` / `;serid`", description = "Show's the ID of the server.", color = embed_color)
        embed.add_field(name='Usage', value="`;serverid` or `;serid`", inline=True)
        embed.add_field(name='User Permissions:', value='`None`', inline=True)
        embed.add_field(name='Bot Permissions:', value='Send Messages', inline=True)
        await client.say(embed = embed)
        return

    if command == ';ud':
        embed = discord.Embed(title = "`;ud`", description = "Searches urban disctionary for the meaning of a word.", color = embed_color)
        embed.add_field(name='Usage', value="`;ud lol`", inline=True)
        embed.add_field(name='User Permissions:', value='`None`', inline=True)
        embed.add_field(name='Bot Permissions:', value='Send Messages', inline=True)
        await client.say(embed = embed)
        return

    if command == ';8ball':
        embed = discord.Embed(title = "`;eightball` / `;8ball`", description = "8balls your question.", color = embed_color)
        embed.add_field(name='Usage', value="`;eightball to be or not to be` or `;8ball to be or not to be`", inline=True)
        embed.add_field(name='User Permissions:', value='`None`', inline=True)
        embed.add_field(name='Bot Permissions:', value='Send Messages', inline=True)
        await client.say(embed = embed)
        return

    if command == ';eightball':
        embed = discord.Embed(title = "`;eightball` / `;8ball`", description = "8balls your question.", color = embed_color)
        embed.add_field(name='Usage', value="`;eightball to be or not to be` or `;8ball to be or not to be`", inline=True)
        embed.add_field(name='User Permissions:', value='`None`', inline=True)
        embed.add_field(name='Bot Permissions:', value='Send Messages', inline=True)
        await client.say(embed = embed)
        return

    if command == ';serid':
        embed = discord.Embed(title = "`;serverid` / `;serid`", description = "Show's the ID of the server.", color = embed_color)
        embed.add_field(name='Usage', value="`;serverid` or `;serid`", inline=True)
        embed.add_field(name='User Permissions:', value='`None`', inline=True)
        embed.add_field(name='Bot Permissions:', value='Send Messages', inline=True)
        await client.say(embed = embed)
        return

    if command == ';clear':
        embed = discord.Embed(title = "`;clear` / `;prune` / `;purge`", description = "Deletes `x` amount of messages.", color = embed_color)
        embed.add_field(name='Usage', value="`;clear 5` or `;prune 5` or `;purge 5`", inline=True)
        embed.add_field(name='User Permissions:', value='Manage Messages', inline=True)
        embed.add_field(name='Bot Permissions:', value='Send Messages', inline=True)
        await client.say(embed = embed)
        return

    if command == ';prune':
        embed = discord.Embed(title = "`;clear` / `;prune` / `;purge`", description = "Deletes `x` amount of messages.", color = embed_color)
        embed.add_field(name='Usage', value="`;clear 5` or `;prune 5` or `;purge 5`", inline=True)
        embed.add_field(name='User Permissions:', value='Manage Messages', inline=True)
        embed.add_field(name='Bot Permissions:', value='Manage Messages', inline=True)
        await client.say(embed = embed)
        return

    if command == ';purge':
        embed = discord.Embed(title = "`;clear` / `;prune` / `;purge`", description = "Deletes `x` amount of messages.", color = embed_color)
        embed.add_field(name='Usage', value="`;clear 5` or `;prune 5` or `;purge 5`", inline=True)
        embed.add_field(name='User Permissions:', value='Manage Messages', inline=True)
        embed.add_field(name='Bot Permissions:', value='Manage Messages', inline=True)
        await client.say(embed = embed)
        return

    if command == ';mute':
        embed = discord.Embed(title = "`;mute`", description = "Mutes the user in the channel where command was ran.", color = embed_color)
        embed.add_field(name='Usage', value="`;mute @User`", inline=True)
        embed.add_field(name='User Permissions:', value='Mute Members', inline=True)
        embed.add_field(name='Bot Permissions:', value='Manage Channels', inline=True)
        await client.say(embed = embed)
        return

    if command == ';unmute':
        embed = discord.Embed(title = "`;unmute`", description = "Mutes the user in the channel where command was ran.", color = embed_color)
        embed.add_field(name='Usage', value="`;unmute @User`", inline=True)
        embed.add_field(name='User Permissions:', value='Mute Members', inline=True)
        embed.add_field(name='Bot Permissions:', value='Manage Channels', inline=True)
        await client.say(embed = embed)
        return

    if command == ';stats':
        embed = discord.Embed(title = "`;stats`", description = "Shows bot's statistics.", color = embed_color)
        embed.add_field(name='Usage', value="`;stats`", inline=True)
        embed.add_field(name='User Permissions:', value='`None`', inline=True)
        embed.add_field(name='Bot Permissions:', value='Send Messages', inline=True)
        await client.say(embed = embed)
        return

    if command == ';author':
        embed = discord.Embed(title = "`;author`", description = "Shows information about bot author.", color = embed_color)
        embed.add_field(name='Usage', value="`;author`", inline=True)
        embed.add_field(name='User Permissions:', value='`None`', inline=True)
        embed.add_field(name='Bot Permissions:', value='Send Messages', inline=True)
        await client.say(embed = embed)
        return

    if command == ';banlist':
        embed = discord.Embed(title = "`;banlist`", description = "Shows list of banned users for that server..", color = embed_color)
        embed.add_field(name='Usage', value="`;banlist`", inline=True)
        embed.add_field(name='User Permissions:', value='`None`', inline=True)
        embed.add_field(name='Bot Permissions:', value='Send Messages', inline=True)
        await client.say(embed = embed)
        return

    if command == ';ping':
        embed = discord.Embed(title = "`;ping`", description = "Shows your ping to the bot..", color = embed_color)
        embed.add_field(name='Usage', value="`;ping`", inline=True)
        embed.add_field(name='User Permissions:', value='`None`', inline=True)
        embed.add_field(name='Bot Permissions:', value='Send Messages', inline=True)
        await client.say(embed = embed)
        return

    if command == ';connect':
        embed = discord.Embed(title = "`;connect`", description = "Joins the voice channel.", color = embed_color)
        embed.add_field(name='Usage', value="`;connect`", inline=True)
        embed.add_field(name='User Permissions:', value='`None`', inline=True)
        embed.add_field(name='Bot Permissions:', value='Connect', inline=True)
        await client.say(embed = embed)
        return

    if command == ';disconnect':
        embed = discord.Embed(title = "`;disconnect`", description = "Leaves the voice channel.", color = embed_color)
        embed.add_field(name='Usage', value="`;disconnect`", inline=True)
        embed.add_field(name='User Permissions:', value='`None`', inline=True)
        embed.add_field(name='Bot Permissions:', value='Connect', inline=True)
        await client.say(embed = embed)
        return

    if command == ';channelid':
        embed = discord.Embed(title = "`;channelid` / `;chnlid``", description = "Shows the channel ID the command was ran in.", color = embed_color)
        embed.add_field(name='Usage', value="`;channelid` or `;chnlid`", inline=True)
        embed.add_field(name='User Permissions:', value='`None`', inline=True)
        embed.add_field(name='Bot Permissions:', value='Send Messages', inline=True)
        await client.say(embed = embed)
        return

    if command == ';chnlid':
        embed = discord.Embed(title = "`;channelid` / `;chnlid``", description = "Shows the channel ID the command was ran in.", color = embed_color)
        embed.add_field(name='Usage', value="`;channelid` or `;chnlid`", inline=True)
        embed.add_field(name='User Permissions:', value='`None`', inline=True)
        embed.add_field(name='Bot Permissions:', value='Send Messages', inline=True)
        await client.say(embed = embed)
        return

    if command == ';github':
        embed = discord.Embed(title = "`;github`", description = "Gives the link to GitHub.", color = embed_color)
        embed.add_field(name='Usage', value="`;github`", inline=True)
        embed.add_field(name='User Permissions:', value='`None`', inline=True)
        embed.add_field(name='Bot Permissions:', value='Send Messages', inline=True)
        await client.say(embed = embed)
        return

    if command == ';send':
        embed = discord.Embed(title = "`;send`", description = "Sends a message to a user.", color = embed_color)
        embed.add_field(name='Usage', value="`;send @User Hi`", inline=True)
        embed.add_field(name='User Permissions:', value='`None`', inline=True)
        embed.add_field(name='Bot Permissions:', value='Send Messages', inline=True)
        await client.say(embed = embed)
        return

    if command == ';shutdown':
        embed = discord.Embed(title = "`;die` / `;shutdown`", description = "Boots the bot offline.", color = embed_color)
        embed.add_field(name='Usage', value="`;shutdown` or `;die`", inline=True)
        embed.add_field(name='User Permissions:', value='`None`', inline=True)
        embed.add_field(name='Bot Permissions:', value='Send Messages', inline=True)
        await client.say(embed = embed)
        return

    if command == ';die':
        embed = discord.Embed(title = "`;die` / `;shutdown`", description = "Boots the bot offline.", color = embed_color)
        embed.add_field(name='Usage', value="`;shutdown` or `;die`", inline=True)
        embed.add_field(name='User Permissions:', value='`None`', inline=True)
        embed.add_field(name='Bot Permissions:', value='Send Messages', inline=True)
        await client.say(embed = embed)
        return

    if command == ';setrole':
        embed = discord.Embed(title = "`;setrole` / `;setrl`", description = "Gives a role to a user.", color = embed_color)
        embed.add_field(name='Usage', value="`;setrole @User Role-Name` or `;setrl @User Role-Name`", inline=True)
        embed.add_field(name='User Permissions:', value='`None`', inline=True)
        embed.add_field(name='Bot Permissions:', value='Send Messages', inline=True)
        await client.say(embed = embed)
        return

    if command == ';setrl':
        embed = discord.Embed(title = "`;setrole` / `;setrl`", description = "Gives a role to the user.", color = embed_color)
        embed.add_field(name='Usage', value="`;setrole @User Role-Name` or `;setrl @User Role-Name`", inline=True)
        embed.add_field(name='User Permissions:', value='`None`', inline=True)
        embed.add_field(name='Bot Permissions:', value='Send Messages', inline=True)
        await client.say(embed = embed)
        return

    if command == ';removerole':
        embed = discord.Embed(title = "`;removerole` / `;remrl`", description = "Removes a role from the user.", color = embed_color)
        embed.add_field(name='Usage', value="`;removerole @User Role-Name` or `;remrl @User Role-Name`", inline=True)
        embed.add_field(name='User Permissions:', value='`None`', inline=True)
        embed.add_field(name='Bot Permissions:', value='Send Messages', inline=True)
        await client.say(embed = embed)
        return

    if command == ';remrl':
        embed = discord.Embed(title = "`;removerole` / `;remrl`", description = "Removes a role from the user.", color = embed_color)
        embed.add_field(name='Usage', value="`;removerole @User Role-Name` or `;remrl @User Role-Name`", inline=True)
        embed.add_field(name='User Permissions:', value='`None`', inline=True)
        embed.add_field(name='Bot Permissions:', value='Send Messages', inline=True)
        await client.say(embed = embed)
        return

    if command == ';flip':
        embed = discord.Embed(title = "`;flip` / `;flipcoin`", description = "Flips the coin.", color = embed_color)
        embed.add_field(name='Usage', value="`;flip` or `;flipcoin`", inline=True)
        embed.add_field(name='User Permissions:', value='`None`', inline=True)
        embed.add_field(name='Bot Permissions:', value='Send Messages, Attach Files', inline=True)
        await client.say(embed = embed)
        return

    if command == ';roll':
        embed = discord.Embed(title = "`;roll`", description = "Rolls the dice in NdN format.", color = embed_color)
        embed.add_field(name='Usage', value="`;roll 5d5`", inline=True)
        embed.add_field(name='User Permissions:', value='`None`', inline=True)
        embed.add_field(name='Bot Permissions:', value='Send Messages', inline=True)
        await client.say(embed = embed)
        return

    if command == ';servers':
        embed = discord.Embed(title = "`;servers`", description = "Shows the list of servers the bot is in.", color = embed_color)
        embed.add_field(name='Usage', value="`;servers`", inline=True)
        embed.add_field(name='User Permissions:', value='`None`', inline=True)
        embed.add_field(name='Bot Permissions:', value='Send Messages', inline=True)
        await client.say(embed = embed)
        return

    if command == ';h':
        embed = discord.Embed(title = "`;h`", description = "Shows the info about a command.", color = embed_color)
        embed.add_field(name='Usage', value="`;h ;ban`", inline=True)
        embed.add_field(name='User Permissions:', value='`None`', inline=True)
        embed.add_field(name='Bot Permissions:', value='Send Messages', inline=True)
        await client.say(embed = embed)
        return



'''---------------------------------------------------------------------'''

client.run(BotToken)
