import asyncio
from telethon import TelegramClient, events

# Ваши данные от My.Telegram.org
api_id = 22555299  # Замените на ваш API_ID
api_hash = '2b9579c4a6819b874fd1d07dba63378b'  # Замените на ваш API_HASH

# Юзернеймы или ID каналов (например, '@source_channel' или -100xxxxxxxxxx)
SOURCE_CHANNEL = '@https://t.me/uijUDuC1pA44ZDQy'
TARGET_CHANNEL = '@https://t.me/hvoykin'

client = TelegramClient('reposter_session', api_id, api_hash)

@client.on(events.NewMessage(chats=SOURCE_CHANNEL))
async def handler(event):
    try:
        # Вариант 1: Копировать текст, фото и медиа БЕЗ плашки "Переслано из"
        await client.send_message(TARGET_CHANNEL, event.message)
        
        # Вариант 2: Пересылать СОХРАНЯЯ плашку "Переслано из" (раскомментируйте строку ниже)
        # await client.forward_messages(TARGET_CHANNEL, event.message)
        
        print(f"Успешно репостнуто сообщение ID: {event.message.id}")
    except Exception as e:
        print(f"Ошибка при репосте: {e}")

async def main():
    print("Бот-репостер запущен и слушает канал...")
    await client.start()
    await client.run_until_disconnected()

if __name__ == '__main__':
    asyncio.run(main())
