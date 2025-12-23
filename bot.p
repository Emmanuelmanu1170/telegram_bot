import os
import telebot

# Environment variable for security on Railway
BOT_TOKEN = os.getenv("BOT_TOKEN")  # Set this on Railway
ADMIN_CHAT_ID = 123456789  # Replace with your Telegram ID

bot = telebot.TeleBot(BOT_TOKEN)

# Temporary storage for orders
ordering = {}

# Services & Prices
SERVICES = {
    "Data Reselling": "Custom pricing",
    "Telegram Automation": "Custom pricing",
    "Digital Marketing": "Custom pricing",
    "Social Media Boosting": {
        "TikTok Followers": "₵35 / 1000",
        "TikTok Likes": "₵35 / 1000",
        "TikTok Views": "₵22 / 1000",
        "Instagram Followers": "₵40 / 1000",
        "Instagram Likes": "₵25 / 1000",
        "Instagram Views": "₵30 / 1000",
        "YouTube Views": "₵40 / 1000",
        "YouTube Likes": "₵25 / 1000",
        "YouTube Subscribers": "₵50 / 1000",
        "Telegram Members": "₵40 / 1000",
        "Telegram Views": "₵40 / 1000",
        "Facebook Followers": "₵35 / 1000",
        "Facebook Likes": "₵35 / 1000",
        "Facebook Views": "₵22 / 1000",
        "WhatsApp Channel Members": "₵100 / 1000",
        "LinkedIn AI Growth": "₵340 / 1000"
    }
}

# Start command
@bot.message_handler(commands=['start'])
def start(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row("📦 Services", "💰 Prices")
    keyboard.row("📝 Place Order", "📞 Contact Admin")
    bot.send_message(message.chat.id,
                     "👋 Welcome!\nI help automate online business orders and social media boosting.\nChoose an option below 👇",
                     reply_markup=keyboard)

# Services menu
@bot.message_handler(func=lambda message: message.text == "📦 Services")
def services(message):
    text = "📦 Our Services:\n"
    for service in SERVICES:
        text += f"- {service}\n"
    bot.send_message(message.chat.id, text)

# Prices menu
@bot.message_handler(func=lambda message: message.text == "💰 Prices")
def prices(message):
    text = "💰 Prices:\n"
    for service, price in SERVICES.items():
        if isinstance(price, dict):
            text += f"\n{service}:\n"
            for sub_service, sub_price in price.items():
                text += f" - {sub_service}: {sub_price}\n"
        else:
            text += f"- {service}: {price}\n"
    bot.send_message(message.chat.id, text)

# Start order process
@bot.message_handler(func=lambda message: message.text == "📝 Place Order")
def place_order(message):
    ordering[message.chat.id] = True
    bot.send_message(message.chat.id,
                     "📝 Send your order in this format:\nName:\nService:\nQuantity / Details:")

# Handle order messages
@bot.message_handler(func=lambda message: True)
def handle_order(message):
    if ordering.get(message.chat.id):
        bot.send_message(ADMIN_CHAT_ID, f"📢 NEW ORDER RECEIVED:\n\n{message.text}\nFrom: @{message.chat.username}")
        bot.send_message(message.chat.id, "✅ Order received! Admin will contact you soon.")
        ordering[message.chat.id] = False
    else:
        bot.send_message(message.chat.id, "❓ Please choose an option from the menu.")

# Contact admin
@bot.message_handler(func=lambda message: message.text == "📞 Contact Admin")
def contact_admin(message):
    bot.send_message(message.chat.id, "📩 You can contact the admin directly on Telegram: @YourTelegramUsername")

# Run the bot
bot.polling()
