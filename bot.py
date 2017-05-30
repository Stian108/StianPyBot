import discord
from discord.ext import commands
import asyncio
import random

import config

bot = commands.Bot(command_prefix=config.PREFIX, self_bot=config.SELF_BOT)


@bot.event
async def on_ready():
    """Print details when the bot is ready."""
    print('Logged in as:')
    print('Username: ' + bot.user.name)
    print('ID: ' + bot.user.id)
    print('------')

'''
@bot.command(pass_context=True, alias="v")
@commands.has_role("Greeter")
async def verify(ctx, *, member: discord.Member):
    """Let a greeter give a user the Member role."""
    try:
        role = discord.utils.get(ctx.message.server.roles, name="Member")
        await bot.add_roles(member, role)
        await bot.say("Gave {} member!".format(member.name))
    except Exception:
        await bot.say("Couldn't make {} member...".format(member.name))
'''


@bot.command()
async def roll(dice: str):
    """Roll a dice in NdN format."""
    try:
        rolls = int(dice.split("d")[0])
        faces = int(dice.split("d")[1])
    except Exception:
        await bot.say("Must be in NdN format")
    result = []
    for i in range(rolls):
        result.append(str(random.randint(1, faces)))
    await bot.say("You rolled: {}".format(", ".join(result)))


bot.run(config.USER_TOKEN if config.SELF_BOT else config.BOT_TOKEN)
