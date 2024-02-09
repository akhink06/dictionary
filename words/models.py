from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=255)
    user = models.OneToOneField("auth.User" , on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    

class Word(models.Model):
    word = models.CharField(max_length=100 , unique=True)
    definition = models.TextField()
    synonymns = models.CharField(max_length=255)

    author = models.ForeignKey("words.Author", on_delete = models.CASCADE)


    def __str__(self):
        return self.word