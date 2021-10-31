# importing libraries
import json
import ssl
import urllib.request


# method to get the price of specific coin
def get_price(url, coin, currency):
    # unverified ssl
    ssl._create_default_https_context = ssl._create_unverified_context
    # getting the request from url
    with urllib.request.urlopen(url+coin+"&tsyms=USD,EUR") as url:
        data = json.loads(url.read().decode())

    # return the price
    return data[currency]
