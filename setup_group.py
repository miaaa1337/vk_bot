import os
import asyncio
from vkbottle import API
from dotenv import load_dotenv

load_dotenv()

async def main():
    api = API(token=os.getenv("VK_TOKEN"))
    
    try:
        await api.request(
            "groups.setSettings",
            {
                "group_id": 238512761, 
                "bots_capabilities": 1,
                "bots_start_button": 0,
                "bots_add_to_chats": 1,
                "bots_allowed_to_add_chats": 1,
                "bots_read_all_messages": 1 
            }
        )
        print("=== НАСТРОЙКА ВКЛЮЧЕНА! БОТ ТЕПЕРЬ ВИДИТ МАТЫ ===")
    except Exception as e:
        print(f"Ошибка: {e}")

asyncio.run(main())
