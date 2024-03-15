## DunastyCode 15.03.2024 ##
import asyncio
import aiohttp
import json
import aiofiles
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from config import token, chat_id, github_repo

bot = Bot(token=token)

data = {}
data['new_commit'] = []
data['last_commit'] = []

async def get_start(message: Message, bot: Bot):
    await bot.send_message(message.from_user.id, f'hello')

async def check_repo(bot: Bot):        
    while True:

        async with aiohttp.ClientSession() as session:

            async with session.get(github_repo) as response:
                commits = await response.json()

            async with aiofiles.open('data.json', mode='r') as f:
                last_data_read = await f.read()
                last_data = json.loads(last_data_read)

            if len(commits) > 0:
                commit = commits[0]['commit']['message']
                author = commits[0]['author']['login']
                time = commits[0]['commit']['author']['date']
                data['new_commit'].append({
                    'author': author,
                    'file': file,
                    'time': time})
                date_string = data['new_commit'][0]['time']
                date_parts = date_string.split("T")
                hours, minutes, seconds = map(int, date_parts[1].split("Z")[0].split(":"))

                if last_data['last_commit'][0]['time'] != data['new_commit'][0]['time']:
                    message = f"Новое изменение репозитория от {author}\nCommit: {commit}\nВремя изменения: {hours+5}:{minutes}:{seconds}"
                    await bot.send_message(chat_id=chat_id, text=message)
                else:
                    #message = "Изменений в репозитории нет"
                    #await bot.send_message(chat_id=chat_id, text=message)
                    pass

                data['last_commit'] = data['new_commit']
                data['new_commit'] = []

                async with aiofiles.open('data.json', 'w') as outfile:
                    await outfile.write(json.dumps(data))

            await asyncio.sleep(60)

async def start_bot(bot: Bot) -> None:
    dp = Dispatcher()
    dp.message.register(get_start)
    await asyncio.create_task(check_repo(bot))
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(start_bot(bot))

