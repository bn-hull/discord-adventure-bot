# setup boilerplate for discord.py
# these are exodependencies

import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
from adventure_bot.storage import (
    transform_story_data_to_json,
    populate_story_data_from_json,
)
from adventure_bot.story_data import StoryData
from adventure_bot.story_generation import replace_text, StoryGenerator
import random


intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix="!", intents=intents)

json_file_db = open("db.json", "r")
story_data = populate_story_data_from_json(json_file_db.read())
json_file_db.close()

story_generator = StoryGenerator("$PERSON", "$PLACE", "$THING")


def overwrite_json(json_file, to_write):
    with open(json_file, "w") as file_to_write:
        file_to_write.write(to_write)


@bot.command()
async def add_person(ctx, arg):
    story_data.add_person(arg)
    overwrite_json("db.json", transform_story_data_to_json(story_data))

    await ctx.send("Added person: " + arg)


@bot.command()
async def add_place(ctx, arg):
    story_data.add_place(arg)
    overwrite_json("db.json", transform_story_data_to_json(story_data))

    await ctx.send("Added place: " + arg)


@bot.command()
async def add_story(ctx, arg):
    story_data.add_place(arg)
    overwrite_json("db.json", transform_story_data_to_json(story_data))

    await ctx.send("Added story: " + arg)


@bot.command()
async def add_thing(ctx, arg):
    story_data.add_place(arg)
    overwrite_json("db.json", transform_story_data_to_json(story_data))

    await ctx.send("Added thing: " + arg)


@bot.command()
async def generate_story(ctx):
    story = ""
    try:
        story = story_generator.generate_story(
            random.shuffle(story_data.story_list)[0],
            random.shuffle(story_data.person_list),
            random.shuffle(story_data.place_list),
            random.shuffle(story_data.thing_list),
        )
    except:
        await ctx.send("Not enough data")
        return

    await ctx.send(story)


if __name__ == "__main__":
    load_dotenv()
    TOKEN = os.getenv("DISCORD_TOKEN")
    try:
        bot.run(TOKEN)
    except:
        print("Invalid token. Enter proper token in .env file under DISCORD_TOKEN")
