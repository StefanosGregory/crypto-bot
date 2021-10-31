# importing libraries
from bs4 import BeautifulSoup as Bs
import requests


# method to get the price of specific coin
def get_price(url):
    # getting the request from url
    data = requests.get(url)

    # converting the text
    soup = Bs(data.text, 'html.parser')

    # finding meta info for the current price
    info = soup.find("div", class_="YMlKec fxKbKc").text

    # return the price
    return info
