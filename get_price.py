# importing libraries
from bs4 import BeautifulSoup as Bs
from requests_html import HTMLSession
from datetime import datetime


def get_price(symbol):
    url = "https://finance.yahoo.com/quote/"
    # Create session
    session = HTMLSession()
    # Get url page
    data = session.get(url+symbol+"-USD")
    # converting the text
    soup = Bs(data.text, 'html.parser')

    # finding info for the current price
    price = soup.find('span', {'data-reactid': '29'}).text
    print(symbol+': $' + price + " - " + datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
    return price
