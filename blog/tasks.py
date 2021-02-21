from bs4 import BeautifulSoup
from celery import shared_task
import requests

from .models import RSSPost


@shared_task
def add_post_rss():
    try:
        r = requests.get('https://news.ycombinator.com/rss')
        soup = BeautifulSoup(r.content, features='xml')
        articles = soup.findAll('item')

        for a in articles:
            title = a.find('title').text
            link = a.find('link').text

            if RSSPost.objects.filter(title=title).exists():
                continue
            else:
                rsspost = RSSPost()
                rsspost.title = title
                rsspost.link = link
                rsspost.save()

                break

    except Exception as e:
        print('The scraping job failed. See exception:')  # noqa:T001
        print(e)  # noqa:T001

