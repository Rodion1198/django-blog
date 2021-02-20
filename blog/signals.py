from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Comment, Post


@receiver(post_save, sender=Post)
def post_is_created(instance, **kwargs):
    if kwargs['created']:
        subject = 'New Post!'
        message = f'New post "{instance.title}" created by <{instance.author}>'
        from_email = f'{instance.author.email}'
        send_mail(subject, message, from_email, ['admin@example.com'])


@receiver(post_save, sender=Comment)
def comment_is_created(instance, **kwargs):
    if kwargs['created']:
        subject = 'New Comment!'
        message = f'New Comment on post "{instance.post.title}" created by <{instance.name}>'
        from_email = 'test@admin.com'
        send_mail(subject, message, from_email, ['admin@example.com'])


@receiver(post_save, sender=Comment)
def send_message_to_author_post(instance, **kwargs):
    if kwargs['created']:
        subject = 'New Comment on your post!'
        message = f'New Comment created! You can check it here http://127.0.0.1:8000/article/{instance.post.pk}'
        from_email = 'test@admin.com'
        send_mail(subject, message, from_email, [instance.post.author.email])
