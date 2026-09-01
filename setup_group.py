import os
import asyncio
from vkbottle import API
from dotenv import load_dotenv

load_dotenv()

async def main():
    # Берём твой токен группы из .env
    api = API(token=os.getenv("VK_TOKEN"))
    
    try:
        # Вызываем правильный метод ВК для изменения настроек сообщества
        await api.request(
            "groups.setSettings",
            {
                "group_id": 238512761, # ОБЯЗАТЕЛЬНО: впиши сюда цифры ID твоей группы!
                "bots_capabilities": 1,
                "bots_start_button": 0,
                "bots_add_to_chats": 1,
                "bots_allowed_to_add_chats": 1,
                "bots_read_all_messages": 1 # ВОТ ОНА! Эта строчка включает доступ к переписке
            }
        )
        print("=== НАСТРОЙКА ВКЛЮЧЕНА! БОТ ТЕПЕРЬ ВИДИТ МАТЫ ===")
    except Exception as e:
        print(f"Ошибка: {e}")

asyncio.run(main())
