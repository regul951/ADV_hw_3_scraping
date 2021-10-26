import requests
import bs4


class Scrap:
    def __init__(self, url):
        self.url = url
        response = requests.get(self.url)
        response.raise_for_status()
        self.soup = bs4.BeautifulSoup(response.text, features='html.parser')


# определяем список ключевых слов
KEYWORDS = {'дизайн', 'фото', 'web', 'python'}

habr_all_url = 'https://habr.com/ru/all/'

soup = Scrap(habr_all_url).soup
articles = soup.find_all('article')


# <дата> - <заголовок> - <ссылка>
x = 0
for article in articles:
    link = article.find(class_='tm-article-snippet__title-link').get('href')
    full_link = 'https://habr.com' + link

    if set(Scrap(full_link).soup.find(class_='tm-article-body').text.split()) & KEYWORDS:
        x += 1
        date = article.find('time').text
        head = article.find('h2').text
        print(f'{x}. {date}, "{head}" {full_link}')
