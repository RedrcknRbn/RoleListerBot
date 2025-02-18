import discord
from discord.ext import commands
from discord import app_commands
import os

intents = discord.Intents.default()
intents.guilds = True
intents.guild_messages = True
intents.guilds = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')
    try:
        synced = await bot.tree.sync()
        print(f'Synced {len(synced)} command(s)')
    except Exception as e:
        print(e)

@bot.tree.command(name="listroles", description="Lists all roles in the server")
async def listRoles(interaction: discord.Interaction):
    roles = [role.name for role in interaction.guild.roles]
    await interaction.response.send_message("\n".join(roles))

bot_token = os.getenv('token')
if bot_token:
    bot.run(bot_token)
else:
    print("Error: token environment variable not set.")