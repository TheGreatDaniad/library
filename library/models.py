from django.db import models

class books(models.Model):
    book_name = models.CharField(max_length=40)
    book_id = models.CharField(max_length=20)
    number_of_books = models.IntegerField(default=0)
    def __str__(self):
        return self.book_name

class books_in_use(models.Model):
    book_name = models.CharField(max_length=40)
    keeper_first_name = models.CharField(max_length=  30)
    keeper_last_name = models.CharField(max_length=30)
    keeper_id = models.CharField(max_length=30)

    def __str__(self):
        return self.keeper_first_name

