# importing libraries
import get_price as gp
import get_coins_symbol as gcs

# calling the get_price method
# gcs.get_symbols()
# url of cryptocurrency prices
url = "https://min-api.cryptocompare.com/data/price?fsym="

# calling the get_price method
ans = gp.get_price(url, 'MANA', 'EUR')

# printing the ans
print(ans)
