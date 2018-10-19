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
    if message.content.startswith('/role'):
        user = [member.display_name for member in client.get_channel("502664510193139773")]
        q = user[random.randrange(0,len(user))]
        reply = '出題者は' + str(q)
            
        await client.send_message(message.channel, reply)
    

# botの接続と起動
# （tokenにはbotアカウントのアクセストークンを入れてください）
client.run('NTAyNjYzMzA1NjY0NjU5NDc3.DqrSDw.7MLkjJ3dW0-7BFN3yijFGAFUxYU')