from django.db import models
from django.contrib.auth.models import User



class Post(models.Model):
    STATUS = (
    (0,"Draft"),
    (1,"Publish")
)


    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now= True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now= True)
    status = models.IntegerField(choices=STATUS, default=0)
    image = models.ImageField(upload_to='images/%Y/%m/%d/', blank=True, null=True)
    

    class Meta:
        ordering = ['-created_on']
    
    def __str__(self):
        return self.title

    def approved_comments(self):
        return self.comments.filter(approved_comment=True)
    
    
    '''def clean(self):
        if not len(self.title) > 10:
            raise ValidationError(
                {'title': "Title should have at least 10 letters"})

    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)'''


class Comment(models.Model):
    for_post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=200, null=True, blank=True)
    text = models.TextField(null=True, blank=True)
    creat_on = models.DateTimeField(auto_now = True)
    approved_comment = models.BooleanField(default=False)


  

    def __str__(self):
        return self.text
# Create your models here.


class Image(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.title