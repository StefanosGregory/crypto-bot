from get_price import get_price
from queries import insert_symbols

lines = []
with open('Data/symbols.txt') as f:
    lines = f.readlines()

count = 0
for line in lines:
    count += 1
    line = line.replace('\n', '')
    line = line.replace(' ', '')
    try:
        price = float(get_price(line))
        insert_symbols(line, price)
    except:
        pass