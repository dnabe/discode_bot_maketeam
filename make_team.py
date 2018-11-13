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
    dice_list = []
    #point_dic = {}
    #point_red = -1
    #point_blue = -1


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
        await client.send_message(message.channel,str(len(user)) + '人')

    elif '/' in message.content and 'd' in message.content and not message.content.startswith('/command'):
        ms = message.content.split('d')[0]
        dk = int(ms.lstrip('/'))
        dm = int(message.content.split('d')[1])
        for i in range(dk):
            dice_list += [random.randrange(1,dm + 1)]
        await client.send_message(message.channel,dice_list)

    elif message.author.id == '433511130439090178':
        await client.send_message(message.channel,'hello')

    #elif cmd_1 == '/win':

        #if cmd_2 == 'red':
            
            #point_dic['赤チーム'] = point_red
        #elif cmd_2 == 'blue':

            #point_dic['青チーム'] = point_blue

        #for i,j in point_dic.items():
            #await client.send_message(message.channel,i + ':' + str(j))




    #elif message.content.startswith('/reset'):
        #point_red = 0
        #point_blue = 0
        #await client.send_message(message.channel,'ポイントをリセットしたよ！')

    elif message.content.startswith('/command'):
        await client.send_message(message.channel,'出題者決め：『/que』')
        await client.send_message(message.channel,'チーム分け：『/team␣〇␣△』 （〇、△には人数）')
        await client.send_message(message.channel,'ボイスチャットのメンバー表示：『/member』')
        await client.send_message(message.channel,'ダイスを振る：『/1d6』')
        #await client.send_message(message.channel,'チームへポイントの加算：『/win␣red』')
        #await client.send_message(message.channel,'ポイントのリセット：『/reset』')
        await client.send_message(message.channel,'使用可能なコマンド確認：『/command』')


def command(message,n):
    try:
        return message.split(' ')[n]
    except IndexError:
        return ''



# botの接続と起動
# （tokenにはbotアカウントのアクセストークンを入れてください）
client.run('NTAyNjYzMzA1NjY0NjU5NDc3.DrMHIw.UxQPCELNo3z1cjePxmkYnCBstkc')
