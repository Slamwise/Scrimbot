import discord
from discord.ext import commands
from discord.ui import Select, View

class Scrim(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
    
    @commands.command()
    async def scrim(self, ctx): #targets scrim-lobby
        channel = self.bot.get_channel(1062581752209608755)
        members = [member.name for member in channel.members]
        member_options = list(map(lambda x: discord.SelectOption(label=x), members))

        menu = Select(options=member_options)

        async def cap1_callback(interaction):
            await interaction.response.send_message()
        view = View()
        view.add_item(menu)

        message = await ctx.send("Select Captain 1", view=view)

async def setup(bot):
    await bot.add_cog(Scrim(bot))