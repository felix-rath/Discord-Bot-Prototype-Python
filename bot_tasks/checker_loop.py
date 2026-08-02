from discord.ext import tasks
import tokens
import datetime

class CheckerLoop:

    LOOP_INTERVAL = 1 # In minutes

    def __init__(self, bot):
        self.bot = bot
        

    @tasks.loop(minutes=LOOP_INTERVAL)
    async def checker_loop(self):
        print("Waiting for check!")
        text = await self.bot.checker.check()
        print("Check finished!")
        text = text.lower()

        found = False
        for word in tokens.KEYWORDS:
            if word.lower() in text:
                print(f"Found keyword: {word}")
                self.bot.is_queue = True
                found = True
                await self.sendPM()
                print("PMs sended!")

        if found is False:
            print("No keyword found!")

    async def sendPM(self):
        guild = self.bot.client.get_guild(tokens.SERVER_ID)
        role = guild.get_role(tokens.ROLE_ID)

        for member in role.members:
            time = datetime.datetime.now().strftime("%H:%M")
            await member.send(f"Drop um: {time}")