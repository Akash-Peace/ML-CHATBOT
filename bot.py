import os
import sys
import time
import random
import imdb
import emoji
import discord
import calendar
import requests
import wikipedia
import pandas as pd
import numpy as np
import pyjokes as jk
#from discord.ext import commands
from bs4 import BeautifulSoup as bs
from datetime import datetime
from PyDictionary import PyDictionary
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
API_KEY = os.getenv('WEATHER_KEY')

client = discord.Client()
#bot = commands.Bot(command_prefix='!')

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

@client.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.text_channels, name="general")
    welimg1 = 'https://www.filmibeat.com/img/2013/10/11-1381464611-vc-review-01.jpg'
    welimg2 = 'https://www.southdreamz.com/wp-content/uploads/2011/03/vadivelu-wallpaper06.jpg'
    await channel.send(f'Welcome to our Channel, {member.name}  {emoji.emojize(":blue_heart:")}')
    await channel.send(welimg1)
    await channel.send(f'Welcome ceremony playing {emoji.emojize(":musical_note:")}{emoji.emojize(":musical_keyboard:")}{emoji.emojize(":saxophone:")}{emoji.emojize(":drum:")}{emoji.emojize(":musical_note:")}')
    await member.create_dm()
    await member.dm_channel.send(f'Hi {member.name},\n I am <@!747469629793894480>,\nwelcome to {member.guild.name}  {emoji.emojize(":folded_hands:")}')
    await member.dm_channel.send(welimg2)
    await member.dm_channel.send(f'Any help, Just type *"Help me becca"*  {emoji.emojize(":scroll:")}')


def usersname(message, m):
    i = 1
    l = []
    for member in message.guild.members:
        if m == 0:
            if member.bot == False:
                l.append(str(i) + '. ' + member.name)
                i = i + 1
        else:
            if member.bot == True:
                l.append(str(i) + '. ' + member.name)
                i = i + 1
    return l
