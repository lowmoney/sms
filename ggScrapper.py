from bs4 import BeautifulSoup
import requests

SEARCH_URL = 'https://gg.deals/games/?title='
GAME_URL = 'https://gg.deals/game/'

def search(key):

    # Load a page with games
    page = requests.get(SEARCH_URL+key).text
    soup = BeautifulSoup(page,'html.parser')

    # Scrape through the searches and find the top three games
    titles = []
    games = soup.find_all('div','details')
    for i in range(0,3):
        titles.append(games[i].find('a','ellipsis title').text.strip())
    
    # Now find the best prices for the three games
    shops = []
    prices = []
    links = []
    for title in titles:
        page = requests.get(GAME_URL + '/' + title.replace(" ",'-') + '/').text
        soup = BeautifulSoup(page,'html.parser')
        pageShops = soup.find_all('a','shop-link')
        pagePrices = soup.find_all('span','numeric')
        shopLinks = soup.find_all('a','game-hoverable full-link')
        # loop through all the shops and prices 
        for shop in pageShops:
            shops.append(shop.img['alt'])
        for price in pagePrices:
            prices.append(price.text.strip().replace('~','').split('\n')[0])
        for link in shopLinks:
            links.append(link['href'])

    # Return an array of shops and prices
    return [[shops],[prices],[links]]