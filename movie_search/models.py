# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Movies(models.Model):
    movie_title = models.CharField(max_length=300)
    movie_content = models.TextField(blank=True, null=True)
    movie_download_url = models.TextField(blank=True, null=True)
    movie_type = models.CharField(max_length=10, blank=True, null=True)
    movie_come_from_url = models.CharField(max_length=600, blank=True, null=True)
    fetch_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'movies'
        unique_together = (('id', 'movie_title'),)

class Blog(models.Model):
    title = models.CharField(max_length = 100)
    content = models.TextField()

    def __str__(self):
        return self.title

class Book(models.Model):
    title = models.CharField(max_length = 100)
    content = models.TextField()

    def __str__(self):
        return self.title

class Writer(models.Model):
    name = models.CharField(max_length = 50)
    address = models.CharField(max_length = 100)
    email = models.CharField(max_length = 100)
    book_ids = models.ManyToManyField(Book)
    blog_ids = models.ManyToManyField(Blog)

    def __str__(self):
        return self.name