def usersonline(message, m):
    i = 1
    l = []
    for member in message.guild.members:
        if m == 0:
            if member.status == discord.Status.online and not member.bot:
                l.append(str(i) + '. ' + member.name)
                i = i + 1
        else:
            if member.status == discord.Status.online and member.bot:
                l.append(str(i) + '. ' + member.name)
                i = i + 1
    return l

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    ops = sys.platform
    msg = message.content.lower()
    msg = msg.replace(' ', '')
    if msg in ['helpmebecca', 'helpkaro', 'helpmeakasha']:
        msg1 = discord.Embed(title=f'HELP  {emoji.emojize(":genie:")}', color=0xFFFFFF)
        msg1.add_field(name=f'* Today trending\n'
                            f'* Find frnds\n'
                            f'* Server members\n'
                            f'* Online members\n'
                            f'* <Eg:Alien> meaning\n'
                            f'* Current gold rate (or) Cgr\n'
                            f'* Covid19 updates\n'
                            f'* <Eg:2021><Eg:01> calendar\n'
                            f'* <Eg:Chennai> weather\n'
                            f'* <Eg:Mars> wiki\n',
                            value=f'+ *Shows Wikipedia results*', inline=False)
        msg1.add_field(name=f'* Tell me a joke\n* <Eg:Titanic> released year\n* My weight? my height <Eg:150> cm\n',
                       value=f'+ *This command guess ur weight according to ur height u provide.*\n  NOTE: *Guess only of age 18-50.*', inline=False)
        await message.channel.send(embed=msg1)
    if msg in ['hibro', 'hellobro', 'hi', 'hello', 'hida', 'higuys', 'helloguys', 'hey', 'heyguys', 'heybro']:
        replytohi = ['Hi bro', 'Namasthe gi', 'Hello bro', 'Vanakam nanba', 'Namaskaram']
        response = random.choice(replytohi)
        await message.channel.send(response)
    if msg in ['byebro', 'bye', 'byeda', 'byeguys']:
        replytobye = ['Bye bro', f'Bye  {emoji.emojize(":waving_hand:")}', 'Bye da']
        response = random.choice(replytobye)
        await message.channel.send(response)
    if msg in [f'beccatq', f'beccathanku', f'beccathankyou', f'beccathanks', f'beccanandri']:
        replytotq = [f'Welcome  {emoji.emojize(":smiling_face_with_heart-eyes:")}']
        response = random.choice(replytotq)
        await message.channel.send(response)
    if msg in ['todaytrending', 'trendingtoday']:
        await message.channel.send('https://getdaytrends.com/')
    if msg == 'findfrnds':
        await message.channel.send('https://friender.pythonanywhere.com')
    if msg in ['goodmorning', 'gm', 'gmguys', 'goodmorningguys']:
        replytohi = [
            'https://ahseeit.com/tamil/king-include/uploads/2019/04/fb_img_1554534638046-5374727696.jpg',
            'https://cdn.sharechat.com/13c8a77f_1570674188621.jpeg',
            'https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcT3xjyh_iYj6eXKDRwNiImnJTuVfJB3EDAupQ&usqp=CAU',
            'https://commentphotos.com/gallery/CommentPhotos.com_1406977362.jpg']
        response = random.choice(replytohi)
        await message.channel.send(response)
    if msg in ['goodnight', 'gn', 'gnguys', 'goodnightguys', 'gnsd']:
        replytohi = ['https://media1.tenor.com/images/04ede9041d740334e037e6ef0769538e/tenor.gif?itemid=10405283',
                     'https://media1.tenor.com/images/ccdbccf7c836d041939bbc8a9d9abf50/tenor.gif?itemid=12458779',
                     'https://i.pinimg.com/originals/51/60/18/51601818d4571dcd1da1430c4f756d95.gif',
                     'https://i.pinimg.com/564x/92/3e/a7/923ea75ec291588f24aec2eb2e9e67fe.jpg']
        response = random.choice(replytohi)
        await message.channel.send(response)
    if msg in ['servermembers', 'crewmembers', 'wonkru', 'akashagang'] and not isinstance(message.channel, discord.channel.DMChannel):
        botsInServerCount = sum(member.bot for member in message.guild.members)
        usersInServerCount = message.guild.member_count - botsInServerCount
        msg1 = discord.Embed(title=f'Frnds in {message.guild.name}  {emoji.emojize(":people_holding_hands:")}', color=0xFFFFFF)
        msg1.add_field(name=f'Total Users : {message.guild.member_count}', value=f'Humans : {usersInServerCount} / Bots : {botsInServerCount}', inline=False)
        msg1.add_field(name=f'Humans : ', value=('\n'.join(usersname(message, m=0))), inline=False)
        msg1.add_field(name=f'Bots : ', value=('\n'.join(usersname(message, m=1))), inline=False)
        await message.channel.send(embed=msg1)
    if msg in ['membersstatus', 'isanyoneonline', 'isanyoneonline?', 'isanyonealive', 'isanyonealive?', 'onlinemembers'] and not isinstance(message.channel, discord.channel.DMChannel):
        onlinehumans = sum(member.status == discord.Status.online and not member.bot for member in message.guild.members)
        onlinebot = sum(member.status == discord.Status.online and member.bot for member in message.guild.members)
        onlinetotal = sum(member.status == discord.Status.online for member in message.guild.members)
        msg1 = discord.Embed(title=f'{onlinetotal} Frnds in ONLINE  {emoji.emojize(":face_with_monocle:")}', color=0xFFFFFF)
        msg1.add_field(name=f'Humans : {onlinehumans}', value=('\n'.join(usersonline(message, m=0))), inline=False)
        msg1.add_field(name=f"Bots : {onlinebot}", value=('\n'.join(usersonline(message, m=1))), inline=False)
        await message.channel.send(embed=msg1)
    if msg[-2:] == f'{emoji.emojize(":pinching_hand:")}{emoji.emojize(":smiling_face_with_sunglasses:")}':
        await message.channel.send('https://static.toiimg.com/thumb/msid-73895124,width-800,height-600,resizemode-75,imgsize-125747,pt-32,y_pad-40/73895124.jpg')
        replytotq = ['Thalaivaaaaa', 'vaa macha vaa macha', 'thalapathy thalapathy yengal thalapathy thalapathy', 'Verithanam']
        response = random.choice(replytotq)
        await message.channel.send(f'@Akash A  {response}')
    if msg[-2:] == f'{emoji.emojize(":sweat_droplets:")}{emoji.emojize(":sweat_droplets:")}':
        await message.channel.send('https://www.fbphotocomment.in/wp-content/uploads/Santhanam-thu-thu-thu.jpg')
        replytotq = ['vekkama illa', 'ithalam oru pulapu', 'thuuu', 'keduketta echa']
        response = random.choice(replytotq)
        await message.channel.send(f'{msg[:-2]}  {response}')
    if msg[-2:] == f'{emoji.emojize(":expressionless_face:")}.':
        await message.channel.send('https://memees.in/funnyimages/memees.php?w=650&img=c2FudGhhbmFtL3NhbnRoYW5hbS1mYWNlLXJlYWN0aW9uLWZhY2Vib29rLTIwMTcwMzI3MDkyNDI3LmpwZw==')
        await message.channel.send(f'{msg[:-2]}  No commemts, Simply waste.')
    if msg == 'ithalamorunagaichuvaiya':
        await message.channel.send('Athaane...')
    if msg[-2:] == f'{emoji.emojize(":face_with_tears_of_joy:")}{emoji.emojize(":rolling_on_the_floor_laughing:")}':
        replytohi = ['https://pbs.twimg.com/media/DLxH_vjV4AE9lTW.jpg',
                     'https://1847884116.rsc.cdn77.org/tamil/news/maxresdefault_(3)-06e.jpg',
                     'https://i.ytimg.com/vi/JPLqP4ohCuY/hqdefault.jpg',
                     'https://memees.in/funnyimages/memees.php?w=650&img=dmFkaXZlbHUvbWFydWRoYW1hbGFpLWNvbWVkeS0tZmFjZWJvb2stMjAxNjAzMjUyMjI0NDIuanBn',
                     'https://media.istockphoto.com/photos/guy-with-hearty-laugh-picture-id471723865',
                     'https://media.gettyimages.com/photos/portrait-of-man-with-big-mouth-laughing-picture-id84439708',
                     'https://i2.wp.com/media1.giphy.com/media/l0MYunAI4j10uWbFm/giphy.gif?ssl=1',
                     'https://i.imgflip.com/eqwem.jpg',
                     'https://i.pinimg.com/originals/ef/04/13/ef0413d8b7a3bbc39431a27e58f08251.jpg',
                     'https://www.hub25.org/wp-content/uploads/2017/10/people-laughing-researchers-establish-mathematical-theory-of-humor-680x380.jpg']
        txt = [f'@Akash A  Vera lvl {emoji.emojize(":rolling_on_the_floor_laughing:")}{emoji.emojize(":face_with_tears_of_joy:")}{emoji.emojize(":rolling_on_the_floor_laughing:")}',
               f'@Akash A  Ultimate {emoji.emojize(":rolling_on_the_floor_laughing:")}{emoji.emojize(":face_with_tears_of_joy:")}{emoji.emojize(":rolling_on_the_floor_laughing:")}',
               f'@Akash A  Maranam {emoji.emojize(":rolling_on_the_floor_laughing:")}{emoji.emojize(":face_with_tears_of_joy:")}{emoji.emojize(":rolling_on_the_floor_laughing:")}',
               f'@Akash A  Hhahahahaha {emoji.emojize(":rolling_on_the_floor_laughing:")}{emoji.emojize(":face_with_tears_of_joy:")}{emoji.emojize(":rolling_on_the_floor_laughing:")}',
               f'@Akash A  {emoji.emojize(":rolling_on_the_floor_laughing:")}{emoji.emojize(":face_with_tears_of_joy:")}{emoji.emojize(":rolling_on_the_floor_laughing:")}{emoji.emojize(":face_with_tears_of_joy:")}{emoji.emojize(":rolling_on_the_floor_laughing:")}{emoji.emojize(":face_with_tears_of_joy:")}{emoji.emojize(":rolling_on_the_floor_laughing:")}{emoji.emojize(":face_with_tears_of_joy:")}']
        response = random.choice(replytohi)
        txt1 = random.choice(txt)
        await message.channel.send(response)
        await message.channel.send(txt1)
    if msg[:-5] == 'myweight?myheight' and msg[-2:] == 'cm':
        user_height = int(msg[-5:-2])
        dataset = pd.read_csv('height_weight.csv')
        #dataset.isnull().sum()
        x = dataset.iloc[:, 0:-1].values
        y = dataset.iloc[:, 1].values
        #np.isnan(x).sum()
        #np.isnan(y).sum()
        imputer = SimpleImputer(missing_values = np.nan, strategy = "mean")
        x = imputer.fit_transform(x)
        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=.30, random_state=0)
        regress = LinearRegression()
        regress.fit(x_train, y_train)
        #y_pred = regress.predict(x_test)
        user_height1 = [[user_height]]
        user_weight_prediction = regress.predict(user_height1)
        user_weight_prediction1 = str(user_weight_prediction)
        await message.channel.send(f'As per ur height({user_height} cm), Approx. ur weight is')
        msg1 = discord.Embed(title=f'{user_weight_prediction1[1:-10]} kg', color=0x7CFC00)
        await message.channel.send(embed=msg1)
        await message.channel.send(f'If my guess is right, Give me a {emoji.emojize(":thumbs_up:")}')
    if msg in ['tellmeajoke', 'jokeplz', 'telljoke']:
        msg1 = discord.Embed(title=jk.get_joke(), color=0xFFFFFF)
        await message.channel.send(embed=msg1)
    if msg[-7:] == 'meaning':
        pdt = PyDictionary()
        oxf = pdt.meaning(msg[:-7])
        msg1 = discord.Embed(title=f'{message.content[:-7]} MEANING', color=0xFFFFFF)
        msg1.add_field(name='\u200b', value=oxf, inline=False)
        await message.channel.send(embed=msg1)
    if msg in ['currentgoldrate', 'todaygoldrate', 'goldratetoday', 'cgr']:
        data = requests.get('https://www.goodreturns.in/gold-rates/')
        soup = bs(data.text, 'html.parser')
        cgr = soup.find('div', id = 'current-price').text
        msg1 = discord.Embed(title=cgr, color=0xFFFFFF)
        await message.channel.send(embed=msg1)
    if msg in ['iloveubecca', f'beccaloveudi{emoji.emojize(":heart_with_arrow:")}', f'beccaloveuchellam{emoji.emojize(":heart_with_arrow:")}', f'beccaloveudear{emoji.emojize(":heart_with_arrow:")}', f'becca,iloveu{emoji.emojize(":heart_with_arrow:")}']:
        if not isinstance(message.channel, discord.channel.DMChannel):
            own = str(message.guild.owner)
            if str(message.author) == own:
                await message.channel.send(f'Luv U toooo baby {emoji.emojize(":heart_with_ribbon:")}{emoji.emojize(":smiling_face_with_heart-eyes:")}{emoji.emojize(":face_blowing_a_kiss:")}{emoji.emojize(":kissing_face_with_closed_eyes:")}')
            else:
                await message.channel.send(f'No bro, I Luv {own},\nMe and {own} made for each other {emoji.emojize(":red_heart:")}')
        else:
            if str(message.author.id) == "747445770071965736":
                await message.channel.send(f'Luv U toooo baby {emoji.emojize(":heart_with_ribbon:")}{emoji.emojize(":smiling_face_with_heart-eyes:")}{emoji.emojize(":face_blowing_a_kiss:")}{emoji.emojize(":kissing_face_with_closed_eyes:")}')
            else:
                tagname = str(client.get_user(747445770071965736))
                await message.channel.send(f'Ithuku per thaan ECHA, I Luv {tagname[:-5]},\nMe and {tagname[:-5]} made for each other {emoji.emojize(":red_heart:")}')
    if msg[-4:] == 'wiki':
        pedia = wikipedia.summary(message.content[:-4], sentences=4)
        msg1 = discord.Embed(title=f'{message.content[:-4]} WIKIPEDIA', color=0xFFFFFF)
        msg1.add_field(name='\u200b', value=pedia, inline=False)
        await message.channel.send(embed=msg1)
    if msg in ['covid19updates', 'coronaupdates', 'covidupdates', 'covupd']:
        data = requests.get('https://www.worldometers.info/coronavirus/')
        soup = bs(data.text, 'html.parser')
        covid1 = soup.find('div', class_ ='maincounter-number').text
        covid = covid1[1:len(covid1)-2]
        others = soup.find_all("span", class_ = "number-table")
        recovered = others[2].text
        deaths1 = others[3].text
        deaths = deaths1[1:]
        msg1 = discord.Embed(title=f'Total cases : {covid}\nRecovered cases : {recovered}\nTotal deaths : {deaths}', color=0xFF0000)
        await message.channel.send(embed=msg1)
        await message.channel.send('Stay home! Stay safe! bro')
    if msg[-12:] == 'releasedyear':
        im = imdb.IMDb()
        search = im.search_movie(message.content[:-12])
        year = search[0]['year']
        title = search[0]['title']
        msg1 = discord.Embed(title=f'{title} : {str(year)}', color=0x7CFC00)
        await message.channel.send(embed=msg1)
    if msg[-7:] == 'weather':
        baseurl = "https://api.openweathermap.org/data/2.5/weather?"
        city = message.content[:-7]
        url = baseurl + "q=" + city + "&appid=" + API_KEY
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            main = data['main']
            temperature = main['temp']
            humidity = main['humidity']
            pressure = main['pressure']
            report = data['weather']
            msg1 = discord.Embed(title=f"{emoji.emojize(':cityscape:')}  Today's Weather", color=0x7CFC00)
            msg1.add_field(name=f"Temperature : {temperature}\nHumidity : {humidity}\nPressure : {pressure}\nWeather Report : {report[0]['description']}", value=f"{city:-^30}", inline=False)
            await message.channel.send(embed=msg1)
        else:
            await message.channel.send("Unpredictable!")
    if msg[-8:] == 'calendar':
        year, mon = int(msg[:4]), int(msg[4:6])
        dt = datetime.date(datetime.now())
        msg1 = discord.Embed(title=f'{emoji.emojize(":calendar:")}  CALENDAR', color=0xFFFFFF)
        msg1.add_field(name=calendar.month(year, mon), value=f"{str(dt):-^30}", inline=False)
        await message.channel.send(embed=msg1)
    if msg in ['aboutbecca', 'whoisbecca', 'whoisbecca?', 'beccanayaaru', 'beccanayaaruda', 'beccanaenna']:
        msg1 = discord.Embed(title=f'ABOUT BECCA  {emoji.emojize(":woman_scientist:")}', color=0xFFFFFF)
        msg1.add_field(name="Spoiler Alert: If u didn't watch *The 100* series, then major spoilers are here. Are u OK with it, then continue reading.",
                       value='Becca was a scientist who in 2051 creating A.L.I.E..\n'
                            'Fearing A.L.I.E., she decided to continue her research in space on her space station Polaris.\n'
                            'In addition to A.L.I.E., she created the Nightblood serum and a second version of the AI.\n'
                            'Later, Becca escaped Polaris just before it was destroyed and descended to Earth to become the first Commander.\n'
                            'The Commanders that come after her are also referred to as “Heirs of Bekka Pramheda” which indicates that she died.\n'
                            'Moreover, it has been confirmed that there can only be a new Commander when the current has died.\n'
                            'In Season Five, it was later revealed that Becca was burned alive by the Second Dawn cult members, led by Bill Cadogan.\n'
                            'Not much is known about Becca’s early life. At some point, she and Chris began working on the A.I. known as A.L.I.E..\n'
                            'She also developed Nightblood for the Eligius Mining Company. At 26, she found a pathway to access a human mind.\n', inline=False)
        msg1.add_field(name='\u200b', value='That same year, in 2051, she had to lock up A.L.I.E. because her answer for what was wrong with the world was too many people.\n'
                             'A year later, on May 10, 2052, Becca was aboard Polaris, trying to perfect A.L.I.E. 2.0, when A.L.I.E. caused the nuclear apocalypse.\n'
                             'Two years later, on October 1, 2054, the thirteen surviving space stations were coming together to form the Ark.\n'
                             'However, when Commander Cole McAdams found out about A.L.I.E. 2.0, he ordered Becca to destroy it.\n'
                             'Becca refused and instead implanted the AI within herself.\n'
                             'Moments before Alpha Station blows up Polaris, Becca uses an escape-pod to descend to Earth.\n'
                             'Becca landed not far from the Second Dawn Bunker in the rubble of a city which would later become Polis.\n'
                             'She was met by several cult members wearing hazmat suits. Even though she offered them the Nightblood serum,\n'
                             'the cult decided to kill her by burning her at the stake, on the orders of Bill Cadogan.\n'
                             '(For more info: Watch *The 100*)', inline=False)
        msg1.add_field(name='“The goal isn’t everything, A.L.I.E.\n'
                            'How you reach the goal matters, too.\n'
                            'I’m sorry that I didn’t teach you that.”\n'
                            ' – Becca, to A.L.L.I.E',value=f"{'The 100':-^30}",inline=False)
        await message.channel.send(embed=msg1)
        await message.channel.send('https://vignette.wikia.nocookie.net/thehundred/images/6/61/The100_S3_Perverse_Instantiation_2_Becca.jpg/revision/latest/top-crop/width/300/height/300?cb=20160529204014')
        await message.channel.send('This is my Short Story!')


@client.event
async def on_error(event, *args, **kwargs):
    with open('err.log', 'a') as f:
        if event == 'on_message':
            f.write(f'Unhandled message: {args[0]}\n')
        else:
            raise

client.run(TOKEN)

'''@bot.command(name='99')https://getdaytrends.com/
async def nine_nine(ctx):
    brooklyn_99_quotes = [
        'I\'m the human form of the 💯 emoji.',
        'Bingpot!',
        (
            'Cool. Cool cool cool cool cool cool cool, '
            'no doubt no doubt no doubt no doubt.'
        ),
    ]

    response = random.choice(brooklyn_99_quotes)
    await ctx.send(response)
print("bot on")
bot.run(TOKEN)
'''
