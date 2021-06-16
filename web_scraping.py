from pprint import pprint

import requests
from bs4 import BeautifulSoup as bs

# определяем список ключевых слов
KEYWORDS = {'дизайн', 'фото', 'web', 'python'}
page = 'https://habr.com/ru/all/'


def get_keywords(main_link, kewords):
    request = requests.get(main_link).text
    soup = bs(request, 'html.parser')
    article_list = []
    articles = soup.find_all('article', class_='post_preview')
    for article in articles:
        date_ = article.find('span', class_='post__time').text
        title = article.find('a', class_='post__title_link').text.lower()
        title_text = {t for t in title.split()}
        link = article.find('a', class_='post__title_link').attrs.get('href')
        text_ = article.find('div', class_='post__text').text.lower()
        preview_text = {t for t in text_.split()}
        sub_request = requests.get(link).text
        sub_soup = bs(sub_request, 'html.parser')
        t_articles = sub_soup.find('div', class_='post__body_full').text.lower()
        text_article = {t for t in t_articles.split()}
        if text_article & kewords or preview_text & kewords or title_text & kewords:
            article_list.append([title, date_, link])
    return article_list


request = requests.get(page)
if request.status_code == 200:
    print('Advanced task')
    pprint(get_keywords(page, KEYWORDS))
else:
    print('Site is not working')


#  Проба без set()
# def get_articles_2(main_link, keywords):
#     request = requests.get(main_link).text
#     soup = bs(request, 'html.parser')
#     article_list = []
#     articles = soup.find_all('article', class_='post_preview')
#     for article in articles:
#         temp_dict = {}
#         date_ = article.find('span', class_='post__time').text
#         title = article.find('a', class_='post__title_link').text
#         link = article.find('a', class_='post__title_link').attrs.get('href')
#         text_ = article.find('div', class_='post__text').text.strip()
#         sub_request = requests.get(link).text
#         sub_soup = bs(sub_request, 'html.parser')
#         text_articles = sub_soup.find('div', class_='post__body post__body_full').text.strip()
#         for key in keywords:
#             if (key in text_.lower()) or (key in title.lower()) or (key in text_articles.lower()):
#                 temp_dict[key] = [title, date_, link]
#                 article_list.append(temp_dict)
#     #  Удаление дублей
#     a2 = []
#     [a2.append(x) for x in article_list if x not in a2]
#     return a2
#
# # request = requests.get(page)
# # if request.status_code == 200:
# #     print('Advanced task')
# #     pprint(get_articles_2(page, KEYWORDS))
# # else:
# #     print('Site is not working')
