import discord
from discord.ext import commands
import asyncio
import aiohttp
import random
import sys

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
client = discord.Client(intents=intents)
client = commands.Bot(command_prefix= commands.when_mentioned_or('>'), intents=intents)
client.remove_command("help")

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online)
    print('logged in as the Utility Bot.')

@client.event
async def on_member_join(member):
    with open('guilds.json', 'r', encoding='utf-8') as f:
        guilds_dict = json.load(f)
    channel_id = guilds_dict[str(member.guild.id)]
    embed = discord.Embed(title=f"MEMBER JOIN | {member.guild.name}", description=f"{member.name} has joined the server.", color=(65280))
    embed.set_thumbnail(url=member.avatar_url)
    embed.set_footer(text="Open Source Code by LLoC Eagle Fan Art#1681")
    await client.get_channel(int(channel_id)).send(embed=embed)
    
    guild = await client.fetch_guild(SERVERIDHERE)
    role = discord.utils.get(guild.roles, name='Unverified')
    await member.add_roles(role)
    
    async with aiohttp.ClientSession() as session:
        webhook = discord.Webhook.from_url('WEBHOOKTOKEN', session=session)
        await webhook.send(f'Hello {member.name} We are glad you are able to join us. Please make sure you read the rules and enjoy your stay here. In order to access the rest of the server, you need to verify yourself in the verify channel.')
    
    embed2 = discord.Embed(title="HI THERE", description=f"Welcome {member.name} to SERVER NAME HERE", color=(65280))
    embed2.add_field(name=content="How to access the server?", value="In order to access the rest of the server, head to the verify channel and type in **>verify**", inline=False)
    await member.send(embed=embed2)

@client.event
async def on_member_remove(member):
    with open('guilds.json', 'r', encoding='utf-8') as f:
        guilds_dict = json.load(f)
    channel_id = guilds_dict[str(member.guild.id)]
    embed = discord.Embed(title=f"MEMBER LEAVE | {member.guild.name}", description=f"{member.name} has left the server. How sad", color=(16711680))
    await client.get_channel(int(channel_id)).send(embed=embed)

@client.command()
async def help(ctx):
    embed = discord.Embed(title="advancedwelcomebot.py", description="Here are my commands", color=(49407))
    embed.add_field(name="CORE COMMANDS", value=">help - This message\n>ping - Checks my latency", inline=False)
    embed.add_field(name="UTILITY COMMANDS", value=">verify - Verify yourself into the server\n>setwchannel - Sets which channel to send Welcome logs to.\n>verifysetup - Sets up the Verification channel and role.", inline=False)
    embed.add_field(name="SOURCE CODE", value="Original Source Code: https://github.com/ErisTheEagleArt/advancewelcomebot.py", inline=False)
    await ctx.send(embed=embed)

@client.command()
async def ping(ctx):
    await ctx.send(f'My current latency is: {round(client.latency * 1000)}ms')

@client.command()
async def verify(ctx):
    mutedRole = discord.utils.get(ctx.guild.roles, name="ROLENAMEHERE")
    await ctx.author.remove_roles(mutedRole)
    await ctx.send("You have been verified and have access to the rest of the server.")
    embed = discord.Embed(title="SUCCESSFULLY VERIFIED", description=f"Thank you for verifying yourself into the server. Now you can access the rest of the server now.", color=(65535))
    await ctx.author.send(embed=embed)
    return

@client.command()
@commands.has_permissions(manage_channels=True)
async def setwchannel(ctx, channel: discord.TextChannel):
    with open('guilds.json', 'r', encoding='utf-8') as f:
        guilds_dict = json.load(f)

    guilds_dict[str(ctx.guild.id)] = str(channel.id)
    with open('guilds.json', 'w', encoding='utf-8') as f:
        json.dump(guilds_dict, f, indent=4, ensure_ascii=False)
    
    await ctx.send(f'I have set the welcome channel for **{ctx.message.guild.name}** to **{channel.name}**')

@client.command()
@commands.has_permissions(manage_roles=True, manage_channels=True)
@commands.bot_has_permissions(manage_roles=True, manage_channels=True)
async def verifysetup(ctx):
    await ctx.send("I am now setting up the Unverified Role and verification channel. This may take a few seconds. PLEASE NO NOT RERUN THIS COMMAND!")
    guild = ctx.guild
    mutedRole = discord.utils.get(guild.roles, name="Unverified")

    if mutedRole:
        await ctx.send("The Unverified Role already exists. No need to rerun this command")
        return

    if not mutedRole:
        mutedRole = await guild.create_role(name="Unverified")

        for channel in guild.channels:
            await channel.set_permissions(mutedRole, speak=False, send_messages=False, read_message_history=True, read_messages=True)

    await asyncio.sleep(2)

    channel = await guild.create_text_channel('verify')

    guild = ctx.guild
    channel = discord.utils.get(guild.text_channels, name="verify")
    role = discord.utils.get(guild.roles, name="@everyone")
    await channel.set_permissions(role, send_messages=False, read_messages=False)
        
    await asyncio.sleep(2)

    guild = ctx.guild
    channel = discord.utils.get(guild.text_channels, name="verify")
    role = discord.utils.get(guild.roles, name="Unverified")
    await channel.send("WELCOME TO YOURSERVERNAMEHERE\n\nTo prevent spam and abuse, be sure to verify yourself here by typing **/verify** with <@YOURBOTIDHERE>")
    await channel.set_permissions(role, send_messages=True, read_messages=True)
    await ctx.send("The **Unverified** role the the **verify** text channel has been set up again")

@verifysetup.error
async def verifysetup_error(ctx, error):
    if isinstance(error, commands.BotMissingPermissions):
        await ctx.send("HEY! YOU NEED TO HAVE THE **MANAGE_CHANNELS** AND **MANAGE_ROLE** PERMISSION TO CONTINUE")
    if isinstance(error, commands.MissingPermissions):
        await ctx.send('SYSTEM ERROR: I require the **MANAGE_CHANNELS** and **MANAGE_ROLES** Permission. Recommended to give me Admin to prevent errors.')
    else:
        raise error




client.run("DISCORDBOTTOKEN")
