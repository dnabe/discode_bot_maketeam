import discord

client = discord.Client()

@client.event
async def on_ready():
    print('ログインしました')

@client.event
async def on_message(message):

    if message.author.id == '279562735635660800':
        reply = '<@324831068412706816> <@268972787601899539> <@379326250717544450> <@381641619239338005> <@336050839556849664> <@335385731071475714> <@322690513507581952> <@287753691270742016> <@448872826187808768> たくみんが話したよ！'
        await client.send_message(message.channel,reply)

client.run('NTExODk2MTE5NTY3OTc0NDAw.Dsxl7g.aFBgRs3aVBpCphX_czE30dQCOAw')
