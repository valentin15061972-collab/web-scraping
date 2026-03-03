import requests
import bs4


KEYWORDS = ['дизайн', 'фото', 'web', 'python']

url = 'https://habr.com/ru/articles/'
response = requests.get(url)

soup = bs4.BeautifulSoup(response.text, features='lxml')
articles_block = soup.select_one('div.tm-articles-list')
articles_list = articles_block.select('article.tm-articles-list__item')

for article in articles_list:
    for el in KEYWORDS:
        if el in article.text.lower():
            article_with_link = article.select_one('h2.tm-title.tm-title_h2')
            link = 'https://habr.com' + article_with_link.select_one('a')['href']

            response = requests.get(link)
            article = bs4.BeautifulSoup(response.text, features='lxml')
            data = article.select_one('time')['title']
            header =article.select_one('h1').text.strip()

            print(f'<{data}>-<{header}>-<{link}>')
            break

