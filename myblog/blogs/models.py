import datetime

from django.db import models
from django.utils import timezone


class Blog(models.Model):

    def __str__(self):
        return self.title

    title = models.CharField(max_length=200)
    art_count = models.IntegerField(default=0)


class Article(models.Model):
    def __str__(self):
        return self.headline

    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    headline = models.CharField(max_length=200)
    text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    image = models.ImageField(null=True, upload_to="blogs/static/images/")

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def get_date(self):
        return self.pub_date.strftime('%d.%m.%Y %H:%M')
