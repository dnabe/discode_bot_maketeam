import discord
import time
import datetime

client = discord.Client()

@client.event
async def on_ready():
    print('ログインしました')

@client.event
async def on_message(message):


    #if message.author.id == '279562735635660800': #たくみんのid
        #reply = '<@&511936816677519382> たくみんが話したよ！' #くらくらサーバ

    if message.author.id == '433511130439090178': #鍋谷のid
        reply = '<@&458110776964808706> テスト' #テスト用
        #reply = 'test' #test

        msg = await client.send_message(message.channel,reply)
        time.sleep(5.0)
        await client.delete_message(msg)

client.run('NTExODk2MTE5NTY3OTc0NDAw.Dsxl7g.aFBgRs3aVBpCphX_czE30dQCOAw')
