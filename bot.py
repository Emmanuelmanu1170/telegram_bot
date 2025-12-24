import os
import telebot

BOT_TOKEN = os.getenv("BOT_TOKEN")

if not BOT_TOKEN:
    raise RuntimeError("BOT_TOKEN is missing")

bot = telebot.TeleBot(BOT_TOKEN, parse_mode="HTML")

@bot.message_handler(commands=["start"])
def start(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row("📦 Services", "💰 Prices")
    keyboard.row("📞 Contact Admin")

    bot.send_message(
        message.chat.id,
        "👋 <b>Welcome</b>\nChoose an option 👇",
        reply_markup=keyboard
    )

@bot.message_handler(func=lambda m: m.text == "📦 Services")
def services(m):
    bot.send_message(
        m.chat.id,
        "📦 <b>Services</b>\n• Data Reselling\n• Social Media Boosting\n• Telegram Automation"
    )

@bot.message_handler(func=lambda m: m.text == "💰 Prices")
def prices(m):
    bot.send_message(
        m.chat.id,
        "💰 <b>Prices</b>\nBot Setup: ₵500\nSupport: ₵150"
    )

@bot.message_handler(func=lambda m: m.text == "📞 Contact Admin")
def contact(m):
    bot.send_message(
        m.chat.id,
        "📞 Admin: @yourusername"
    )

bot.polling(# This removes any old connections (Fixes Error 409)
bot.remove_webhook()

# Then start the bot
bot.polling(none_stop=True)
 )
