import threading
import get_price as gp
from Helpers.notify import notify
from queries import select_favorites, select_all
from Helpers.console_colors import bcolors as color


def check_favorites_symbols_rise_fall():
    print('------------------------------')
    # Load favorites coins from db
    favorites = select_favorites()
    # For all coins in favorites
    for favorite in favorites:
        try:
            # Take the price
            price = float(gp.get_price(favorite.coin_symbol))
            # If current price smaller than /2 of favourite price alert
            if price <= float(favorite.starter_price) / 2:
                print(color.FAIL + "Coin with symbol " + favorite.coin_symbol + " fall 50%" + price + color.RESET)
                notify("Coin " + favorite.coin_symbl + " fall 50% ", favorite.coin_symbol)
            # If current price bigger than x2 of favourite price alert
            elif price >= float(favorite.starter_price) * 2:
                print(color.OK + "Coin with symbol " + favorite.coin_symbol + " rise 50%" + price + color.RESET)
                notify("Coin " + favorite.coin_symbol + " rise 50% ", favorite.coin_symbol)
        except:
            print(color.FAIL + "Price for " + favorite.coin_symbol + " not found! Skipping.." + color.RESET)

    # Loop every 10 seconds
    timer = threading.Timer(10, check_favorites_symbols_rise_fall)
    # Start for loop
    timer.start()


def check_fall():
    print('------------------------------')
    # Load favorites coins from db
    symbols = select_all()
    # For all coins in favorites
    for symbols in symbols:
        try:
            # Take the price
            price = float(gp.get_price(symbols.coin_symbol))
            # If current price smaller than /2 of favourite price alert
            if price <= float(symbols.starter_price) / 2:
                print(color.FAIL + "Coin with symbol " + symbols.coin_symbol + " fall 50%" + price + color.RESET)
                notify("Coin " + symbols.coin_symbl + " fall 50% ", symbols.coin_symbol)
        except:
            print(color.FAIL + "Price for " + symbols.coin_symbol + " not found! Skipping.." + color.RESET)

    # Loop every 10 seconds
    timer = threading.Timer(10, check_fall)
    # Start for loop
    timer.start()
