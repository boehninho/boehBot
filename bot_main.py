import asyncio
import botFunctions #import botFunctions.py
import discord

_secrettoken: str = 'discord_api_token'
client = discord.Client()
_botchan: int = 699985778872287233

@client.event
async def on_ready():
    print('Bot ist eingeloggt als: {}'.format(client.user.name))
    await client.change_presence(activity=discord.Game(' an sich selbst herum!'), status=discord.Status.online)
    

@client.event
async def on_message(message):
    if message.author.bot:
        return

    if '!bottester' in message.content:
        message.channel = client.get_channel(_botchan)
        await message.channel.send('test')

    if '!help' in message.content:
        message.channel = client.get_channel(_botchan)
        await message.channel.send('**Anleitung zum boehBot**\r\n'
                                   '!beleidigen **NAME** - Beleidigt **NAME** maßlos.\r\n'
                                   '!witz - Erzählt einen lustigen Witz.\r\n'
                                   '!dice **NAME** - Rollt den Würfel mit **NAME**\r\n'
                                   '!wetter **STADT** - Gibt einen Wetterbericht aus\r\n'
                                   '!meme - Random MEOW Reddit Meme\r\n'
                                   '!apple - Fun Fact über Heino\r\n'
                                   '!fabi - Fabi an die Tuppenapp erinnern\r\n'
                                   '!xxx - Random XXX Picture *hr*')

    if '!beleidigen' in message.content:
        message.channel = client.get_channel(_botchan)
        split = message.content.split(' ')
        try:
            await message.channel.send('**' + split[1] + '** ' + botFunctions.getBeleidigung())
        except:
            pass

    if '!fabi' in message.content:
        message.channel = client.get_channel(_botchan)
        await message.channel.send('Fabian???\r\n'
                                   '**DENK AN DIE TUPPENAPP DU HUSO!!!**')
        await asyncio.sleep(1)
        await message.channel.send('**Fun Fact** - Fabian wurde bereits **' + botFunctions.erinnerungFabi(1) + '**x daran erinnert!')

    if '!witz' in message.content:
        message.channel = client.get_channel(_botchan)
        await message.channel.send(botFunctions.getWitze())

    if '!apple' in message.content:
        message.channel = client.get_channel(_botchan)
        await message.channel.send('**Heino** hat von Apple einfach keinen Plan :-(\r\n'
                                   '¡¡¡¡¡ kriegt nur er hin :-D')
    if '!xxx' in message.content:
        message.channel = client.get_channel(_botchan)
        getUrl = botFunctions.getPornPicture()
        await message.channel.send(getUrl)

    if '!dice' in message.content:
        message.channel = client.get_channel(_botchan)
        user1 = str(message.author).split('#')[0]
        user2 = str(message.content.split(' ')[1])

        getOutput = botFunctions.diceGame(user1, user2)

        await message.channel.send('**Das große Würfel hat begonnen!!** '
                                   '**{}** fordert **{}** heraus :-)'.format(user1, user2))
        await asyncio.sleep(3)
        await message.channel.send('**' + user1 + '** beginnt zu Würfeln..')
        await asyncio.sleep(2)
        await message.channel.send('**' + user1 + '** hat eine **' + getOutput[0] + '** gewürfelt, nicht schlecht!')
        await asyncio.sleep(2)
        await message.channel.send('**Die Spannung steigt ins Unermessliche...**')
        await asyncio.sleep(2)
        await message.channel.send('**' + user2 + '** hat eine **' + getOutput[1] + '** gewürfelt, nicht schlecht!')
        await asyncio.sleep(1)
        if getOutput[2] == 'none':
            await message.channel.send('**Unentschieden**, nächstes mal klappts bestimmt! :-P')
        else:
            await message.channel.send('Damit hat **' + getOutput[2] + '** gewonnen, Glückwunsch! :-)')

    if '!meme' in message.content:
        message.channel = client.get_channel(_botchan)
        await message.channel.send(botFunctions.getRandomMeme())

    if '!wetter' in message.content:
        message.channel = client.get_channel(_botchan)
        city = str(message.content.split(' ')[1])
        _buffer = botFunctions.getWetter(city)
        if _buffer is not None:
            await message.channel.send('Folgende Wetterinformation zu **{}** gefunden:\r\n'
                                       'Die **aktuelle Temperatur** liegt bei **{}°C**.\r\n'
                                       'Die **minimale Temperatur** lag bei **{}°C**.\r\n'
                                       'Die **maximale Temperatur** lag bei **{}°C**.\r\n'
                                       'Der **Wind** bläst mit **{}m/s** - Uiui!\r\n'.format(city, _buffer[0], _buffer[1], _buffer[2], _buffer[3]))

client.run(_secrettoken)
