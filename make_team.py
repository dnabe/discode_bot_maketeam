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
    cmd_2 = command(message.content,1)
    cmd_3 = command(message.content,2)
    list_red = []
    list_blue = []
    
    
    if message.content.startswith('/que'):
        user = [member.display_name for member in client.get_all_members() if member.voice.voice_channel is not None]
        q = user[random.randrange(0,len(user))]
        reply = '出題者は ' + str(q)
            
        await client.send_message(message.channel, reply)
    
    elif cmd_1 == '/team':
        user = [member.display_name for member in client.get_all_members() if member.voice.voice_channel is not None]
        
        for i in range(int(cmd_2)):
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
        
    elif '/' in message.content and 'd' in message.content and not message.content.startswith('/command'):
        ms = message.content.split('d')[0]
        dk = int(ms.lstrip('/'))
        dm = int(message.content.split('d')[1])
        for i in range(dk):
            dice_list += str(random.randrange(1,m + 1)) + '  '
        await client.send_message(message.channel,dice_list)
        
        
    #elif cmd_1 == '/win':
        
        #if cmd_2 == 'red':
            #point_red += int(cmd_3)
        #elif cmd_2 == 'blue':
            #point_blue += int(cmd_3)
            
        #reply = '赤チーム ： ' + str(point_red) + '    青チーム ： ' + str(point_blue)
        
        #await client.send_message(message.channel,reply)
        
    #elif message.content.startswith('/reset'):
        #point_red = 0
        #point_blue = 0
        #await client.send_message(message.channel,'ポイントをリセットしたよ！')
        
    elif message.content.startswith('/command'):
        await client.send_message(message.channel,'出題者決め：『/que』')
        await client.send_message(message.channel,'チーム分け：『/team␣〇␣△』 （〇、△には人数比）')
        await client.send_message(message.channel,'ボイスチャットのメンバー表示：『/member』')
        await client.send_message(message.channel,'ダイスを振る：『/1d6』')
        #await client.send_message(message.channel,'チームへポイントの加算：『/win␣red␣〇』 （〇は点数）')
        #await client.send_message(message.channel,'ポイントのリセット：『/reset』')
        await client.send_message(message.channel,'使用可能なコマンド確認：『/command』')
        
        
def command(message,n):
    try:
        return message.split(' ')[n]
    except IndexError:
        return ''
    

# botの接続と起動
# （tokenにはbotアカウントのアクセストークンを入れてください）
client.run('NTAyNjYzMzA1NjY0NjU5NDc3.DquIqw.Y47wNQ52eGp1mIsZMhKQBu2BEno')