#
import logging
import telebot
from telebot import types

from secret import API_TOKEN

loger = logging.getLogger(__name__)
loger.setLevel(logging.DEBUG)

bot = telebot.TeleBot(API_TOKEN)

AVAILABLE_PAIRS = ["ETH/USDT", "BTC/USDT", "ETH/BTC"]
pair = None
goal_price = None
expiration = None
bet = None
bet_size = "$100"


# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """Привет, я пари Бот.\nХочешь поспорить о цене криптоактива? Тогда жми /letsBet""")


@bot.message_handler(commands=["letsBet"])
def lets_bet(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    ups = [
        types.InlineKeyboardButton("ETH/USDT", callback_data="ETH/USDT"),
        types.InlineKeyboardButton("BTC/USDT", callback_data="BTC/USDT"),
        types.InlineKeyboardButton("ETH/BTC", callback_data="ETH/BTC"),
    ]
    markup.add(*ups)
    msg = bot.reply_to(message, "На какую пару спорим?", reply_markup=markup)
    bot.register_next_step_handler(msg, get_pair)


def get_pair(message):
    global pair
    pair = message.text
    loger.warning(f"Logger: {pair}")
    bot.reply_to(message, "Какой таргет? Впиши цифру")
    bot.register_next_step_handler(message, get_target_price)


def get_target_price(message):
    global goal_price
    goal_price = message.text
    loger.warning(f"Logger: {goal_price}")
    bot.reply_to(message, "В течение скольки дней, цена достигнет таргета? Впиши цифру")
    bot.register_next_step_handler(message, get_expiration)


def get_expiration(message):
    global expiration
    expiration = message.text
    loger.warning(f"Logger: {expiration}")
    markup = types.InlineKeyboardMarkup()
    ups = [
        types.InlineKeyboardButton("Достигнет", callback_data="Достигнет"),
        types.InlineKeyboardButton("НЕ Достигнет", callback_data="НЕ Достигнет"),
    ]
    markup.add(*ups)
    bot.send_message(message.chat.id, "В течение заданого времени цена ... таргета?", reply_markup=markup)
    # bot.register_next_step_handler(message.message, get_bet)


@bot.callback_query_handler(func=lambda call: True)
def get_bet(call):
    global bet
    bet = call.data
    loger.warning(f"Logger: {bet}")
    bot.send_message(call.message.chat.id, "Проверим контракт? /check")


@bot.message_handler(commands=["check"])
def check_contract(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    ups = [
        types.InlineKeyboardButton("Верно", callback_data="accept"),
        types.InlineKeyboardButton("Не Верно", callback_data="decline"),
    ]
    markup.add(*ups)
    msg = bot.reply_to(
        message, (f"Контракт звучит верно? : \"\"\"Я ставлю {bet_size} на то что цена\n"
                  f" пары {pair} {bet} таргета, в течение {expiration} дней\"\"\""),
        reply_markup=markup
    )
    bot.register_next_step_handler(msg, final_accept)


def final_accept(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    ups = [
        types.InlineKeyboardButton("Размещаем", callback_data="accept"),
        types.InlineKeyboardButton("Не Размещаем", callback_data="decline"),
    ]
    markup.add(*ups)
    msg = bot.reply_to(
        message, (f"Размещаем контракт в блокчейне (etherium)?"),
        reply_markup=markup
    )
    bot.register_next_step_handler(msg, build_and_deploy_smart_contract)


def build_and_deploy_smart_contract(message):
    count = 0.1
    address = "0xbad.....4dgffd4"
    x = (f"Отправьте {count} ETH на этот адресс {address}."
     f" Если второй участник не отправит в конктракт такуюже сумму"
     f" в течение 12 часов, контракт не будет считаться заключеным"
     f" и средства вернуться вам обратно")
    bot.reply_to(message, x)


bot.infinity_polling()
