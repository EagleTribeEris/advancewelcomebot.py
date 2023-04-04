WELCOME BOT WITH SLASH COMMANDS FOR DISCORD.PY

This source code allows you to welcome members while having Slash commands work.
Includes:
- Sending messages in a desired text channel
- Gives a role to a member
- Sends a welcome message to a webhook
- DMs members upon joining the server

With the Discord.py 2.0 rewrite, Slash commands became normal commands because slash commands has a big
problem where there is no permission handling in slash commands.

================================================

With the Discord.py 2.0 rewrite. The code has been improved a lot. Here is what has been changed since the last Discord.py 1.7.x release
- Slash commands became normal commands (Default prefix is >)
- Code specify you need Message Content Intent
- Code suitable for public bots since we use json file to store data on where to send Logs to which channel and which server
- Added Ping command.

================================================

READ THIS: I am unable to get a data reset command to work at all.
The only way to remove your server/channel ids from the json file is too manually remove it from the file.
Turn on Developers mode to find out your server id.
I tried modifing the on_guild_remove in https://stackoverflow.com/questions/64760333/how-to-set-a-welcome-channel-discord-py
and modified it to a command but unable to get it to work. At this point, idk if it is even possible to remove data from your json file via command.
I always get the following error: discord.ext.commands.errors.CommandInvokeError: Command raised an exception: KeyError: 'MYGUILDIDHERE'
If you know how to fix this or create a data reset command, PLEASE let me know but submitting an issue or pull request.

================================================

REQUIREMENTS:
- Knowledge of Discord.py
- A discord bot application with token
- Python 3.8.6 or newer (Using a Python software version below this may cause issues)

================================================

SETUP:
1. Fork or Download this Source code to your hosting provider
2. Create a Discord Bot Application and copy your bot token at https://discord.com/developers
3. At the bottom, replace DISCORDBOTTOKEN with your Discord bot token you just created.
4. Enable the Server Members intent and the Message Content Intent in the developers portal. Should also unselect "Public Bot" in the developers portal as well.
5. FOR EACH CLIENT EVENT (Developers mode needs to be on for this step):
- At "guild = await client.fetch_guild(SERVERIDHERE)", replace SERVERIDHERE with the Server id your bot will be in
- At webhook = Webhook.from_url('WEBHOOKTOKEN', adapter=AsyncWebhookAdapter(session)), replace WEBHOOKTOKEN with the Webhook url (if you want the webhook)
- At mutedRole = discord.utils.get(ctx.guild.roles, name="ROLENAMEHERE"), replace ROLENAMEHERE with the name of the role you want the bot to give in your server.
6. Install discord.py (Included in the requirements file)
7. Run the bot
8. Set up the Joins/Leaves log channel with the setwchannel command
9. Run verifysetup if you need too
10. You should be done (I advise you test with an alt or with a friend to ensure you did everything correctly)

================================================

DISCLAIMER: THERE IS LITERALLY NO WARRENTY IF YOU DECIDE TO USE THIS SOURCE CODE. IF YOU DECIDE TO USE
THIS SOURCE CODE, IT IS TO BE USED AT YOUR OWN RISK! WE WILL NOT BE HELD LIABLE FOR DAMAGES!

================================================

CREDITS: https://stackoverflow.com/questions/64760333/how-to-set-a-welcome-channel-discord-py