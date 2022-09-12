import discord
from discord.ext import commands
import asyncio
from discord import Webhook, AsyncWebhookAdapter
import aiohttp
from contextlib import redirect_stdout
from discord_slash import SlashCommand
import json

intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)
slash = SlashCommand(client, sync_commands=True)

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online)
    print('logged in as **Bot**')

@client.event
async def on_member_join(member):
    with open('guilds.json', 'r', encoding='utf-8') as f:
        guilds_dict = json.load(f)
    channel_id = guilds_dict[str(member.guild.id)]
    embed = discord.Embed(title=f"MEMBER JOIN | {member.guild.name}", description=f"Hello {member.mention} and Welcome to **{member.guild.name}**. Make sure to read the rules channel", color=(3140255))
    embed.set_thumbnail(url=member.avatar_url)
    await client.get_channel(int(channel_id)).send(embed=embed)

    async with aiohttp.ClientSession() as session:
        webhook = Webhook.from_url('WEBHOOKTOKEN', adapter=AsyncWebhookAdapter(session))
        await webhook.send(f'{member.mention} joined **{member.guild.name}**')

    guild = member.guild
    role = discord.utils.get(guild.roles, name='Unverified')
    await member.add_roles(role)
    
    embed2 = discord.Embed(title="HI THERE", description=f"Welcome {member.mention} to **{member.guild.name}**", color=(3140255))
    embed2.add_field(name="How to access the server?", value="In order to access the rest of the server, head over to the verify channel and type in **/verify** with me", inline=False)
    await member.send(embed=embed2)

@client.event
async def on_member_remove(member):
    with open('guilds.json', 'r', encoding='utf-8') as f:
        guilds_dict = json.load(f)
    channel_id = guilds_dict[str(member.guild.id)]
    embed = discord.Embed(title=f"MEMBER LEAVE | {member.guild.name}", description=f"**{member.name}** has left **{member.guild.name}**. How sad", color=(16711680))
    await client.get_channel(int(channel_id)).send(embed=embed)
    
    async with aiohttp.ClientSession() as session:
        webhook = Webhook.from_url('WEBHOOKTOKEN', adapter=AsyncWebhookAdapter(session))
        await webhook.send(f'{member.name} left **CAT ROSALINA 18+**')





@slash.slash(name="verify", description='Gain access to the server')
async def verify(ctx):
    role = discord.utils.get(ctx.guild.roles, name="Unverified")

    if role in ctx.author.roles:
        await ctx.author.remove_roles(role)
        await ctx.send("You have been verified and have access to the rest of the server.")
        embed = discord.Embed(title="SUCCESSFULLY VERIFIED", description=f"Thank you for verifying yourself into the server. Now you can access the rest of the server now.", color=(3140255))
        embed.set_footer(text=f"Successfully Verified in **{ctx.guild.name}")
        await ctx.author.send(embed=embed)
        return
    else:
        await ctx.send("You are already verified. No need to rerun this command.")

@slash.slash(name="setwchannel", description='Sets which channel to send Welcome logs to for your current server.')
@commands.has_permissions(manage_channels=True)
async def setwchannel(ctx, channel: discord.TextChannel):
    with open('guilds.json', 'r', encoding='utf-8') as f:
        guilds_dict = json.load(f)

    guilds_dict[str(ctx.guild.id)] = str(channel.id)
    with open('guilds.json', 'w', encoding='utf-8') as f:
        json.dump(guilds_dict, f, indent=4, ensure_ascii=False)
    
    await ctx.send(f'I set the welcome channel for **{ctx.guild.name}** to **{channel.name}**')

@setwchannel.error
async def setwchannel_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send('HEY! YOU NEED TO HAVE THE **MANAGE_CHANNELS** PERMISSION TO CONTINUE')
    else:
        raise error

@slash.slash(name="resources", description='See useful links and stats.')
async def resources(ctx):
    embed = discord.Embed(title="USEFUL RESOURCES", description="Here is some useful links and stats.", color=(3140255))
    embed.add_field(name="Your Current Server Stats", value="Guild Name: {ctx.guild.name}\nGuild ID: {ctx.guild.id}\nGuild Member Count: {ctx.guild.member_count}", inline=False)
    embed.add_field(name="ORIGNAL SOURCE", value="Orignal Source Code: https://github.com/ErisTheEagleArt/advancewelcomebot.py\nMade and Provided by: LLoC Eagle Fan Art#1681", inline=False)
    await ctx.send(embed=embed)

@slash.slash(name="verifysetup", description='Set up the Verification role and Verify channel.')
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
    await channel.send("WELCOME TO CAT ROSALINA 18+ | ERIS DEVELOPMENT\n\nTo prevent spam and abuse, be sure to verify yourself here by typing **/verify** with <@997300484132061184>\nWARNING: Even though there is no p*rn content here, however content in this server is suggestive which is intended for Mature Audiences\nPLEASE DO NOT JUDGE US WHEN YOU ACCESS THE SERVER!\n\nIf you are having issues verifying yourself, DM me and I will help you get verified.\nYou do NOT have to verify yourself, you can just chill here")
    await channel.set_permissions(role, send_messages=True, read_messages=True)
    await ctx.send("The **Unverified** role the the **verify** text channel has been set up again")





client.run("DISCORDBOTTOKEN")
