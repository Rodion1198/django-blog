import os

from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'simple_blog.settings')

app = Celery('simple_blog')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

app.conf.beat_schedule = {
    'scraping_rss_posts': {
        'task': 'blog.tasks.add_post_rss',
        'schedule': crontab('1-23/2'),
    }
}
