import discord # インストールした discord.py
import random

client = discord.Client() # 接続に使用するオブジェクト

# 起動時に通知してくれる処理
@client.event
async def on_ready():
    print('ログインしました')

# メッセージによる処理
@client.event
async def on_message(message):
    
    cmd_1 = command(message.content,0)
    red_team = command(message.content,1)
    blue_team = command(message.content,2)
    l = len(user)
    num_team = list_team()
    list_red = []
    list_blue = []
    
    if message.content.startswith('/que'):
        user = [member.display_name for member in client.get_all_members() if member.voice.voice_channel is not None]
        q = user[random.randrange(0,len(user))]
        reply = '出題者は' + str(q)
            
        await client.send_message(message.channel, reply)
    
    elif cmd_1 == '/team'
        user = [member.display_name for member in client.get_all_members() if member.voice.voice_channel is not None]
        for i in range(int(red_team)):
            list_red[i] = user[random.randrange(0,len(user))]
            user.remove(list_red[i])
        list_blue = user
        reply = red_team + 'vs' + blue_team
            
        await client.send_message(message.channel,reply)
        
def command(message,n):
    try:
        return message.split(' ')[n]
    except IndexError:
        return ''
    

# botの接続と起動
# （tokenにはbotアカウントのアクセストークンを入れてください）
client.run('NTAyNjYzMzA1NjY0NjU5NDc3.DquIqw.Y47wNQ52eGp1mIsZMhKQBu2BEno')