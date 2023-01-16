import discord
from discord.ext import commands
from discord.ui import Select, View

class Scrim(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
    
    @commands.command()
    async def scrim(self, ctx): #targets scrim-lobby
        self.channel = self.bot.get_channel(1062581752209608755)
        self.captains = []
        self.team1_picks = []
        self.team2_picks = []
        # self.view = View(timeout=None)

        async def captains(self):
            members = [member.name for member in self.channel.members]
            member_options = list(map(lambda x: discord.SelectOption(label=x), members))
            cap_menu = Select(min_values=2, max_values=2, options=member_options)
            view = View(timeout=None)
            async def cap_callback(interaction):
                self.captains.clear()
                self.captains.extend(cap_menu.values)
                view.stop()
                await interaction.response.send_message(f"Captains are {self.captains[0]} and {self.captains[1]}")
                await picks(self)
        
            cap_menu.callback = cap_callback
            view.add_item(cap_menu)
            message = await ctx.send("Select Captains", view=view)

        async def picks(self):
            async def choices(self):
                members = [member.name for member in self.channel.members if member not in self.captains]
                return await list(map(lambda x: discord.SelectOption(label=x), members)) + ['Completed?']

            view = View(timeout=None)

            pick_menu_1 = Select(options=choices(self))
            pick_menu_2 = Select(options=choices(self))

            async def pick_callback_1(interaction):
                pick = pick_menu_1.values[0]
                if pick == "Completed":
                    view.stop()
                    await interaction.response.send_message(f"Teams picked")
                else:
                    self.team1_picks.append(pick)
                    view.remove_item(pick_menu_1)
                    view.add_item(pick_menu_2)

            async def pick_callback_2(interaction):
                    pick = pick_menu_2.values[0]
                    if pick == "Completed":
                        view.stop()
                        await interaction.response.send_message(f"Teams picked")
                    else:
                        self.team2_picks.append(pick)
                        view.remove_item(pick_menu_2)
                        view.add_item(pick_menu_1)

            pick_menu_1.callback = pick_callback_1
            pick_menu_2.callback = pick_callback_2
            view.add_item(pick_menu_1)
            # view.add_item(pick_menu_2)

        await captains(self)

async def setup(bot): 
    await bot.add_cog(Scrim(bot))