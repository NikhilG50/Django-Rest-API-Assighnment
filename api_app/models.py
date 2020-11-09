from django.db import models
from django.contrib.contenttypes.fields import GenericRelation
from star_ratings.models import Rating


class Authors(models.Model):
    first_name = models.CharField(max_length=150, blank=False, null=False)
    last_name = models.CharField(max_length=150)
    address = models.TextField(max_length=150)
    gender = models.SmallIntegerField()
    dob = models.DateField(null=True)

    def __str__(self):
        return self.first_name +' '+ self.last_name


class Book(models.Model):
    auther_id = models.ForeignKey(Authors, on_delete=models.CASCADE)
    Book_title = models.CharField(max_length=150)
    Books_pages = models.SmallIntegerField()
    pusbhish_date = models.DateField(auto_now_add=True)
    Book_cost = models.IntegerField()
    is_activate = models.BooleanField(default=True)
    ratings = GenericRelation(Rating, related_query_name='foos')

    def __str__(self):
        return self.Book_title