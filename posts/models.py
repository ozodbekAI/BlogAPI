from django.db import models

from config import settings

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)
    slug = models.CharField(max_length=255, blank=False, null=False)


    def __str__(self) -> str:
        return self.name
    

class Tag(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)

    def __str__(self) -> str:
        return self.name



class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="posts")
    title = models.CharField(max_length=255, blank=False, null=False)
    content = models.TextField(blank=False, null=False)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name="posts")
    tags = models.ManyToManyField(Tag, related_name='posts')
    publish_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)


    def __str__(self) -> str:
        return self.title


class LikeDislike(models.Model):
    LIKE = 1
    DISLIKE = -1

    VOTE_CHOICES = (
        (LIKE, 'Like'),
        (DISLIKE, 'Dislike')
    )

    post = models.ForeignKey(Post, related_name='likes_dislikes', on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='likes_dislikes', on_delete=models.CASCADE)
    vote = models.SmallIntegerField(choices=VOTE_CHOICES)

class Comment(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="user")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="post")
    comment = models.TextField(blank=False, null=False)
    created_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f'Comment by {self.author} on {self.post}'


