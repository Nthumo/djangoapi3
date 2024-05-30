from django.db import models
from django.contrib.auth.models import User

class Book(models.Model):
    name = models.CharField(max_length=20)
    author = models.CharField(max_length=10)
    added_by = models.ForeignKey(User, default=False, on_delete=models.CASCADE)
    added_on = models.DateTimeField(auto_now=True)
    book_detail = models.TextField(max_length=500)


    def __str__(self):
        return self.name
