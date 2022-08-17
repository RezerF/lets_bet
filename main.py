


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


def get_winner(target_date, current_price, target_price, true_wallet_bet, false_wallet2_bet):
    if target_date:
        if current_price >= target_price:
            return true_wallet_bet
        return false_wallet2_bet


def send_prize(get_winner):
    pass
