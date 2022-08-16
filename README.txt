WELCOME BOT WITH SLASH COMMANDS FOR DISCORD.PY

This source code allows you to welcome members while having Slash commands work. Now has support where you can
set up the bot for the Welcome module to work properly in multiple servers like what you see in bots like Dyno, Carl bot, etc
Meaning you can set up a welcome channel per server and it will welcome members in each server seperatly just like popular bots like Dyno.
Making this version more advanced then the last version.
No need to make a bunch of discord bots and hosting them seperatly anymore for each server

Includes:
- Sending messages in a desired text channel (New version now supports having one bot in multiple servers and welcomes members in your desired set channel for each server.)
- Gives a role to a member
- Sends a welcome message to a webhook
- DMs members upon joining the server
- Slash commands working with all of this.

================================================

REQUIREMENTS:
- Knowledge of Discord.py
- A discord bot application with token (with Server Members intent enabled)
- Python 3.8.6 or newer (Using a Python software version below this version may have a chance to cause issues or errors)

================================================

SETUP:
1. Fork or Download this Source code to your hosting provider (or computer if you wish to self-host it)
2. Create a Discord Bot Application and copy your bot token at https://discord.com/developers
3. At the bottom, replace DISCORDBOTTOKEN with your Discord bot token you just created.
4. Enable the Server Members intent in the developers portal. Should also unselect "Public Bot" in the developers portal as well.
5. MODIFICATIONS:
- At webhook = Webhook.from_url('WEBHOOKTOKEN', adapter=AsyncWebhookAdapter(session)), replace WEBHOOKTOKEN with the Webhook url (if you want the webhook)
- At mutedRole = discord.utils.get(ctx.guild.roles, name="ROLENAMEHERE"), replace ROLENAMEHERE with the name of the role you want the bot to give in your server.
6. Install discord.py and discord-py-slash-command
7. Run the bot (I advise you test with an alt or with a friend to ensure you did everything correctly)

You need to do nothing with the .json file. That file is already set to go.

SET UP BOT ON DISCORD.
1. Invite the bot to your server.
2. Use /setwchannel command to change which text channel you want the welcome message to be sent to.
3. Repeat Steps 1-2 for each server you want your bot it.
NOTE: The bot will not DM new members if you do not set up the role the bot gives unless you want to modify the code.

================================================

NOTE: This source code was designed to be made for private utility bots in a few servers.
You could have this a public bot but can not guarente proper working results.

If your bot stays unverified and enabled the Message Content intent, you may be able to use regular commands
instead.

DISCLAIMER: THERE IS LITERALLY NO WARRENTY IF YOU DECIDE TO USE THIS SOURCE CODE. IF YOU DECIDE TO USE
THIS SOURCE CODE, IT IS TO BE USED AT YOUR OWN RISK! WE WILL NOT BE HELD LIABLE FOR ANY DAMAGES WHAT SO EVER!

===============================================

CREDITS:
https://stackoverflow.com/questions/64760333/how-to-set-a-welcome-channel-discord-py
This help page is how I learned this.