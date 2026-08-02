import tokens

async def send_pm(bot):
    guild = bot.client.get_guild(tokens.SERVER_ID)
    role = guild.get_role(tokens.ROLE_ID)
    for member in role.members:
        await member.send("Drop gefunden!")