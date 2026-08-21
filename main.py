import os
import asyncio
import re
from vkbottle.bot import Bot, Message
from dotenv import load_dotenv

load_dotenv()

bot = Bot(token=os.getenv("VK_TOKEN"))

BAD_WORDS = [
    "дурак", "дебил", "идиот", "тварь", "мразь", "лошара", "клоун", "тупой", "тупая", "мать шлюха", "тварь дрожащая", "тварь мерзкая", "тварь гнида", "тварь подлая", "хуеглот", "хуеглотка", "спермоглот", "манда", "спидозная", "гнида", "блять", "блядота", "мать давалка", "шлюха", "шлюшка", "шлюшко", "залупа", "гей", "геи", "хохлы", "обьебосы", "хуесосы", "пидор", "пидоры",
    "хуй", "сука", "блядь", "гондон", "уебок", "ебанат", "уебище", "давалка", "тупорылая", "ебланище", "козлина", "пидорас", "еблан", "ебучий", "ебучая", "ебучее", "петушок", "тупорылый", "чмоня", "уебак", "наркоман", "петушара", "лохушка", "чмо", "спидозный", "идиотский", "конченный", "залупный", "пидорский", "говно", "говноедский", "говнячий", "говнючий", "ебанное", "ебаное", "ёбанное", "ёбло", "ебло", "ебало", "еблище", "ебальце", "ебасос", "чвк", "рф", "президент",
    "хохол", "кацап", "чурка", "негр", "даун", "хач", "сво", "z", "svo", "всу", "украина", "россия", "путин", "зеленский", "свиньи", "фашисты", "укроп", "негретос", "нигга", "долбаеб", "долбоеб", "долбоёб", "долбаёб", "долбаёбы", "долбаёбов", "долбаёбами", "кончелыга", "пидораха"
]

# Компилируем регулярное выражение ОДИН РАЗ при запуске бота
# \b означает границы слова. re.IGNORECASE игнорирует большие/маленькие буквы
BAD_WORDS_PATTERN = re.compile(r'\b(' + '|'.join(BAD_WORDS) + r')\b', re.IGNORECASE)


# ==================== 1. КОМАНДА БАНА ====================
@bot.on.chat_message(text=".бан")
async def ban_user(message: Message):
    if message.reply_message:
        victim_id = message.reply_message.from_id
        try:
            await bot.api.messages.remove_chat_user(
                chat_id=message.peer_id - 2000000000,
                user_id=victim_id
            )
            await message.answer("забанено! 🚫")
        except Exception as e:
            await message.answer(f"не палучилось забанеть(( :  {e}")
    else:
        await message.answer("ответь на сообщение того, кого хочешь забанить!")

# ==================== 2. ОБЩИЙ ОБРАБОТЧИК (МАТЫ + ПРИВЕТСТВИЕ) ====================
@bot.on.chat_message()
async def handle_message(message: Message):
    # Сначала проверяем на приветствие (системное действие)
    if message.action and message.action.type.value == "chat_invite_user" and message.action.member_id == -message.group_id:
        await message.answer(
            "привет! я классный бот защитник твоей бедной фейк странички.\n"
            "чтобы я мог обезопасить чат, выдай мне права администратора."
        )
        return

    # Если это обычное текстовое сообщение — проверяем маты через регулярку
    if message.text:
        # Проверяем, есть ли совпадение в тексте
        if BAD_WORDS_PATTERN.search(message.text):
            try:
                # Получаем имя автора мата
                users = await bot.api.users.get(user_ids=message.from_id)
                user = users[0]
                name = f"{user.first_name} {user.last_name}"
                
                # Переотправляем текст от лица бота
                await message.answer(f"{name}: {message.text}")

                # Сносим оригинал
                await message.ctx_api.messages.delete(
                    cmids=[message.conversation_message_id], 
                    delete_for_all=True, 
                    peer_id=message.peer_id
                )
            except Exception as e:
                print(f"Ошибка при удалении мата: {e}")
            return

print("бот запущен!")
bot.run_forever()