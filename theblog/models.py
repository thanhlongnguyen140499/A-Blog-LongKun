from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields.related import OneToOneField
from django.urls import reverse
from datetime import datetime, date
from ckeditor.fields import RichTextField

# Create your models here.

class Category(models.Model):

    name = models.CharField(max_length=255, default='coding')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        # return reverse('article-detail', args=(str(self.id))) # Go to detail page
        return reverse('home')   # Khong can args -> vi trong urls khong co <int:pk>


class Profile(models.Model):
    user = OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(default='bio of user')
    profile_pic = models.ImageField(null=True, blank=True, upload_to="profile/")
    website_url = models.CharField(max_length=255, null=True, blank=True)
    fb_url = models.CharField(max_length=255, null=True, blank=True)
    twitter_url = models.CharField(max_length=255, null=True, blank=True)
    instagram_url = models.CharField(max_length=255, null=True, blank=True)
    pinterest_url = models.CharField(max_length=255, null=True, blank=True)
    
    def __str__(self):
        return str(self.user)

    def get_absolute_url(self):
        return reverse('home')

    
class Post(models.Model):
    title = models.CharField(max_length=255)
    header_image = models.ImageField(null=True, blank=True, upload_to="images/")
    title_tag = models.CharField(max_length=255, default='Long Kun Blogs')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=255, default='coding')
    snippet = models.CharField(max_length=255)
    # body = models.TextField()
    body = RichTextField(blank=True, null=True)
    post_date = models.DateField(auto_now_add=datetime.now)
    likes = models.ManyToManyField(User, related_name='blog_posts')

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        # return reverse('article-detail', args=(str(self.id))) # Go to detail page
        return reverse('home')   # Khong can args -> vi trong urls khong co <int:pk>

