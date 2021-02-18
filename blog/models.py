# import sys

from ckeditor.fields import RichTextField

from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
# from django.core.files.uploading import InMemoryUploadedFile

# from PIL import Image
# from io import BytesIO


User = get_user_model()


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    @staticmethod
    def get_absolute_url():
        return reverse('home')


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField()
    profile_image = models.ImageField(null=True, blank=True, upload_to='images/user_profile')   # noqa: DJ01
    website_url = models.CharField(max_length=255, null=True, blank=True)   # noqa: DJ01
    facebook_url = models.CharField(max_length=255, null=True, blank=True)  # noqa: DJ01
    twitter_url = models.CharField(max_length=255, null=True, blank=True)   # noqa: DJ01
    instagram_url = models.CharField(max_length=255, null=True, blank=True)     # noqa: DJ01
    pinterest_url = models.CharField(max_length=255, null=True, blank=True)     # noqa: DJ01

    def __str__(self):
        return str(self.user)


class Post(models.Model):
    title = models.CharField(max_length=250)
    header_image = models.ImageField(null=True, blank=True, upload_to='images/')   # noqa: DJ01
    title_tag = models.CharField(max_length=250)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=255)
    snippet = models.CharField(max_length=255)
    body = RichTextField(blank=True, null=True)
    post_date = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='blog_posts')

    def count_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        return reverse('article-detail', args=[self.id])

    # def save(self, *args, **kwargs):
    #     image = self.header_image
    #     img = Image.open(image)
    #     new_img = img.convert('RGB')
    #     resized_new_img = new_img.resize((400, 400), Image.ANTIALIAS)
    #     filestream = BytesIO()
    #     resized_new_img.save(filestream, "JPEG", quality=90)
    #     name = '{}.{}'.format(*self.header_image.name.split('.'))
    #     self.header_image = InMemoryUploadedFile(
    #         filestream, 'Imagefield', name, 'jpeg/header_image', sys.getsizeof(filestream), None
    #     )
    #     super().save(*args, **kwargs)
