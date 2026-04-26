from django.db import models
from django.db.models import DateTimeField
from django.db.models import TextField
from django.db.models import CharField
from django.db.models import ManyToManyField
from django.db.models import ForeignKey
from django.db.models import.CASCADE

class Author(models.Model):
    name = CharField(max_length=255, unique=True)
    email = CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = CharField(max_length=255)
    content = TextField()
    tags = ManyToManyField(Tag)
    author = ForeignKey(Author, on_delete=CASCADE)
    created_at = DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title