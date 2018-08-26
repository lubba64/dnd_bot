#imports

#bot imports

import random
import asyncio
import aiohttp
import json
from discord import Game
from discord.ext.commands import Bot
import sys, pygame
import time
import os

#krist imports

import races

#variables

number_of_people=0
number_of_people2=0
identification_iterator=0

#lists

char_sheets=[]
grid=[]
Letters=(
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z"
)
#classes

class Charachter():
    def __init__(self,dude,hp,wp,sp,dp,pp,lp,cp,mp,fp,name,race,subrace,Class,Subclass,level,skp,deaths,copper):
        self.dude=dude
        self.hp=hp
        self.wp=wp
        self.sp=sp
        self.dp=dp
        self.pp=pp
        self.lp=lp
        self.cp=cp
        self.mp=cp
        self.fp=fp
        self.name=name
        self.Class=Class
        self.Subclass=Subclass
        self.race=race
        self.subrace=subrace
        self.level=level
        self.skp=skp
        self.deaths=deaths
        self.copper=copper
        self.pts=90

class letter():
    def __init__(self,x,y,img):
        self.x=x
        self.y=y
        self.img=img

#misc function
def set_points(i):
    char_sheets[i].pts=90
    char_sheets[i].pts-=int(char_sheets[i].hp)
    char_sheets[i].pts-=int(char_sheets[i].wp)
    char_sheets[i].pts-=int(char_sheets[i].sp)
    char_sheets[i].pts-=int(char_sheets[i].dp)
    char_sheets[i].pts-=int(char_sheets[i].pp)
    char_sheets[i].pts-=int(char_sheets[i].lp)
    char_sheets[i].pts-=int(char_sheets[i].cp)
    char_sheets[i].pts-=int(char_sheets[i].mp)
    char_sheets[i].pts-=int(char_sheets[i].fp)

#pygame setup

size = width, height =  395, 425
screen = pygame.display.set_mode(size)
black=0,0,0
dim="14,11"

#botstuff
BOT_PREFIX = ("?", "!")
TOKEN = "NDgwMTU2NDQ5MDgzODgzNTQw.DltKEA.j_M6TbR5BmDCs2TmRMOHrZsDAW4"  # Get at discordapp.com/developers/applications/me
client = Bot(command_prefix=">")
char_sheets.append(Charachter("ExamplePerson#0000",10,10,10,10,10,10,10,10,10,"name","race","subrace","class","subclass",0,0,0,0)) #sets playing game
@client.event
async def on_ready():
    await client.change_presence(game=Game(name=">help"))


@client.command(name='stream',
                description="tells you the stream page",
                pass_context=True)
async def stream_page():
    await client.say()


@client.command(name='newchar',
                description="makes a new charachter sheet",
                pass_context=True)
async def New_Char(context):
    global identification_iterator
    for i in range(0,len(char_sheets)):
        if char_sheets[i].dude==context.message.author:
            await client.say("you already have a charachter sheet")
            identification_iterator=0
            pass
        else:
            identification_iterator+=1
    if identification_iterator==len(char_sheets):
        await client.say("new charachter sheet has been made")
        char_sheets.append(Charachter(context.message.author,0,0,0,0,0,0,0,0,0,None,None,None,None,None,0,0,0,0))
    identification_iterator=0

@client.command(name='resetchar',
                description="resets a charachter sheet",
                pass_context=True)
async def Charachter_Sheet(context):
    for i in range(0,len(char_sheets)):
        identification_iterator+=1
        if context.message.author==char_sheets[i].dude:
            char_sheets[i].hp=0
            char_sheets[i].wp=0
            char_sheets[i].sp=0
            char_sheets[i].dp=0
            char_sheets[i].pp=0
            char_sheets[i].lp=0
            char_sheets[i].cp=0
            char_sheets[i].mp=0
            char_sheets[i].fp=0
            char_sheets[i].name=None
            char_sheets[i].race=None
            char_sheets[i].subrace=None
            char_sheets[i].Class=None
            char_sheets[i].subclass=None
            char_sheets[i].level=0
            char_sheets[i].skp=0
            char_sheets[i].deaths=0
            char_sheets[i].copper=0
            await client.say("charachter sheet has been reset")
    if identification_iterator==len(char_sheets):
        await client.say("you dont have a charachter sheet")
    identification_iterator=0

@client.command(name='set',
                description="sets stats in your charachter sheet",
                pass_context=True)
