import random
import discord
from discord.ext import commands, tasks
from itertools import cycle


client = commands.Bot(command_prefix = '+')
status = cycle(['Status 1', 'Status 2'])

@client.event
async def on_ready():
    change_status.start()
    print("hello")

@client.event
async def on_member_join(member):
    print(f'{member} joined UwU')

@client.event
async def on_member_remove(member):
    print(f'{member} we\'ll miss you (not really...)')

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')

@client.command(aliases=['8ball'])
async def _8ball(ctx, *, question):
    responses = ['It is certain.',
                 'It is decidedly so.',
                 'Without a doubt.',
                 'Yes - definitely.',
                 'You may rely on it.',
                 'As I see it, yes.',
                 'Most likely.',
                 'Outlook good',
                 'Yes.',
                 'Signs point to yes.',
                 'Reply hazy, try again.',
                 'Ask again later.',
                 'Better not tell you now.',
                 'Cannot predict now.',
                 'Concentrate and ask again.',
                 'Don\'t count on it.',
                 'My reply is no.',
                 'My sources say no',
                 'Outlook not so good.',
                 'Very doubtful.']
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')

@tasks.loop(seconds=10)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))

client.run('TOKEN')
