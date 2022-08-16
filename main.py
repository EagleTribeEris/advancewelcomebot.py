import discord
from discord.ext import commands
import asyncio
from discord import Webhook, AsyncWebhookAdapter
import aiohttp
from contextlib import redirect_stdout
from discord_slash import SlashCommand
import json

intents = discord.Intents.all()
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
    mutedRole = discord.utils.get(ctx.guild.roles, name="ROLENAMEHERE")

    await ctx.author.remove_roles(mutedRole)
    await ctx.send("You have been verified and have access to the rest of the server.")
    embed = discord.Embed(title="SUCCESSFULLY VERIFIED", description=f"Thank you for verifying yourself into the server. Now you can access the rest of the server now.", color=(3140255))
    await ctx.author.send(embed=embed)
    return

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





client.run("DISCORDBOTTOKEN")
