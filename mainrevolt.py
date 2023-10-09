import voltage
from voltage.ext import commands
import random
import json
import asyncio
import aiohttp

client = commands.CommandsClient("!")

@client.listen("ready")
async def ready():
    print("logged in as the Utility Bot.")

@client.listen("member_join")
async def on_member_join(member: voltage.Member):
    with open('guilds.json', 'r', encoding='utf-8') as f:
        guilds_dict = json.load(f)

    channel_id = guilds_dict[str(member.server.id)]
    embed = voltage.SendableEmbed(title="MEMBER JOIN", description=f"{member.mention} has joined the server.", media=member.display_avatar.url, color="#2FEA9F")
    await client.get_channel(str(channel_id)).send(embed=embed)

botdev = ["INSERTYOURUSERIDHERE"]

@commands.is_server_owner()
@client.command(description="Sets which channel to send Welcome logs to")
async def setwchannel(ctx, channel: voltage.Channel):
    if ctx.author.id in botdev:
        with open('guilds.json', 'r', encoding='utf-8') as f:
            guilds_dict = json.load(f)
        guilds_dict[str(ctx.server.id)] = str(channel.id)
        with open('guilds.json', 'w', encoding='utf-8') as f:
            json.dump(guilds_dict, f, indent=4, ensure_ascii=False)
        await ctx.send(f'Set welcome channel for **{ctx.message.server.name}** to **{channel.name}**')
    else:
        await ctx.send("This command is locked to the Bot owner/Admins")
        return



client.run("REVOLTBOTTOKEN")
