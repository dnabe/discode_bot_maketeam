import discord

client = discord.Client()

@client.event
async def on_ready():
    print('ログインしました')

@client.event
async def on_message(message):

    if message.author.id == '279562735635660800':
        reply = '@劇的ファン たくみんが話したよ！'
        await client.send_message(message.channel,reply)

client.run('NTExODk2MTE5NTY3OTc0NDAw.Dsxl7g.aFBgRs3aVBpCphX_czE30dQCOAw')
