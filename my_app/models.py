from django.db import models

# Create your models here.


class Search(models.Model):
    search = models.CharField(max_length=500)
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return {}.format(self.search)

    class Meta:
        verbose_name_plural = "Searches"

# class DateTimeBox(models.Model):


class PopularThread(models.Model):
    rank = models.IntegerField()
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=512)
    made_from = models.CharField(max_length=30)
    thumbnail_img_url = models.URLField()
    original_path = models.URLField()
