import telebot
from telebot import types
import time

# --- CONFIGURATION ---
TOKEN = "YOUR_BOT_TOKEN_HERE" # Put your token here
bot = telebot.TeleBot(TOKEN)

# --- 1. START COMMAND (MAIN MENU) ---
@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    
    # Create Buttons
    btn1 = types.InlineKeyboardButton("📶 Data Services", callback_data="menu_data")
    btn2 = types.InlineKeyboardButton("🎓 Affiliate Program", callback_data="menu_affiliate")
    btn3 = types.InlineKeyboardButton("🤖 Bot Automation", callback_data="menu_bots")
    btn4 = types.InlineKeyboardButton("👤 My Account", callback_data="menu_account")
    btn5 = types.InlineKeyboardButton("📞 Contact Admin", url="https://t.me/supergigantic")

    markup.add(btn1, btn2, btn3, btn4, btn5)
    
    welcome_text = (
        "🔥 *Welcome to Gigantic Services!* 🔥\n\n"
        "Your one-stop hub for Data, Affiliate Profits, and Bot Automation.\n\n"
        "Select an option below to get started:"
    )
    bot.send_message(message.chat.id, welcome_text, parse_mode="Markdown", reply_markup=markup)

# --- 2. CALLBACK HANDLERS (BUTTON CLICKS) ---
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.data == "menu_data":
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("🌐 Visit Data Website", url="https://Giganticdatahub.shop"))
        markup.add(types.InlineKeyboardButton("💼 Become Agent (₵40)", callback_data="buy_agent"))
        markup.add(types.InlineKeyboardButton("⬅️ Back", callback_data="back_main"))
        
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, 
                             text="📶 *DATA SERVICES*\n\n• MTN, AirtelTigo, Vodafone\n• Bulk Data available\n• Agent Access: ₵40 one-time", 
                             parse_mode="Markdown", reply_markup=markup)

    elif call.data == "menu_affiliate":
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("🤝 Join Program (₵199)", callback_data="buy_affiliate"))
        markup.add(types.InlineKeyboardButton("⬅️ Back", callback_data="back_main"))
        
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, 
                             text="🎓 *AFFILIATE PROGRAM*\n\n• Earn 50% commission per sale\n• Promote professional courses\n• Open to everyone!", 
                             parse_mode="Markdown", reply_markup=markup)

    elif call.data == "menu_bots":
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("🛠 Order Bot (₵250)", callback_data="order_bot"))
        markup.add(types.InlineKeyboardButton("⬅️ Back", callback_data="back_main"))
        
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, 
                             text="🤖 *BOT AUTOMATION*\n\n• Custom Telegram Bots (₵250)\n• Monthly Management (₵70)\n• Delivery in 24 Hours", 
                             parse_mode="Markdown", reply_markup=markup)

    elif call.data == "back_main":
        # Returns to the original main menu
        send_welcome(call.message)

# --- 3. FINAL SETUP ---
print("Bot is starting...")
bot.remove_webhook() # THIS FIXES ERROR 409
time.sleep(1)
bot.polling(none_stop=True)
