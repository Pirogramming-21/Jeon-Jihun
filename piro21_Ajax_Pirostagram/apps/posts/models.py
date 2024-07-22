from django.db import models
from apps.users import models as user_model

# Create your models here.

class Post(models.Model):
    author = models.ForeignKey(
                                user_model.User,
                                null=True,
                                on_delete=models.CASCADE,
                                related_name = 'post_author'
                            )
    image = models.ImageField(blank=False, upload_to='posts/%Y%m%d')
    caption = models.TextField(blank=False)
    post_likes = models.ManyToManyField(
                                user_model.User, 
                                blank=True,
                                related_name='post_likes'
                            )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.author}: {self.caption}"
    
class Comment(models.Model):
    author = models.ForeignKey(
            user_model.User, 
            null=True, 
            on_delete=models.CASCADE, 
            related_name= 'comment_author'
        )
    posts = models.ForeignKey(
            Post, 
            null=True, 
            on_delete=models.CASCADE, 
            related_name= 'comment_post'
        )
    
    contents = models.TextField(blank=True)
   
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.author}: {self.contents}"