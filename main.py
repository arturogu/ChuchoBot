import discord
import os
import random
from keep_alive import keep_alive

client = discord.Client()

cryEmoji = [
    "<:cry_bob:445120997016993803>", "<:cry_royo:445125067295424512>",
    "<:cry_shaak:445123994388135936>"
]
sleepEmoji = [
    "<:chucho_sleep:445132913667735552>", "<:roostygasm:445118699779784726>",
    "<:tia_tula:445117635831660544>"
]

sleepWords = ["zack snyder", "snyder cut", "justice league", "snyder"]

llaves = [
    "https://media.discordapp.net/attachments/768385029784993862/813593987519873024/Maldita_sea_2.gif",
    "https://media.discordapp.net/attachments/768385029784993862/813593905298931732/MalditaSea.gif"
]

pogg = ["pog", "Pog", "POG", "POg", "pOG", "PoG", "pOG", "poG"]

musk = ["elon", "Elon", "Musk", "musk"]

mendex = ["Mendex", "mendex"]

bob = [
    "<:smartass:445119911367409664>", "<:cry_bob:445120997016993803>",
    "<:bobxdidi:445129104392585236>", "<:bob13:817638288688414740>",
    "<:bob_wut:445130461866360834>", "<:bob_smile:445125856134823936>",
    "<:bob_ninja:445130068939898880>", "<:bob_ew:445130092989906971>",
    "<:bob_cry2:445130083745792001>", "<:banana_bob:445125088518471683>"
]

jackbox = [
    "quiplash", "survive the internet", "split the room", "mad verse city",
    "fibbage", "champ'd up", "drawfull", "trivia murder party", "jokeboat",
    "talking points"
]


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.author.name == 'AEROROCK182':
        await message.add_reaction("<:todomeco:780959558016434227>")

    if message.author.name == 'Elisa_i':
        await message.add_reaction("<:todomeco:780959558016434227>")

    if message.author.name == 'Dieg0350':
        await message.add_reaction("<:todomeco:780959558016434227>")
        await message.add_reaction("<:didi_magic:445130062598111232>")

    # if message.author.name in ('Cotepich1', 'Isai.Navarro', 'ElMemo'):
    #   await message.add_reaction("🖕")

    if message.content.startswith(('cual', 'Cual', 'cuál', 'Cuál')):
        await message.channel.send('Esta')

    if message.content.startswith('$caca'):
        await message.channel.send(":poop:")

    if message.content.startswith('$sillas'):
        await message.channel.send(
            "https://tenor.com/view/wrestling-throwing-chairs-lucha-libre-chairs-boo-gif-17986816"
        )

    if message.content.startswith('$malditasea'):
        await message.channel.send(random.choice(llaves))

    if message.content.startswith('$poggers'):
        await message.channel.send(
            "<:poggers:726940974114144256><:pogchuy:839951744850067578>")

    if message.content.startswith('$bob'):
        await message.channel.send(random.choice(bob))

    if message.content.startswith('$jackbox'):
        await message.channel.send(random.choice(jackbox))

    if message.content.startswith(('huele a', 'Huele a')):
        huele = message.content[8:]
        await message.channel.send("¿Qué es " + huele + "?")

    if any(word in message.content for word in sleepWords):
        await message.add_reaction(sleepEmoji[0])
        await message.add_reaction(sleepEmoji[1])
        await message.add_reaction(sleepEmoji[2])

    if any(word in message.content for word in pogg):
        await message.add_reaction("<:poggers:726940974114144256>")
        await message.add_reaction("<:pogchuy:839951744850067578>")

    if "twitter.com/anysutherlin" in message.content:
        await message.delete()
        await message.channel.send(
            "<:shutup:751981321626189904><:shutup:751981321626189904><:shutup:751981321626189904><:shutup:751981321626189904><:shutup:751981321626189904>"
        )

    if any(word in message.content for word in musk):
        await message.delete()

    if any(word in message.content for word in mendex):
        await message.add_reaction("<:todomeco:780959558016434227>")


@client.event
async def on_message_delete(message):
    await message.channel.send("No lo borre compa")


keep_alive()
client.run(os.getenv('TOKEN'))
