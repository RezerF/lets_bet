


def contract(person1, person2, condition):
    if condition is True:
        pass

active_pare = ETH/BTC
current_date = 0
expiration_date = 356
target_price = 0.14
# coefficient = 1
prize_fund_usdt_erc20 = 2000
wallet1 = "0xbf.."
wallet2 = " 0xba.."
bet_wallet1 = True # input
bet_wallet2 = False # input

target_date = current_date + expiration_date
current_price = 0.2

"""
цена eth/btc в течение года должна достигнуть 0.14
Участник1 говорит "Правда"
Участник2 говорит "Ложь"
Каждый ставит по 500 долларов

=================================================
            ####Смарт-контракт####
Если текущее время меньше либо равно времени экспирации:
    Если текущая цена больше либо равна 0.14:
        Отправь деньги на первый кошелек(Участник1)
        Отправь сообщение проигравшему
        Закрой смарт-контракт
Иначе:
    Отправь деньги на второй кошелек(Участник2)
    Отправь сообщение проигравшему
    Закрой смарт-контракт
"""

def get_winner(target_date, current_price, target_price, true_wallet_bet, false_wallet2_bet):
    if target_date:
        if current_price >= target_price:
            return true_wallet_bet
        return false_wallet2_bet


def send_prize(get_winner):
    pass
