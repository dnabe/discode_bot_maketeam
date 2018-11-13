import discord
import time

client = discord.Client()

@client.event
async def on_ready():
    print('ログインしました')

@client.event
async def on_message(message):

    #if message.author.id == '279562735635660800': #たくみんのid
    if message.author.id == '433511130439090178': #鍋谷のid
        reply = '<@&458110776964808706> たくみんが話したよ！' #テスト用
        #reply = '<@&511936816677519382> たくみんが話したよ！' #くらくらサーバ
        #reply = '<@324831068412706816> <@268972787601899539> <@379326250717544450> <@381641619239338005> <@336050839556849664> <@335385731071475714> <@322690513507581952> <@287753691270742016> <@448872826187808768> たくみんが話したよ！'
        msg = await client.send_message(message.channel,reply)
        time.sleep(5.0)
        await client.delete_message(msg)

client.run('NTExODk2MTE5NTY3OTc0NDAw.Dsxl7g.aFBgRs3aVBpCphX_czE30dQCOAw')
