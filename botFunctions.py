import os
import random
import re
import requests


def getRandomMeme():
    _r1, _r2, _r3 = random.randint(0,9), random.randint(0,400), random.randint(0,400)
	#generate 'half'random header
    _reqmeme = requests.get("https://www.reddit.com/r/memes.json", headers={"User-Agent": "linux:discordbot:v" + str(_r1) + "." + str(_r2) + "." + str(_r3)})
    _json = _reqmeme.json()
    _randomurl = random.choice(_json["data"]["children"])["data"]["url"]
    return str(_randomurl)

def getPornPicture():
    _r1, _r2, _r3 = random.randint(0, 9), random.randint(0, 400), random.randint(0, 400)
    _pattern = r'<ima?ge?\s+[^>]*?data-src="([^"]+)'
    _random = random.randint(1, 200)
    _url = "https://www.youx.xxx/" + str(_random) + "/?order=popular"
    _req = requests.get(_url, headers={"User-Agent": "linux:discordbot:v" + str(_r1) + "." + str(_r2) + "." + str(_r3)})
    _imgurl: list = []

    for url in re.findall(_pattern, _req.text):
        _imgurl.append(url)

    _randomimg = random.randint(0, len(_imgurl))
    return _imgurl [_randomimg]

def erinnerungFabi(option):
    _readNumber = open(os.getcwd() + '\\data\\fabi.txt', 'r', encoding='utf-8')
    _aktuell = _readNumber.read().splitlines()[0]
    _readNumber.close()

    if option == 1:
        _replace = int(_aktuell) + 1
        _neu = open(os.getcwd() + '\\data\\fabi.txt', 'w', encoding='utf-8')
        _neu.write(str(_replace))
        _neu.close()
        return str(_replace)

def getWetter(city):
	_apikey: str = 'enter_api_key'
    _apiurl = 'https://api.openweathermap.org/data/2.5/weather?q=' + city + '&APPID=' + _apikey + '&units=metric'
    _apireq = requests.get(_apiurl)
    _apidata = _apireq.json()
    try:
        _temp = _apidata['main']['temp']
        _tempmin = _apidata['main']['temp_min']
        _tempmax = _apidata['main']['temp_max']
        _wind = _apidata['wind']['speed']
        return _temp, _tempmin, _tempmax, _wind
    except:
        return None


def getWitze():
    _holeWitze = open(os.getcwd() + '\\data\\witze.txt', 'r', encoding='utf-8')
    _witze: list = []
    for singleWitz in _holeWitze.read().splitlines():
        _witze.append(singleWitz)
    _holeWitze.close()

    _random = random.randint(0, len(_witze))
    return _witze[_random]

def getBeleidigung():
    _beleidigung: list = []
    _holeBeleidigung = open(os.getcwd() + '\\data\\beleidigen.txt', 'r', encoding='utf-8')
    for singleBeleidigung in _holeBeleidigung.read().splitlines():
        _beleidigung.append(singleBeleidigung)
    _holeBeleidigung.close()
    _random = random.randint(0, len(_beleidigung))
    return _beleidigung[_random]


def diceGame(user1, user2):
    dice1, dice2 = random.randint(1, 6), random.randint(1, 6)
    winner: str = ''

    if dice1 > dice2:
        winner = user1
    elif dice1 < dice2:
        winner = user2
    else:
        winner = 'none'

    return str(dice1), str(dice2), winner
