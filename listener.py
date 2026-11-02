import os
import logging
from telethon import TelegramClient, events
from dotenv import load_dotenv

# Импортируем вашу функцию публикации из main.py
from main import publish_telegram_post

load_dotenv()

# Ваши данные с my.telegram.org
API_ID = int(os.getenv("TELEGRAM_API_ID", 0))
API_HASH = os.getenv("TELEGRAM_API_HASH", "")

# Источник (чужой канал) и ваш целевой канал
SOURCE_CHANNEL = '@source_channel_username'  # Юзернейм чужого канала (например, @conifers_pro)

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

client = TelegramClient('session_userbot', API_ID, API_HASH)

@client.on(events.NewMessage(chats=SOURCE_CHANNEL))
async def handle_new_post(event):
    message = event.message
    post_text = message.text or message.caption or ""
    
    if not post_text or len(post_text) < 50:
        return  # Пропускаем слишком короткие посты или пустые сообщения
        
    logging.info(вальв=f"Перехвачено новый пост из {SOURCE_CHANNEL}")

    image_path = None
    # Если к посту прикреплено фото, скачиваем его во временный файл
    if message.photo:
        try:
            image_path = await message.download_media(file="temp_listener_img.jpg")
        except Exception as e:
            logging.error(f"Не удалось скачать фото из поста: {e}")

    # Формируем структуру данных, которую ожидает ваш publish_telegram_post
    # Если у вас в main.py картинка ждет URL, можно использовать локальный файл или загрузку на ImgBB
    article_data = {
        "text": post_text,
        "image_url": None, # Или передать ссылку, если загружаете на ImgBB
        "url": f"https://t.me/{message.chat.username}/{message.id}" if message.chat else ""
    }

    try:
        # Передаем в ваш основной обработчик (Gemini перепишет текст, создаст Telegraph и опубликует)
        publish_telegram_post(article_data)
        logging.info("Пост успешно переработан и опубликован в ваш канал!")
    except Exception as e:
        logging.error(f"Ошибка при публикации перехваченного поста: {e}")

def main():
    if not API_ID or not API_HASH:
        logging.error("Не указаны TELEGRAM_API_ID или TELEGRAM_API_HASH в .env файле!")
        return
        
    print("Юзербот запущен и слушает чужой канал...")
    client.start()
    client.run_until_disconnected()

if __name__ == '__main__':
    main()