async def setSTAT(context,STAT,POINTS):
    global identification_iterator
    for i in range(0,len(char_sheets)):
        if char_sheets[i].dude==context.message.author:
            if STAT.lower()=="hp":
                char_sheets[i].hp=POINTS
                set_points(i)
                if char_sheets[i].pts<0:
                    await client.say("you have run out of spendable points. hp set to 0")
                    char_sheets[i].hp=0
                    set_points(i)
                else:
                    await client.say("hp has been set to "+str(POINTS))
                identification_iterator=0
            elif STAT.lower()=="wp":
                char_sheets[i].wp=POINTS
                set_points(i)
                if char_sheets[i].pts<0:
                    await client.say("you have run out of spendable points. wp set to 0")
                    char_sheets[i].wp=0
                    set_points(i)
                else:
                    await client.say("wp has been set to "+str(POINTS))
                identification_iterator=0
            elif STAT=="sp":
                char_sheets[i].sp=POINTS
                set_points(i)
                if char_sheets[i].pts<0:
                    await client.say("you have run out of spendable points. sp set to 0")
                    char_sheets[i].sp=0
                    set_points(i)
                else:
                    await client.say("sp has been set to "+str(POINTS))
                identification_iterator=0
            elif STAT=="dp":
                char_sheets[i].dp=POINTS
                set_points(i)
                if char_sheets[i].pts<0:
                    await client.say("you have run out of spendable points. dp set to 0")
                    char_sheets[i].dp=0
                    set_points(i)
                else:
                    await client.say("dp has been set to "+str(POINTS))
                identification_iterator=0
            elif STAT=="pp":
                char_sheets[i].pp=POINTS
                set_points(i)
                if char_sheets[i].pts<0:
                    await client.say("you have run out of spendable points. pp set to 0")
                    char_sheets[i].pp=0
                    set_points(i)
                else:
                    await client.say("pp has been set to "+str(POINTS))
                identification_iterator=0
            elif STAT=="lp":
                char_sheets[i].lp=POINTS
                set_points(i)
                if char_sheets[i].pts<0:
                    await client.say("you have run out of spendable points. lp set to 0")
                    char_sheets[i].lp=0
                    set_points(i)
                else:
                    await client.say("lp has been set to "+str(POINTS))
                identification_iterator=0
            elif STAT=="cp":
                char_sheets[i].cp=POINTS
                set_points(i)
                if char_sheets[i].pts<0:
                    await client.say("you have run out of spendable points. cp set to 0")
                    char_sheets[i].cp=0
                    set_points(i)
                else:
                    await client.say("cp has been set to "+str(POINTS))
                identification_iterator=0
            elif STAT=="mp":
                char_sheets[i].mp=POINTS
                set_points(i)
                if char_sheets[i].pts<0:
                    await client.say("you have run out of spendable points. mp set to 0")
                    char_sheets[i].mp=0
                    set_points(i)
                else:
                    await client.say("mp has been set to "+str(POINTS))
                identification_iterator=0
            elif STAT=="fp":
                char_sheets[i].fp=POINTS
                set_points(i)
                if char_sheets[i].pts<0:
                    await client.say("you have run out of spendable points.fp set to 0")
                    char_sheets[i].fp=0
                    set_points(i)
                else:
                    await client.say("fp has been set to "+str(POINTS))
                identification_iterator=0
            else:
                await client.say("that isnt a valid stat. stats are:hp,wp,sp,dp,pp,lp,cp,mp, and fp")
        else:
            identification_iterator+=1
    if identification_iterator==len(char_sheets):
        await client.say("you dont have a sheet yet")
    identification_iterator=0

@client.command(name='showchar',
                description="displays your charachter sheet",
                pass_context=True)
async def Show_Char(context):
    global identification_iterator
    for i in range(0,len(char_sheets)):
        if char_sheets[i].dude==context.message.author:
            await client.say("""
            your charachter sheet is:
            name:{0}
            race:{1}
            subrace{13}
            class{2}
            subclass:{3}
            health:{4}
            wisdom:{5}
            speed:{6}
            detection:{7}
            power:{8}
            leader:{9}
            charge:{10}
            mana:{11}
            fourtune:{12}
            """.format(char_sheets[i].name,
            char_sheets[i].race,
            char_sheets[i].Class,
            char_sheets[i].Subclass,
            char_sheets[i].hp,
            char_sheets[i].wp,
            char_sheets[i].sp,
            char_sheets[i].dp,
            char_sheets[i].pp,
            char_sheets[i].lp,
            char_sheets[i].cp,
            char_sheets[i].mp,
            char_sheets[i].fp,
            char_sheets[i].subrace))
            identification_iterator=0
        else:
            identification_iterator+=1
    if identification_iterator==len(char_sheets):
        await client.say("you dont have a charachter sheet")
    identification_iterator=0

@client.command(name='setname',
                description="sets your name",
                pass_context=True)
async def Set_Name(context,name):
    global identification_iterator
    for i in range(0,len(char_sheets)):
        identification_iterator+=1
        if char_sheets[i].dude==context.message.author:
            char_sheets[i].name=name
            await client.say("your name has been set to "+char_sheets[i].name)
        if identification_iterator==len(char_sheets):
            await client.say("you dont have a charachter sheet yet.")
    identification_iterator=0

@client.command(name='setrace',
                description="sets your race",
                pass_context=True)
async def Set_Race(context,race):
    global identification_iterator
    for i in range(0,len(char_sheets)):
        identification_iterator+=1
        if char_sheets[i].dude==context.message.author:
            if race in races.Races:
                char_sheets[i].race=race
                await client.say("your race has been set to "+char_sheets[i].race)
            else:
                await client.say("that isnt a valid race.")
        if identification_iterator==len(char_sheets):
            await client.say("you dont have a charachter sheet yet.")
    identification_iterator=0

