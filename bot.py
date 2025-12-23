import telebot
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row("📦 Services", "💰 Prices")
    keyboard.row("📝 Place Order", "📞 Contact Admin")

    bot.send_message(
        message.chat.id,
        "👋 Welcome!\nI help automate online business orders.\nChoose an option 👇",
        reply_markup=keyboard
    )

@bot.message_handler(func=lambda m: m.text == "📦 Services")
def services(m):
    bot.send_message(m.chat.id, "📦 Services:\n• Data Reselling\n• Telegram Bots\n• Digital Marketing")

@bot.message_handler(func=lambda m: m.text == "💰 Prices")
def prices(m):
    bot.send_message(m.chat.id, "💰 Prices:\nBot Setup: ₵500\nSupport: ₵150")

@bot.message_handler(func=lambda m: m.text == "📞 Contact Admin")
def contact(m):
    bot.send_message(m.chat.id, "📞 Admin: @yourusername")

bot.infinity_polling()
