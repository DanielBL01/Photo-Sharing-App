from django.db import models
from django.contrib.auth import get_user_model

class Post(models.Model):
    # Foreign keys will throw errors if null or blank
    # get_user_model() grabs our current custom model 
    users = models.ForeignKey(
        get_user_model(), 
        on_delete=models.CASCADE
    )

    # numbers can be inside CharField
    title = models.CharField(max_length=60, blank=False)
    description = models.CharField(max_length=120, blank=True)
    date_posted = models.DateTimeField(auto_now_add=True)

    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    # If the post is deleted, delete all the comments as well
    post = models.ForeignKey(
        Post, 
        on_delete=models.CASCADE,

        # simple way to perform 'backwards query' --> get all comments for one post
        related_name='comments',
    )

    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )

    comment = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.comment[0:25]