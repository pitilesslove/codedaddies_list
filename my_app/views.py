import requests
from requests.compat import quote_plus
from django.shortcuts import render
from bs4 import BeautifulSoup
from . import models

BASE_CRAIGSLIST_URL = 'https://losangeles.craigslist.org/search/?query={}'
DAUM_CAFE_URL = "https://m.cafe.daum.net"


def home(request):
    page = requests.get(DAUM_CAFE_URL)
    soup = BeautifulSoup(page.content, features='html.parser')
    popular_top_50_list = soup.find_all(class_='popular-list')

    popular_thread_list = []
    for part_of_html_list in popular_top_50_list:
        one_html_list = part_of_html_list.findAll('li')
        for a_list in one_html_list:
            original_link_address = DAUM_CAFE_URL + a_list.find(
                class_='popular-list__link')['href']

            thumbnail_image_url = 'http:' + a_list.find("img").get('src')
            rank = a_list.find(class_='popular-list__rank').getText()[2:]
            thread_title = a_list.find("strong").getText()
            made_from = a_list.find(class_='popular-list__cafe-name').getText()
            # print(image_tag)
           # models.PopularThread.objects.create(
           #     rank=int(rank[2:]), made_from=made_from, title=thread_title, thumbnail_img_url=original_link_address, original_path=original_link_address)
            popular_thread_list.append(
                (rank, thread_title, thumbnail_image_url, made_from, original_link_address))
        stuff_for_frontend = {
            # 'contents': models.PopularThread.objects.all(),
            'contents': popular_thread_list,
        }

    return render(request, 'base.html', stuff_for_frontend)


def new_search(request):
    search = request.POST.get('search')
    models.Search.objects.create(search=search)
    final_url = BASE_CRAIGSLIST_URL.format(quote_plus(search))
    response = requests.get(final_url)
    data = response.text

    stuff_for_frontend = {
        'search': search,
    }
    return render(request, 'my_app/new_search.html', stuff_for_frontend)
