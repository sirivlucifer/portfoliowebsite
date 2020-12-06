from django.db import models
from ckeditor.fields import RichTextField
from django.utils import timezone
from django.conf import settings

# Create your models here.

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    body = RichTextField(blank=True, null=True)
    created_on = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    last_modified = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField('Category', related_name='posts')

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=20)


class Comment(models.Model):
    STATUS = (
        (1, 'True'),
        (0, 'False'),
    )
    status = models.IntegerField(choices=STATUS, default=0)
    author = models.CharField(max_length=60)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)



