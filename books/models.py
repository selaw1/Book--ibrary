from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Author(models.Model):

    name = models.OneToOneField(User, on_delete=models.CASCADE )

    def get_absolute_url(self):
        return reverse('books:author_detail', kwargs={'pk':self.pk})

    def __str__(self):
        return str(self.name)

class Book(models.Model):

    title = models.CharField(max_length=255, null=False, blank=False)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=False, blank=False, related_name='book_author')

    def __str__(self):
        return self.title
