def get_increase_rate(current_price, base_price):
    increase_rate = round(((current_price - base_price)/base_price)*100, 2)
    # print(f'increase rate = {increase_rate}')
    return increase_rate

def get_buying_amount(balance, price, coherence):
    amount = (balance / price) * coherence
    return round(amount,2)