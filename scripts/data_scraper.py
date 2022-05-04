from requests import get 
from bs4 import BeautifulSoup as bs 
import datetime 
import pandas as pd 

def scraping_stock_news(keyword='IHSG', base_url='https://www.kontan.co.id', path_search='/search/?search=', n=100):
    url = base_url + path_search + keyword
    news_list = []
    while True:
        page = get(url) 
        soup = bs(page.content, 'html.parser')

        div_sp_hl = soup.find_all('div', class_='sp-hl')
        news_list = news_list + [x.find('a').text for x in div_sp_hl]

        if len(news_list) >= n:
            return news_list
        
        if soup.find('ul', class_='cd-pagination') != None:
            ul_cd_pagination = soup.find('ul', class_='cd-pagination')
            a_next_button = ul_cd_pagination.find_all('a')[-1]
            url = base_url + a_next_button['href']
        else:
            return news_list

if __name__ == '__main__':
    print(scraping_stock_news(n=30))