# -*- coding: utf-8 -*-
# @Time : 2020/7/3 15:24
# @Author : Mamamooo
# @Site :
# @File : py_jx_20_4_douban.py
# @Software: PyCharm
"""

"""

import requests
from bs4 import BeautifulSoup
import bs4
#
# def main():
#     url = "https://movie.douban.com/cinema/later/beijing/"
#     init_page = requests.get(url).content
#     print(init_page)
#     init_soup = BeautifulSoup(init_page, 'lxml')
#     print(init_soup)
#
#     all_movies = init_soup.find('div', id="showing-soon")
#     print(all_movies)
#     for each_movie in all_movies.find_all('div', class_="item"):
#         all_a_tag = each_movie.find_all('a')
#         all_li_tag = each_movie.find_all('li')
#
#         movie_name = all_a_tag[1].text
#         url_to_fetch = all_a_tag[1]['href']
#         movie_date = all_li_tag[0].text
#
#         response_item = requests.get(url_to_fetch).content
#         soup_item = BeautifulSoup(response_item, 'lxml')
#         img_tag = soup_item.find('img')
#
#         print('{} {} {}'.format(movie_name, movie_date, img_tag['src']))
#
# main()


import asyncio
import aiohttp

from bs4 import BeautifulSoup


async def fetch_content(url):
    async with aiohttp.ClientSession(
            connector=aiohttp.TCPConnector(ssl=False)
    ) as session:
        async with session.get(url) as response:
            return await response.text()


async def main():
    url = "https://movie.douban.com/cinema/later/beijing/"
    init_page = await fetch_content(url)
    init_soup = BeautifulSoup(init_page, 'lxml')

    movie_names, urls_to_fetch, movie_dates = [], [], []

    all_movies = init_soup.find('div', id="showing-soon")
    for each_movie in all_movies.find_all('div', class_="item"):
        all_a_tag = each_movie.find_all('a')
        all_li_tag = each_movie.find_all('li')

        movie_names.append(all_a_tag[1].text)
        urls_to_fetch.append(all_a_tag[1]['href'])
        movie_dates.append(all_li_tag[0].text)

    tasks = [fetch_content(url) for url in urls_to_fetch]
    pages = await asyncio.gather(*tasks)

    for movie_name, movie_date, page in zip(movie_names, movie_dates, pages):
        soup_item = BeautifulSoup(page, 'lxml')
        img_tag = soup_item.find('img')

        print('{} {} {}'.format(movie_name, movie_date, img_tag['src']))


asyncio.run(main())
