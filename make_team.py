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
    list_red = []
    list_blue = []
    
    if message.content.startswith('/que'):
        user = [member.display_name for member in client.get_all_members() if member.voice.voice_channel is not None]
        q = user[random.randrange(0,len(user))]
        reply = '出題者は' + str(q)
            
        await client.send_message(message.channel, reply)
    
    elif cmd_1 == '/team':
        user = [member.display_name for member in client.get_all_members() if member.voice.voice_channel is not None]
        l = len(user)
        for i in range(l):
            re = user[random.randrange(0,len(user))]
            list_red += [re]
            user.remove(re)
        list_blue = user
            
        await client.send_message(message.channel,'赤チームは')
        await client.send_message(message.channel,list_red)
        await client.send_message(message.channel,'青チームは')
        await client.send_message(message.channel,list_blue)
    
    elif message.content.startswith('/member'):
        user = [member.display_name for member in client.get_all_members() if member.voice.voice_channel is not None]
        await client.send_message(message.channel,user)
        
    elif message.content.startswith('/command'):
        await client.send_message(message.channel,'出題者決め：『/que』')
        await client.send_message(message.channel,'チーム分け：『/team␣〇␣△』 （〇、△には人数比）')
        await client.send_message(message.channel,'ボイスチャットのメンバー表示：『/member』')
        await client.send_message(message.channel,'使用可能なコマンド確認：『/command』')
        
        
def command(message,n):
    try:
        return message.split(' ')[n]
    except IndexError:
        return ''
    

# botの接続と起動
# （tokenにはbotアカウントのアクセストークンを入れてください）
client.run('NTAyNjYzMzA1NjY0NjU5NDc3.DquIqw.Y47wNQ52eGp1mIsZMhKQBu2BEno')