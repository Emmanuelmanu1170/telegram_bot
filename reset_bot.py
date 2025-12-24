import telebot
import os

# Replace with your actual bot token if not using env variable
BOT_TOKEN = os.getenv("BOT_TOKEN")  

bot = telebot.TeleBot(BOT_TOKEN)

# This removes any webhook or stuck session
bot.remove_webhook()
print("✅ Webhook removed. Bot can now poll safely."
