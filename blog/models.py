from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=32)
    anons = models.CharField(max_length=100)
    text = models.TextField()
    image = models.ImageField(upload_to='blog')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title


class Tag(models.Model):
    name = models.CharField(max_length=32)
    post = models.ManyToManyField(Post)

    def __str__(self):
        return self.name


class Comment(models.Model):
    text = models.CharField(max_length=32)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username + ' - '+self.text[:10]


class Profile(models.Model):
    avatar = models.ImageField(upload_to='blog/static/blog/images')
    bio = models.CharField(max_length=50)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
