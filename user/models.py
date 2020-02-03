from django.db import models


class Post(models.Model):
    user_name = models.CharField(max_length=100, null=False)
    post_title = models.CharField(max_length=50, null=False)
    post_content = models.TextField(default='tutorial content')
    date_published = models.DateField(blank=True, null=True)
    user_profile_link = models.URLField(max_length=100, blank=True, null=True)
