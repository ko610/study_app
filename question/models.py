from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class PostQuestion(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='static/images')
    content = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    goods = models.IntegerField(default=0)

    def __str__(self):
        return self.content
    
