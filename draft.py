#
import telebot
from telebot import types

API_TOKEN = '5560543776:AAHHVSdYILQRFfDTShlgj2jTe7whL5Q79m4'

bot = telebot.TeleBot(API_TOKEN)

AVAILABLE_PAIRS = ["ETH/USDT", "BTC/USDT", "ETH/BTC"]
pair = None


# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """Привет, я пари Бот.\nХочешь поспорить о цене криптоактива? Тогда жми /letsBet""")


# # Handle all other messages with content_type 'text' (content_types defaults to ['text'])
# @bot.message_handler(func=lambda message: True)
# def echo_message(message):
#     bot.reply_to(message, message.text)


# Handle '/letsBet'
@bot.message_handler(commands=['letsBet'])
def lets_bet(message):
    markup = types.InlineKeyboardMarkup()
    ups = [
        types.InlineKeyboardButton("ETH/USDT", callback_data="ETH/USDT"),
        types.InlineKeyboardButton("BTC/USDT", callback_data="BTC/USDT"),
        types.InlineKeyboardButton("ETH/BTC", callback_data="ETH/BTC"),
    ]
    markup.add(*ups)
    bot.reply_to(message, "На какую пару спорим?", reply_markup=markup)
    bot.register_next_step_handler(message, duration_offer)


@bot.callback_query_handler(func=lambda c: c.data in AVAILABLE_PAIRS)
def choose_pair(callback_query):
    global pair
    pair = callback_query.data
    print(pair)
    bot.answer_callback_query(callback_query.id, text=pair)
    msg = bot.send_message(callback_query.from_user.id, f"Вы выбрали: {pair}")
    bot.register_next_step_handler(msg, get_duration)
    # bot.register_callback_query_handler(get_duration, func=lambda c: c.data in AVAILABLE_PAIRS)


def get_duration(message):
    x = message
    bot.send_message(message.chat.id, "You send")
    pass


@bot.message_handler()
def duration_offer(message):
    # markup = types.InlineKeyboardMarkup()
    # markup.add()
    text = message.text
    if text.isdigit():
        duration = text
    else:
        bot.reply_to(message, "Только цифру!!")
    bot.reply_to(message, "В течение какого времени наступит событие?\n Впишите цифру в днях")


# @bot.message_handler()
# def about_message(message):
#     bot.reply_to(message, message)


bot.infinity_polling()
