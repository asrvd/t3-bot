import discord
from discord.ext import commands
from .utils import return_issue_or_pr
from dotenv import load_dotenv
import os

load_dotenv()

token = os.getenv('TOKEN')

intents = discord.Intents.default()
intents.members = True
intents.guilds = True
intents.messages = True
intents.message_content = True

client = commands.Bot(
    command_prefix=commands.when_mentioned_or("."),
    case_insensitive=True,
    intents=intents,
)


@client.event
async def on_ready():
    print("Logged in as")
    print(client.user.name)
    print(client.user.id)
    print("------")
    await client.change_presence(status=discord.Status.online)


@client.event
async def on_message(message):
    if message.author.bot or message.author.id == client.user.id:
        return
    all_urls = f""
    for word in message.content.split():
        if word.startswith("#"):
            issue_id = word[1:]
            if issue_id.isdigit():
                issue_url = return_issue_or_pr(issue_id)
                if issue_url:
                    all_urls += f"#{issue_id} <{issue_url}>\n"
    if all_urls:
        await message.reply(all_urls, allowed_mentions=discord.AllowedMentions.none())
    await client.process_commands(message)


client.run(token)
