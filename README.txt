WELCOME BOT WITH SLASH COMMANDS FOR DISCORD.PY

This source code allows you to welcome members while having Slash commands work.
Includes:
- Sending messages in a desired text channel
- Gives a role to a member
- Sends a welcome message to a webhook
- DMs members upon joining the server
- Slash commands working with all of this.

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
4. Enable the Server Members intent in the developers portal. Should also unselect "Public Bot" in the developers portal as well.
5. FOR EACH CLIENT EVENT (Developers mode needs to be on for this step):
- At "channel = client.guilds[0].get_channel(CHANNELIDHERE)", replace CHANNELIDHERE with the channel id you want the bot to send the welcome and leave messages to.
- At "guild = await client.fetch_guild(SERVERIDHERE)", replace SERVERIDHERE with the Server id your bot will be in
- At webhook = Webhook.from_url('WEBHOOKTOKEN', adapter=AsyncWebhookAdapter(session)), replace WEBHOOKTOKEN with the Webhook url (if you want the webhook)
- At mutedRole = discord.utils.get(ctx.guild.roles, name="ROLENAMEHERE"), replace ROLENAMEHERE with the name of the role you want the bot to give in your server.
6. Install discord.py and discord-py-slash-command
7. Run the bot (I advise you test with an alt or with a friend to ensure you did everything correctly)

================================================

WARNING: THIS BOT IS INTENDED TO BE A PRIVATE BOT. THIS WILL NOT WORK AS A PUBLIC BOT OTHERWISE THE BOT GETS MESSED UP!

DISCLAIMER: THERE IS LITERALLY NO WARRENTY IF YOU DECIDE TO USE THIS SOURCE CODE. IF YOU DECIDE TO USE
THIS SOURCE CODE, IT IS TO BE USED AT YOUR OWN RISK! WE WILL NOT BE HELD LIABLE FOR DAMAGES!