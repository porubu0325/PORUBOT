import discord
from discord.ext import commands, tasks
import datetime

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
    # 定時実行タスクを開始
    send_time.start()
    send_image.start()

@tasks.loop(hours=1)
async def send_time():
    now = datetime.datetime.now()
    # 毎時0分に実行
    if now.minute == 0:
        current_time = now.strftime("%H:%M")
        # 任意のテキストチャンネルIDを指定
        channel_id = YOUR_CHANNEL_ID  # ここにチャンネルIDを入力

        channel = bot.get_channel(channel_id)
        if channel:
            await channel.send(f'現在の時刻は {current_time} です。')

@tasks.loop(minutes=30)
async def send_image():
    # 任意のテキストチャンネルIDを指定
    channel_id = YOUR_CHANNEL_ID  # ここにチャンネルIDを入力
    image_path = 'your_image.png'  # ここに画像ファイルのパスを入力

    channel = bot.get_channel(channel_id)
    if channel:
        with open(image_path, 'rb') as file:
            image = discord.File(file)
            await channel.send(file=image)

        
# Botトークンをセットアップ
bot.run("YOUR_BOT_TOKEN")