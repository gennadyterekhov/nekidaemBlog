from django.db import models
from django.contrib.auth.models import User



class Blog(models.Model):
    name = models.CharField(max_length=200)
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    subscribers = models.ManyToManyField(User)


    def __str__(self):
        return self.name


class Post(models.Model):
    blog_id = models.ForeignKey(Blog, on_delete=models.CASCADE)
    title = models.CharField(max_length=80)
    text = models.TextField()
    pub_date = models.DateTimeField('date published')
    views = models.ManyToManyField(User)


    def __str__(self):
        return self.title


# class View(models.Model):
#     post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
#     user_id = models.ForeignKey(User, on_delete=models.CASCADE)
