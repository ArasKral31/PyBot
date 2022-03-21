import os
import discord
from discord import *
from discord.ext import *
from discord.ext import commands
from time import *
from random import randint as r
from cryptography.fernet import Fernet

intents = discord.Intents(messages=True, guilds=True,
                          reactions=True, members=True, presences=True)
bot = commands.Bot(command_prefix="!", intents=intents)

try:
   token_dir = open('token.token')
   token_file=token_dir.read()
   token = token_file
except:
   print('Didnt find file named "token.token" please create file and write token inside')

   
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name="Oyun "))
    print("ben hazırım")


@bot.event
async def on_member_join(member):
    channel = discord.utils.get(
        member.guild.text_channels, name="hos-geldiniz")
    await channel.send(f"{member} aramıza katıldı. Hoş geldi!")
    role = discord.utils.get(member.server.roles, name="Kayıtsız")
    await bot.add_roles(member, role)


@bot.event
async def on_member_remove(member):
    channel = discord.utils.get(member.guild.text_channels, name="gorusuruz")
    await channel.send(f"{member} aramızdan ayrıldı : (")


@bot.command()
async def test(ctx):
    await ctx.send('test başarılı')
    print("Birisi 'test' komudunu kullandı")


@bot.command(aliases=["oyun", "game", "zarat", "zar"])
async def roll(ctx):
    await ctx.send("Zar atılıyor ...")
    sleep(1.2)
    await ctx.send(str(roll_dice())+' geldi')


@bot.command()
async def clear(ctx, amount=99999):
    await ctx.channel.purge(limit=amount)
    await ctx.send(str(amount)+' mesaj silindi')
    print("birisi 'clear' komutunu kullandı \n "+str(amount) + ' mesaj silindi')


@bot.command(aliases=["copy"])
@commands.has_role("Administrator")
async def channel_copy(ctx, amount=1):
    for i in range(amount):
        await ctx.channel.clone()
    await ctx.send('kopyalama başarılı')
    print(f'!copy kullanıldı , {str(amount)} kere kopyalandı')


@bot.command(aliases=["at", "gönder"])
@commands.has_role("Administrator")
async def kick(ctx, member: discord.Member, *args, pr="Yok"):
    await member.kick(reason="Yok")
    await ctx.send(str(member)+' sunucudan atıldı')


@commands.has_role("Administrator")
@bot.command()
async def ban(ctx, member: discord.Member, pr="Yok"):
    await member.ban(reason="Yok")
    await ctx.send(str(member)+' sunucudan banlandı')


@bot.command()
async def durum(ctx, durum=""):
    await bot.change_presence(activity=discord.Game(name=durum+" "))
    await ctx.send(f'durum "{durum} oynuyor" olarak değiştirildi')



    








@bot.command(aliases=["memegonder","sakayap","saka","şaka","memeat","memetest"])
async def meme(ctx):
    rnd = r(0, 17)
    if rnd==1:
        with open('meme1.png', 'rb') as f:
            picture = discord.File(f)
            await ctx.send(file=picture)
    elif rnd==2:
        with open('meme2.png', 'rb') as f:
            picture = discord.File(f)
            await ctx.send(file=picture)
    elif rnd==3:
        with open('meme3.png', 'rb') as f:
            picture = discord.File(f)
            await ctx.send(file=picture)
    elif rnd==4:
        with open('meme4.png', 'rb') as f:
            picture = discord.File(f)
            await ctx.send(file=picture)
    elif rnd==5:
        with open('meme5.png', 'rb') as f:
            picture = discord.File(f)
            await ctx.send(file=picture)
    elif rnd==6:
        with open('meme6.png', 'rb') as f:
            picture = discord.File(f)
            await ctx.send(file=picture)
    elif rnd==7:
        with open('meme7.png', 'rb') as f:
            picture = discord.File(f)
            await ctx.send(file=picture)
    elif rnd==8:
        await ctx.send("Insanları bir oyundan çalıntı bir fikirle gaza getirip paralarını çal ve yurt dışına kaç : ")
        with open('meme8.png', 'rb') as f:
            picture = discord.File(f)
            await ctx.send(file=picture)
    elif rnd==9:
        await ctx.send("izlediğin filmde 1 saniyeline +18 sahne gelmiştir : ")
        with open('meme9.png', 'rb') as f:
            picture = discord.File(f)
            await ctx.send(file=picture)
    elif rnd==10:
        await ctx.send("Akşam 3'te acıkmışsındır : ")
        with open('meme10.png', 'rb') as f:
            picture = discord.File(f)
            await ctx.send(file=picture)
    elif rnd==11:
        with open('meme11.jpg', 'rb') as f:
            picture = discord.File(f)
            await ctx.send(file=picture)
    elif rnd==12:
        with open('meme12.png', 'rb') as f:
            picture = discord.File(f)
            await ctx.send(file=picture)
    elif rnd==13:
        with open('meme13.jpg', 'rb') as f:
            picture = discord.File(f)
            await ctx.send(file=picture)
    elif rnd==14:
        with open('meme14.jpg', 'rb') as f:
            picture = discord.File(f)
            await ctx.send(file=picture)
    elif rnd==15:
        with open('meme15.jpg', 'rb') as f:
            picture = discord.File(f)
            await ctx.send(file=picture)
    elif rnd==15:
        with open('meme15.jpg', 'rb') as f:
            picture = discord.File(f)
            await ctx.send(file=picture)
    elif rnd==16:
        with open('meme16.jpg', 'rb') as f:
            picture = discord.File(f)
            await ctx.send(file=picture)
    else:
        with open('meme17.jpg', 'rb') as f:
            picture = discord.File(f)
            await ctx.send(file=picture)


@bot.command()
async def tokenbul(ctx, kisitokeni=""):
   with open('nah!.gif', 'rb') as f:
      picture = discord.File(f)
      await ctx.send(f'{kisitokeni} kişisinin tokeni bulundu \n TOKEN : ')
      await ctx.send(file=picture)

    
@staticmethod
def roll_dice():
    return r(0, 6)


bot.run(token)
