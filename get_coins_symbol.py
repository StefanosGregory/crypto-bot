# importing libraries
import json
import ssl
import urllib.request


def get_symbols():
    # Method to extract from cryptocompare all cryptos symbols
    # unverified ssl
    ssl._create_default_https_context = ssl._create_unverified_context
    # getting the request from url
    with urllib.request.urlopen("https://www.cryptocompare.com/api/data/coinlist/") as url:
        # load json data
        data = json.loads(url.read().decode())
    # Filter data
    data = data['Data']
    # Open txt.file
    text_file = open("Data/symbols.txt", "w")

    for coin in data:
        text_file.write(data[coin]['Symbol'] + "\n")

    text_file.close()
