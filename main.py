import get_price as gp


# url of the bit coin price
url = "https://www.google.com/finance/quote/"+"BTC-USD"

# calling the get_price method
ans = gp.get_price(url)

# printing the ans
print(ans)
