import discord
from discord.ext import commands
import asyncio
from discord import Webhook, AsyncWebhookAdapter
import aiohttp
from contextlib import redirect_stdout
from discord_slash import SlashCommand

intents = discord.Intents.all()
client = discord.Client(intents=intents)
slash = SlashCommand(client, sync_commands=True)

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online)
    print('logged in as the Private Bowsette Bot.')

@client.event
async def on_message(message):
    if "MessageType.premium_guild" in str(message.type):
        channel = client.guilds[0].get_channel(CHANNELIDHERE)
        print(channel)
        embed = discord.Embed(title="SERVER BOOST | Server Name Here", description=f"We have a new booster. Thank you.", color=(16750330))
        await message.channel.send(embed=embed)

@client.event
async def on_member_join(member):
    print(f'{member.name} has joined the server')
    channel = client.guilds[0].get_channel(CHANNELIDHERE)
    print(channel)
    embed = discord.Embed(title="MEMBER JOIN | Server Name Here", description=f"{member.name} has joined the server.", color=(3140255))
    embed.set_thumbnail(url=member.avatar_url)
    await channel.send(embed=embed)
    guild = await client.fetch_guild(SERVERIDHERE)
    role = discord.utils.get(guild.roles, name='Unverified')
    await member.add_roles(role)
    
    async with aiohttp.ClientSession() as session:
        webhook = Webhook.from_url('WEBHOOKTOKEN', adapter=AsyncWebhookAdapter(session))
        await webhook.send(f'Hello {member.name} We are glad you are able to join us. Please make sure you read the rules and enjoy your stay here. In order to access the rest of the server, you need to verify yourself in the verify channel.')
    
    embed2 = discord.Embed(title="HI THERE", description=f"Welcome {member.name} to SERVER NAME HERE", color=(3140255))
    embed2.add_field(name="How to access the server?", value="In order to access the rest of the server, head to the verify channel and type in **/verify**", inline=False)
    await member.send(embed=embed2)

@client.event
async def on_member_remove(member):
    print(f'{member.name} has left the server')
    channel = client.guilds[0].get_channel(CHANNELIDHERE)
    print(channel)
    embed = discord.Embed(title="MEMBER LEAVE | Server Name Here", description=f"{member.name} has left the server. How sad", color=(16711680))
    await channel.send(embed=embed)

@slash.slash(name="verify", description='Gain access to the server')
async def _verify(ctx):
    mutedRole = discord.utils.get(ctx.guild.roles, name="ROLENAMEHERE")

    await ctx.author.remove_roles(mutedRole)
    await ctx.send("You have been verified and have access to the rest of the server.")
    embed = discord.Embed(title="SUCCESSFULLY VERIFIED", description=f"Thank you for verifying yourself into the server. Now you can access the rest of the server now.", color=(3140255))
    await ctx.author.send(embed=embed)
    return




client.run("DISCORDBOTTOKEN")