@client.command(name='setsubrace',
                description="sets your subrace(leave blank if you dont want to be a hybrid)",
                pass_context=True)
async def Set_Subrace(context,subrace):
    global identification_iterator
    for i in range(0,len(char_sheets)):
        identification_iterator+=1
        if char_sheets[i].dude==context.message.author:
            if subrace in races.Races:
                char_sheets[i].subrace=subrace
                await client.say("your subrace has been set to "+char_sheets[i].subrace)
            else:
                await client.say("that isnt a valid subrace.")
        if identification_iterator==len(char_sheets):
            await client.say("you dont have a charachter sheet yet.")
    identification_iterator=0

@client.command(name='setclass',
                description="sets your class",
                pass_context=True)
async def Set_Class(context,Class):
    global identification_iterator
    for i in range(0,len(char_sheets)):
        identification_iterator+=1
        if char_sheets[i].dude==context.message.author:
            char_sheets[i].Class=Class
            await client.say("your class has been set to "+char_sheets[i].Class)
        if identification_iterator==len(char_sheets):
            await client.say("you dont have a charachter sheet yet.")
    identification_iterator=0

@client.command(name='setsubclass',
                description="sets your subclass",
                pass_context=True)
async def Set_Subclass(context,Sub_class):
    global identification_iterator
    for i in range(0,len(char_sheets)):
        identification_iterator+=1
        if char_sheets[i].dude==context.message.author:
            char_sheets[i].Subclass=Sub_class
            await client.say("your subclass has been set to "+char_sheets[i].Subclass)
        if identification_iterator==len(char_sheets):
            await client.say("you dont have a charachter sheet yet.")
    identification_iterator=0

@client.command(name='ptsleft',
                description="displays the number of points you have left to spend on stats",
                pass_context=True)
async def points_left(context):
    global identification_iterator
    for i in range(0,len(char_sheets)):
        identification_iterator+=1
        if char_sheets[i].dude==context.message.author:
            await client.say("you have "+str(char_sheets[i].pts)+" left")
        if identification_iterator==len(char_sheets):
            await client.say("you dont have a charachter sheet yet.")
    identification_iterator=0

@client.command(name='randomchar',
                description="picks a random charachter sheet (krist gods only function)",
                pass_context=True)
async def randomcharas(context):
    global identification_iterator
    chargrabbed=False
    I=None
    if "gods of krist" in [y.name.lower() for y in context.message.author.roles]:
        if not len(char_sheets)==1:
            while chargrabbed==False:
                I=random.randint(0,len(char_sheets)-1)
                if not char_sheets[I].name==None and not char_sheets[I].race==None and not char_sheets[I].Class==None and not char_sheets[I].Subclass==None:
                    if char_sheets[I].pts==0:

                        await client.say("""
                        random char from {13}:
                        name:{0}
                        race:{1}
                        class{2}
                        subclass:{3}
                        health:{4}
                        wisdom:{5}
                        speed:{6}
                        detection:{7}
                        power:{8}
                        leader:{9}
                        charge:{10}
                        mana:{11}
                        fourtune:{12}
                        """.format(char_sheets[I].name,
                        char_sheets[I].race,
                        char_sheets[I].Class,
                        char_sheets[I].Subclass,
                        char_sheets[I].hp,
                        char_sheets[I].wp,
                        char_sheets[I].sp,
                        char_sheets[I].dp,
                        char_sheets[I].pp,
                        char_sheets[I].lp,
                        char_sheets[I].cp,
                        char_sheets[I].mp,
                        char_sheets[I].fp,
                        char_sheets[I].dude))
                        identification_iterator=0
                    else:
                        chargrabbed=False
                else:
                    chargrabbed=False
        else:
            await client.say("there are no players.")
    else:
        await client.say("you arent elligible to use this command. you must be a god of krist.")

@client.command(name='playernum',
                description="displays number of players in session",
                pass_context=True)
async def num_players():
    global number_of_people2
    for i in range(0,len(char_sheets)):
        number_of_people2+=1
    await client.say(number_of_people2)

async def num_players_console():
    await client.wait_until_ready()
    number_of_people=-1
    while not client.is_closed:
        number_of_people=-1
        for i in range(0,len(char_sheets)):
            number_of_people+=1
        print("Current number of players:"+str(number_of_people))
        await asyncio.sleep(100)

async def stream_display():
    screen.fill(black)
    for i in range(0,11):
        for e in range(0,14):
            grid.append(letter(e*40,i*40,54))
            grid[-1].img = "A.png"
            grid[-1].a = pygame.image.load(grid[-1].image)
            grid[-1].a = pygame.transform.scale(grid[-1].a,(40,40))
            screen.blit(grid[-1].a,grid[-1].rect)

client.loop.create_task(stream_display())
client.loop.create_task(num_players_console())
client.run(TOKEN)

